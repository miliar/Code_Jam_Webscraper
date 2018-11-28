#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<list>
using namespace std;

int grow(int i)
{
	return 2*i-1;
}

int main(void)
{
	ifstream ifs;
	ifs.open("A-small-attempt2.in",ios_base::in);
	ofstream ofs;
	ofs.open("A-small-attempt2.out",ios_base::trunc);
	int T;
	ifs>>T;

	for(int caseNo=1;caseNo<=T;caseNo++)
	{
		int A,N;
		ifs>>A>>N;
		vector<int>mote;
		for(int i=0;i<N;i++)
		{
			int temp;
			ifs>>temp;
			mote.push_back(temp);
		}
		sort(mote.begin(),mote.end());
		int total=0;
		int current=A;
		int i=0;
		int j=0;
		while(i<N)
		{
			if(A==1)
			{
				total=N;
				break;
			}
			if(current>mote[i])
			{
				current+=mote[i];
				i++;
				j=i;
			}
			else
			{
				current=grow(current);
				total++;
				j++;
			}
			if(j>=N)
			{
				break;
			}
		}

		ofs<<"Case #"<<caseNo<<": "<<total<<endl;
	}
			
}