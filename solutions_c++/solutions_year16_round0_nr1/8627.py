/*
5
0
1
2
11
1692

Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076
*/


#include<iostream>
#include<stdio.h>
using namespace std;
bool visited[11];
int SheepSleepCount(int N)
{
	int i=1;
	if(N<=0)
		return 0;
	while(1)
	{
		int newNum = N*i;
		i++;
		int org=newNum;
		while(newNum>0)
		{
			int digit = newNum%10;
			newNum=newNum/10;
			visited[digit] = true;
		}
		bool allvisited=true;
		for(int j=0;j<10;j++)
		{
			if(!visited[j] )
				allvisited=false;
		}
		if(allvisited)
			return org ;
		
	}
}
int main()
{
	int T;
	cin>>T;
	int N;
	for(int i=0;i<T;i++)
	{
		cin>>N;
		for(int j=0;j<10;j++)
		{
			visited[j]=false;
		}

		int ans = SheepSleepCount(N);
		if(ans==0)
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<"\n";
		else
			cout<<"Case #"<<i+1<<": "<<ans<<"\n";
	}
	
}