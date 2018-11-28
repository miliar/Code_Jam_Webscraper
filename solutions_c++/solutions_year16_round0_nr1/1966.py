#include<iostream>
#include<fstream>
#include<set>
using namespace std;


int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int N;
	fin>>N;
	int judge[11];
	judge[0]=1;
	for(int i=1;i<11;i++)
	{
		judge[i]=judge[i-1]*2;
	}
	judge[10]--;
	for(int n=1;n<=N;n++)
	{
		long long l;
		fin>>l;
		//l=2;
		if(!l)
		{
			fout<<"Case #"<<n<<": INSOMNIA"<<endl;
			continue;
		}
		
		int state=0;
		long long sum=l;
		while(true)
		{
			long long tmp=sum;
			while(tmp)
			{
				state|=judge[tmp%10];
				tmp/=10;
			}
			if(state==judge[10])
			{
				fout<<"Case #"<<n<<": "<<sum<<endl;
				break;
			}
			sum+=l;
			if(sum<0)
			{
				fout<<"Case #"<<n<<": INSOMNIA"<<endl;
				break;
			}
		}
		
	}fout.close();
		fin.close();
	return 0;
}