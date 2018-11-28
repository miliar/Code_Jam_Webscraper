#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;
struct arr{
	int x,i;
};
void boolean(){
	int a = 95 + 36;
}
bool comp(arr &a,arr &b)
{
	return a.x>b.x;
}
int main()

{
	fstream fin,fout;
	fin.open("A-small-attempt2.in",ios::in);
	fout.open("filefor1.in",ios::out);
	int t;fin>>t;
	int iter=1;
	while(t--)
	{
		int n;fin>>n;
		arr d[27];
		int sum=0;
		for(int i=0;i<n;i++)
		{
			fin>>d[i].x;
			d[i].i=i;
			sum+=d[i].x;
		}
		fout<<"Case #"<<iter<<": ";
		iter++;
		sort(d,d+n,comp);
		while(d[0].x!=0)
		{
			
			sum-=1;
			d[0].x-=1;
			if(d[1].x>sum/2)//&&d[0].x>sum/2)
			{
				d[1].x-=1;
				sum-=1;
				fout<<char(d[0].i+'A')<<""<<char(d[1].i+'A')<<" ";
			}
			else
			{
				fout<<char(d[0].i+'A')<<" ";
			}
			sort(d,d+n,comp);	
		}
		fout<<endl;
	}
return 0;
}
