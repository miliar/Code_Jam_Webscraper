#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string taskname = "A-large";

int in_T;
int answer=0;

void start_task(ifstream &fd_in, ofstream &fd_out);
int solve(int in_Smax, string test_case);

int main() {

	ifstream fd_in(taskname + ".in");
	if(!fd_in)
	{
		cout << "Error: can't open input file " << (taskname + ".in") << endl;;
		return -1;
	}

	ofstream fd_out(taskname + ".out");
	if(!fd_out)
	{
		cout << "Error: can't open output file "<< (taskname + ".out") << endl;;
		return -1;
	}

	start_task(fd_in, fd_out);

	fd_in.close();
	fd_out.close();


	return 0;
}

void start_task(ifstream &fd_in, ofstream &fd_out)
{
	fd_in >> in_T;
	int in_Smax;
	string test_case;

	for(int i=1;i<=in_T;i++)
	{
		fd_in >> in_Smax;
		fd_in >> test_case;
		fd_out << "Case #" << i << ": " << solve(in_Smax, test_case) << endl;
	}
}


int solve(int in_Smax, string test_case)
{
	answer = 0;
	int sum = 0;
	int num;

	for(int i = 0; i< in_Smax+1;i++)
	{
		num = test_case[i] - 0x30;

		if(sum<i)
		{
			answer += i-sum;
			sum += i-sum;

		}
			sum += num;
	}



	return answer;
}
