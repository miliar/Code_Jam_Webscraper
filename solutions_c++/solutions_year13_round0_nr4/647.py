
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <string>
#include <Windows.h>
#include <algorithm>

using namespace std;

CRITICAL_SECTION		CS;

enum TASK_STATE
{
	TASK_ADDED,
	TASK_PROCESSING,
	TASK_COMPLETED,
};

struct chest {
	int						type;
	int						open;
	vector<int>				keys;
};

struct task
{
	int						case_number;
	int						state;
	string					result;

	int						K;
	int						N;
	vector<int> 			keys;
	vector<chest>			chests;

	task					(int case_number) : case_number(case_number), state(TASK_ADDED) {}
};

struct task_pred {
  bool		operator()		(const task& lhs, const task& rhs) {
	  return lhs.case_number < rhs.case_number;
  }
};

vector<task>				tasks;

void clone_chests			(vector<chest> &src, vector<chest> &res)
{
	res.assign				(src.begin(), src.end());
}

void open_chest				(chest &ch, vector<int> &src, vector<int> &res, vector<int>::iterator &skip_it)
{
	ch.open					= true;
	res.reserve				(src.size()-1+ch.keys.size());
	for (vector<int>::iterator it = src.begin(); it != src.end(); ++it) {
		if (it == skip_it)	continue;
		res.push_back		(*it);
	}
	for (int i=0; i<(int)ch.keys.size(); ++i) {
		res.push_back		(ch.keys[i]);
	}
}

bool impossible_to_open		(vector<chest> &chests, vector<int> &keys)
{
	vector<int> available;
	available.assign		(keys.begin(), keys.end());

	for (int i=0, size=chests.size(); i!=size; ++i) {
		chest &ch			= chests[i];
		if (ch.open)		continue;
		int type			= ch.type;
		if (available.end() != ::find(available.begin(), available.end(), type)) continue;
		bool closed			= true;
		for (int j=0; j!=size; ++j) {
			chest &test		= chests[j];
			if (test.type == type) continue;
			if (test.keys.end() != ::find(test.keys.begin(), test.keys.end(), type)) {
				closed		= false;
				break;
			}
		}
		if (closed)			return true;
	}

	vector<int> required;
	for (int i=0, size=chests.size(); i!=size; ++i) {
		chest &ch			= chests[i];
		if (ch.open)		continue;
		required.push_back	(ch.type);
		for (int k=0, k_size=ch.keys.size(); k!=k_size; ++k) {
			available.push_back(ch.keys[k]);
		}
	}
	::sort					(required.begin(), required.end());
	::sort					(available.begin(), available.end());

	for (int i=0, size=required.size(); i!=size; ++i) {
		int type			= required[i];
		int count			= 1;
		for (int j=i+1; j<size; ++j) {
			if (required[j] != type) break;
			++count;
		}
		vector<int>::iterator low	= lower_bound(available.begin(), available.end(), type);
		vector<int>::iterator up	= upper_bound(available.begin(), available.end(), type);
		if (count > (up - low)) {
			return true;
		}
	}
	return false;
}

bool open_chests			(vector<chest> &chests, vector<int> &keys, vector<int> &result)
{
	if (keys.empty()) {
		for (int i=0, size=chests.size(); i!=size; ++i) {
			chest &ch			= chests[i];
			if (!ch.open)		return false;
		}
		return true;
	}
	if (impossible_to_open(chests, keys)) {
		return false;
	}
	bool all_open			= true;
	for (int i=0, size=chests.size(); i!=size; ++i) {
		chest &ch			= chests[i];
		if (ch.open)		continue;
		all_open			= false;
		vector<int>::iterator it = ::find(keys.begin(), keys.end(), ch.type);
		if (it == keys.end())	continue;
		vector<int> clone_keys;
		open_chest			(ch, keys, clone_keys, it);
		if (open_chests(chests, clone_keys, result)) {
			result.push_back(i);
			return true;
		}
		ch.open				= false;
	}
	return all_open;
}

