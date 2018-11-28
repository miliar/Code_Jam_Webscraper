#include <iostream>
#include <cstring>
#include <set>
#include <fstream>
using namespace std;
typedef unsigned long long ULL;
bool isFull(char* flag, int n)
{
	int sum=0;
	for(int i=0;i<n;i++)
	{
		if(*(flag+i)!=0)
			++sum;
	}
	if(sum==n)
		return true;
	return false;
}

int main()
{
	int t=0;
	ifstream inf("A-large.in");
	ofstream otf("out.txt");
	inf>>t;
	int cntr=0;
	ULL n;
	char flag[10];
	char digit[50];
	set<ULL> sset;
	while(cntr<t)
	{
		inf>>n;
		sset.clear();
		memset(flag,0,sizeof(flag));
		ULL step=1;
		ULL rst=n;
		while(!isFull(flag,10))
		{
			ULL nn=step*n;
			if(sset.find(nn)!=sset.end())
			{
				rst=0;
				break;
			}

			rst=nn;
			sset.insert(nn);
			sprintf(digit,"%d",nn);
			int len=strlen(digit);
			for(int i=0;i<len;i++)
			{
				int num=digit[i]-'0';
				if(flag[num]==0) ++flag[num];

			}
			++step;
		}
		otf<<"Case #"<<cntr+1<<": ";
		cout<<"Case #"<<cntr+1<<": ";
		if(rst>0)
		{
			otf<<rst<<endl;
			cout<<rst<<endl;
		}
		else
		{
			otf<<"INSOMNIA"<<endl;
			cout<<"INSOMNIA"<<endl;
		}
		cntr++;
	}
	return 0;
}