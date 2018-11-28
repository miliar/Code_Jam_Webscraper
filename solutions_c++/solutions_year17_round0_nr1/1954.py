
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

struct Task
{
	int						case_number;
	int						state;
	string					result;
	int						time;

	string					S;
	unsigned int			K;

	Task					() : case_number(-1), state(TASK_ADDED) {}
};

vector<Task>				tasks;

void execute_task			(Task& t)
{
	stringstream ss;
	if (t.K > t.S.length()) {
		ss << "IMPOSSIBLE";
		t.result = ss.str();
		return;
	}
	int invert = 0;
	int end = t.S.length() - t.K;
	for (int i = 0; i <= end; ++i) {
		if (t.S[i] == '-') {
			int count = i + t.K;
			for (int j = i; j < count; ++j) {
				if (t.S[j] == '-') {
					t.S[j] = '+';
				} else {
					t.S[j] = '-';
				}
			}
			++invert;
		}
	}
	for (unsigned int i = t.S.length() - t.K; i < t.S.length(); ++i) {
		if (t.S[i] == '-') {
			ss << "IMPOSSIBLE";
			t.result = ss.str();
			return;
		}
	}
	ss << invert;
	t.result				= ss.str();
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

bool read_task				(Task& t, ifstream& file)
{
	char buffer[4*4096];
	if (!get_line(file, buffer, sizeof(buffer))) {
		return false;
	}
	{
		stringstream ss		(buffer);
		ss >> t.S;
		ss >> t.K;
	}
	//t.lawn.resize			(t.Cols);
	//for (int i=0; i<t.Cols; ++i) {
	//	t.lawn[i].resize	(t.Rows);
	//}
	//for (int r=0; r<t.Rows; ++r) {
	//	if (!get_line(file, buffer, sizeof(buffer))) {
	//		return false;
	//	}
	//	stringstream ss		(buffer);
	//	for (int c=0; c<t.Cols; ++c) {
	//		ss >> t.lawn[c][r];
	//	}
	//}

	return true;
}

void print_task				(Task& t)
{
	//cout << "Task #" << t.case_number << " Text = " << t.N << endl;
}

void print_result			(Task& t)
{
	cout << "Case #" << t.case_number << ": " << t.result.c_str() << endl;
}

DWORD WINAPI worker_thread	(void* arg)
{
	while (true) {
		Task* t				= 0;
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
	tasks.resize			(line_count);
	for (int i=0; i!=line_count; ++i) {
		Task& t = tasks[i];
		t.case_number = i + 1;
		if (!read_task(t, file)) {
			return -1;
		}
	}

	if (IsDebuggerPresent()) {
		for (int i=0; i!=tasks.size(); ++i) {
			Task& t			= tasks[i];
			t.time			= timeGetTime();
			//print_task	(t);
			execute_task	(t);
			t.time			= timeGetTime() - t.time;
			//cout << "Task " << t.case_number << " done in [" << t.time << "] ms" << endl;
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

		//cout << "Work done in [" << timeGetTime() - time << "] ms" << endl;
		for (int i=0; i!=tasks.size(); ++i) {
			print_result		(tasks[i]);
		}
	}
	return 0;
}
