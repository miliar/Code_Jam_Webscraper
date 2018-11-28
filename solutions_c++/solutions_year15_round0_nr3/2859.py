#include<iostream>
#include<string>
#define sz (int)1e4+1
using namespace std;
char arr[sz][sz];
int sg[sz][sz];
string s;
int matrix[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};
char values[4][4]={{'1','i','j','k'},{'i','1','k','j'},{'j','k','1','i'},{'k','j','i','1'}};
void precomp(int n)
{
	char ans;
	int sign;
	for(int i=0;i<n;i++)
	{
		arr[i][i]=s[i];
		sg[i][i]=1;
	}
	for(int l=2;l<=n;l++)
	{
		for(int i=0;i<=n-l;i++)
		{
			int j=i+l-1;
			sign=sg[i][j-1];
			ans=arr[i][j-1];
			char temp=s[j];
			int a,b;
			switch(ans)
			{
				case '1':a=0;
					break;
				case 'i':a=1;
					break;
				case 'j':a=2;
					break;
				case 'k':a=3;
					break;
			}
			switch(temp)
			{
				case '1':b=0;
					break;
				case 'i':b=1;
					break;
				case 'j':b=2;
					break;
				case 'k':b=3;
					break;
			}
			ans=values[a][b];
			sign*=matrix[a][b];
			arr[i][j]=ans;
			sg[i][j]=sign;
		}
	}	
}
void solution()
{
	
int n;
int xx;
cin>>n>>xx;
string str;
cin>>str;
 s="";
for(int i=1;i<=xx;i++)
{
	s+=str;
}
if(s.length()<3)
{cout<<"NO";
return ;
}
int x=s.length();
precomp(x);
int flag=0;
for(int i=0;i<x-2;i++)
{
if(arr[0][i]=='i')
	for(int j=i+1;j<x-1;j++)
	{
		if(arr[i+1][j]!='j')
		continue;
		sign=sign*sg[0][i]*sg[i+1][j]*sg[j+1][x-1];
		if(arr[j+1][x-1]=='k' && sign==1)
		{
			cout<<"YES";
			return;
		}
	}
}
cout<<"NO";
return ;
}
int main()
{
	int test;
	cin>>test;
	for(int i=1;i<=test;i++)
	{
		cout<<"case #"<<i<<": ";
		solution();
		cout<<endl;
	}
	return 0;
}
