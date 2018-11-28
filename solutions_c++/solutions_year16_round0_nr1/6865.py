#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

vector<bool> flag(10, false);
int count = 0;

void solve(int a)
{
	while (a>0)
	{
		int temp = a%10;
		a/=10;
		if (!flag[temp])
		{
			flag[temp] = true;
			count++;
		}
	}
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");
	int T;
	fin>>T;
	for (int i = 1;i<=T;i++)
	{
		int N;
		fin>>N;
		if (N==0)
		{
			fout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		for (int i = 0;i<10;i++)
			flag[i] = false;
		int temp = 0;
		count = 0;
		while (count<10)
		{
			temp+=N;
			solve(temp);
			if (temp>N*100)
				break;
		}
		if (count>=10)
			fout<<"Case #"<<i<<": "<<temp<<endl;
		else fout<<"Case #"<<i<<": INSOMNIA"<<endl;
	}
	//fin>>T;
	fin.close();
	fout.close();
	return 0;
}