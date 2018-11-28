#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int a[200];
int T=0;
int num[10];
int count=0;
int k=0;
int case0=0;

void clean()
{
	for (int i=0; i<=9; i++)
	{
		num[i]=0;
	}
}
void dem(int i)
{
	if(count>=1000)
	{
		cout<<"Case #"<<case0<<": "<<"INSOMNIA"<<endl;
		return;
	}
	char mark[12];
	sprintf(mark, "%d", i);
	int y=strlen(mark);
	for (int i=1; i<=y; i++)
	{
		int ar=mark[i-1]-'0';
		num[ar]=1;
	}
	int key=1;
	for (int i=0; i<=9; i++)
	{
		if (num[i]!=1)
			key=0;
	}
	if(key==0) {count++; dem(i+k);}
		else 
		{ 
			cout<<"Case #"<<case0<<": "<<i<<endl; 
			return;
		}
	
}
int main()
{
	freopen("aaa.in", "r", stdin);
	freopen("output.out", "w", stdout);
	cin>>T;
	for (int i=1; i<=T; i++)
	{
		cin>>a[i];
	}
	for (int i=1; i<=T; i++)
	{
		case0++;
		k=a[i];
		count=0;
		dem(a[i]);
		clean();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
} 
