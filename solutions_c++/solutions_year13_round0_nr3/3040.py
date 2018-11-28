#include<iostream>
#include<fstream>
#include<cstring>
#include<cstdio>
#include<cmath>
using namespace std;


bool isPr(int t)
{
	char oneline[100];
	sprintf(oneline,"%d",t);
	int l=strlen(oneline);
	int ll=l/2;
	int i;
	for(i=0;i<ll;i++)
	{
		if(oneline[i]!=oneline[l-1-i])
			break;
	}
	return i>=ll;

}


int main()
{
	int N;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	fin>>N;

	for(int k=0;k<N;k++)
	{
		int a,b;
		fin>>a>>b;
		int count=0;
		for(int i=a;i<=b;i++)
		{
			int t=(int)(sqrt((double)i)+0.5);
			int tt=t*t;
			if(tt==i)
			{
				if(isPr(t)&&isPr(i))
				{
					count++;
					//cout<<i<<endl;
				}
			}
		}
		fout<<"Case #"<<k+1<<": "<<count<<endl;;
	}
	return 0;
}
