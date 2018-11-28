/*A*/
#include<cstdio>
#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int vis[10];
int sum=0;

void check(int n)
{
	while(n>0)
	{
		int temp=n%10;
		if(vis[temp]==0)
		{
			sum++;
			vis[temp]=1;
		}
		n/=10;
	}
}
int main()
{
	ofstream outfile;
	outfile.open("A.txt");
	int T,ca=1;
	int N;
	scanf("%d",&T);
	while(T--)
	{
		memset(vis,0,sizeof(vis));
		sum=0;
		scanf("%d",&N);
		int flag=0;
		int temp;
		for(int i=1;;i++)
		{
			temp=i*N;
			check(temp);
			if(sum==10)
			{
				flag=1;
				break;
			}
			if(i==10000)    break;
		}
		if(flag==1)
		    printf("Case #%d: %d\n",ca++,temp);
		    //outfile<<"Case #"<<ca++<<": "<<temp<<endl;
		else
		    printf("Case #%d: INSOMNIA\n",ca++);
		    //outfile<<"Case #"<<ca++<<": "<<"INSOMNIA"<<endl;
	}
	outfile.close();
	return 0;
}