void execute_task			(task& t)
{
	vector<int> result;
	if (!open_chests(t.chests, t.keys, result)) {
		t.result			= "IMPOSSIBLE";
		return;
	}
	std::stringstream out;
	for (int i=0, size=result.size(); i!=size; ++i) {
		out << (result[size - i - 1] + 1);
		if (i!=size-1) {
			out << " ";
		}
	}

	t.result				= out.str();
}

bool get_line				(ifstream& stream, char* buffer, int buffer_size)
{
	if (!stream.good()) {
		cout << "wrong input file format" << endl;
		return false;
	}
	stream.getline			(buffer, buffer_size);
	return true;
}

bool read_task				(task& t, ifstream& file)
{
	char buffer[4*4096];
	if (!get_line(file, buffer, sizeof(buffer))) {
		return false;
	}
	{
		stringstream ss		(buffer);
		ss >> t.K;
		ss >> t.N;
	}
	t.chests.resize			(t.N);
	if (!get_line(file, buffer, sizeof(buffer))) {
		return false;
	}
	{
		stringstream ss		(buffer);
		for (int i=0; i<t.K; ++i) {
			int key;
			ss >> key;
			t.keys.push_back(key);
		}
	}
	for (int i=0; i<t.N; ++i) {
		if (!get_line(file, buffer, sizeof(buffer))) {
			return false;
		}
		stringstream ss		(buffer);
		chest &ch			= t.chests[i];
		ch.open				= 0;
		ss >> ch.type;
		int key_count;
		ss >> key_count;
		ch.keys.resize		(key_count);
		for (int i=0; i<key_count; ++i) {
			ss >> ch.keys[i];
		}
	}

	return true;
}

void print_task				(task& t)
{
	//cout << "Task #" << t.case_number << " Text = " << t.N << endl;
}

void print_result			(task& t)
{
	cout << "Case #" << t.case_number << ": " << t.result.c_str() << endl;
}

DWORD WINAPI worker_thread	(void* arg)
{
	while (true) {
		task* t				= 0;
		{
			EnterCriticalSection(&CS);
			for (int i=0, size=tasks.size(); i!=size; ++i) {
				if (tasks[i].state == 0) {
					t		= &tasks[i];
					t->state= TASK_PROCESSING;
					break;
				}
			}
			LeaveCriticalSection(&CS);
		}
		if (t == 0) {
			return 0;
		}
		execute_task		(*t);
		t->state			= TASK_COMPLETED;
	}
	return 0;
}

int main					(int argc, char** argv)
{
	if (argc < 2) {
		cout << "Input file missing" << endl;
		return -1;
	}
	int time				= timeGetTime();
	ifstream file			(argv[1]);
	if (!file.is_open()) {
		return -1;
	}
	char line[4*4096];
	file.getline			(line, sizeof(line));
	int line_count			= atoi(line);
	for (int i=0; i!=line_count; ++i) {
		task t(i+1);
		if (!read_task(t, file)) {
			return -1;
		}
		tasks.push_back		(t);
	}

	if (IsDebuggerPresent()) {
		for (int i=0; i!=tasks.size(); ++i) {
			task& t			= tasks[i];
			//print_task	(t);
			execute_task	(t);
			print_result	(t);
		}
	} else {
		InitializeCriticalSection(&CS);
		HANDLE handles[4];
		for (int i=0; i<4; ++i) {
			handles[i]			= CreateThread( NULL, 0, &worker_thread, 0, 0, 0);
		}
		WaitForSingleObject		(handles[0], INFINITE);
		WaitForSingleObject		(handles[1], INFINITE);
		WaitForSingleObject		(handles[2], INFINITE);
		WaitForSingleObject		(handles[3], INFINITE);
		DeleteCriticalSection	(&CS);
		::sort					(tasks.begin(), tasks.end(), task_pred());
		//cout << "Work done in [" << timeGetTime() - time << "] ms" << endl;
		for (int i=0; i!=tasks.size(); ++i) {
			print_result		(tasks[i]);
		}
	}
	return 0;
}
