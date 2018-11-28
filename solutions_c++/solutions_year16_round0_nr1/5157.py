#include<iostream>
#include<vector>
using namespace std;

int destruct(int N,int *visited)
{
	
	int temp=N;
	while(temp!=0)
	{
		int a=temp%10;
		visited[a]=1;
		temp=temp/10;
	}
	for(int i=0;i<10;i++)
	if(visited[i]==0)return 0;
	
	return 1;
}
int main()
{	int N;
	int T;
	cin>>T;
	int count=0;
	while(T--)
	{
		cin>>N;
		if(N==0){cout<<"Case #"<<++count<<": INSOMNIA"<<endl;continue;}
		int visited[10]={0};
		int stop=0;
		int m=N;
		
		while(1)
		{
			stop=destruct(m,visited);
			if(!stop)m+=N;
			else {cout<<"Case #"<<++count<<": "<<m<<endl;break;}
		}
	}
	return 0;
}
