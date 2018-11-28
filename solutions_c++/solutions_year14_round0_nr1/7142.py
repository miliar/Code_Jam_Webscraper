/*
ID: devraj.2
PROG: ride
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;
const static string filename ="A";

string Solve()
{
	int answer = 0;
	string v_cheat = "Volunteer cheated!";
	string m_cheat = "Bad magician!";
	stringstream sout;
	int a[4][4],b[4][4];
	int answer1,answer2;
	int count = 0;
	cin>>answer1;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			cin>>a[i][j];
	cin>>answer2;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			cin>>b[i][j];

	for(int i = 0 ;i<4;i++)
		for(int j=0;j<4;j++)
		{
			if(a[answer1 - 1][i] == b[answer2 -1][j])
			{
				count++;
				answer = a[answer1 - 1][i];
			}
			if(count > 1)
				break;
		}
		if(count == 0)
			sout<<v_cheat;
		else if(count == 1)
			sout<<answer;
		else
			sout<<m_cheat;


	return sout.str();
}


void SolveSmall()
{
	//A-small-attempt0
	string inFile = filename + "-small" +"-attempt1"+ ".in" ;
	string outFile = filename + "-small"+"-attempt1" + ".out";

	freopen(outFile.c_str()  ,"w",stdout);
	freopen(inFile.c_str() ,"r", stdin);

}

void SolveLarge()
{
	string inFile = filename + "-large" + ".in" ;
	string outFile = filename + "-large" + ".out";

	freopen(inFile.c_str()  ,"w",stdout);
	freopen(outFile.c_str() ,"r", stdin);

}

int main() {

		SolveSmall();
		int t_testCase = 0;
		cin>>t_testCase;
		for(int t = 0; t < t_testCase; ++t)
		{
			cout<<"Case #"<<t+1<<": "<<Solve()<<endl;

		}

    return 0;
}