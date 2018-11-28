#include <iostream>
#include <cstdio>

using namespace std;

int T;
char states[4][4]={{'1','i','j','k'},{'i','1','k','j'},{'j','k','1','i'},{'k','j','i','1'}};
int s[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};

int converter(char in)
{
	if(in=='1') 
		return 0;
	else if(in=='i') 
		return 1;
	else if(in=='j') 
		return 2;
	else if(in=='k') 
		return 3;
}

int main()
{
	freopen("inpdjikstra.txt","r",stdin);
	freopen("outputdjikstra.txt","w",stdout);
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		long long int L,X;
		cin>>L>>X;
		int str[10005];
		int result=0;
		int sign=1;
		int current=1;
		for(long long int j=0;j<L;j++)
		{
			char temp;
			cin>>temp;
			str[j]=converter(temp);
		}
		for(long long int j=0;j<L*X;j++)
		{
			sign=sign*s[result][str[j%L]];
			result=converter(states[result][str[j%L]]);
			if(result==current && sign==1)
			{ 
				current++;
				result=0;
			}
		}
		if(current==4 && result == 0 && sign== 1) 
			cout<<"Case #"<<i<<": YES"<<endl;
		else 
			cout<<"Case #"<<i<<": NO"<<endl;
	}
	return 0;
}
