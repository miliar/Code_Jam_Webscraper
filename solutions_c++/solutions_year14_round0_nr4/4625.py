
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
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

struct task
{
	int						case_number;
	int						state;
	string					result;

	vector<double>			Naomi;
	vector<double>			Ken;

	task					(int case_number) : case_number(case_number), state(TASK_ADDED) {}
};

struct task_pred {
  bool		operator()		(const task& lhs, const task& rhs) {
	  return lhs.case_number < rhs.case_number;
  }
};

vector<task>				tasks;

void execute_task			(task& t)
{
	int war_score			= 0;
	int deceitful_score		= 0;
	int size				= t.Naomi.size();
	std::sort				(t.Naomi.begin(), t.Naomi.end());
	std::sort				(t.Ken.begin(), t.Ken.end());
	vector<double> ken		= t.Ken;
	for (int i=0; i!=size; ++i) {
		double n			= t.Naomi[i];
		auto it				= ::upper_bound(ken.begin(), ken.end(), n);
		if (it == ken.end()) {
			++war_score;
			ken.erase		(ken.begin());
		} else {
			ken.erase		(it);
		}
	}
	ken						= t.Ken;
	for (int i=0; i!=size; ++i) {
		double n			= t.Naomi[i];
		auto it				= ::lower_bound(ken.begin(), ken.end(), n);
		if (it == ken.begin()) {
			ken.pop_back	();
		} else {
			++deceitful_score;
			ken.erase		(it-1);
		}
	}
	stringstream out;
	out << deceitful_score << " " << war_score;
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
	int count				= 0;
	{
		stringstream ss	(buffer);
		ss >> count;
	}
	t.Naomi.resize			(count);
	t.Ken.resize			(count);
	if (!get_line(file, buffer, sizeof(buffer))) {
		return false;
	}
	{
		stringstream ss	(buffer);
		for (int i=0; i<count; ++i) {
			ss >> t.Naomi[i];
		}
	}
	if (!get_line(file, buffer, sizeof(buffer))) {
		return false;
	}
	{
		stringstream ss	(buffer);
		for (int i=0; i<count; ++i) {
			ss >> t.Ken[i];
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
