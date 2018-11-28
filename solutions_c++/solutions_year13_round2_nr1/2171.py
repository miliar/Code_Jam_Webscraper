/*
ID: bchen
PROG: osmos
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int cur;

int time_needed(int a, int b)
{
	int cnt = 0;
	if(a < 2)
	{
		return 99999999;
	}
	while(a<=b)
	{
		cnt++;
		a = 2*a-1;
	}
	cur = a;
	return cnt;
}

int main()
{
	
	ifstream fin("osmos.in");

	int T;
	fin>>T;
	
	///*
	ofstream fout("osmos.out");
	for(int i=0;i<T;i++)
	{
		int A, N;
		fin>>A>>N;
		int cnt = 0;
		vector<int> motes;
		for(int k=0;k<N;k++)
		{
			int tmp;
			fin>>tmp;
			motes.push_back(tmp);
		}	

		sort(motes.begin(), motes.end());
		eat:
		while(motes.size() > 0 && A > motes[0])
		{
			A += motes[0];
			motes.erase(motes.begin());
		}
		while(motes.size() > 0)
		{
			int x = time_needed(A,motes[0]);
			if(x < (int)motes.size())
			{
				cnt += x;
				A = cur;
				//cout<<"x: "<<x<<endl;
				//cout<<"cnt: "<<cnt<<endl;
				//cout<<"size: "<<motes.size()<<endl;
				//cout<<"A: "<<A<<endl;
				//cout<<"MIN: "<<motes[0]<<endl;
				goto eat;
			}
			else
			{
				cnt += motes.size();
				break;
			}
		}
		fout<<"Case #"<<i+1<<": "<<cnt<<endl;
		//cout<<"Case #"<<i+1<<": "<<cnt<<endl;
	}
	//*/
	return 0;
}
