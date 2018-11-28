#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include<fstream>
using namespace std;
const int maxn=11;
int t;
int vis[maxn];
bool judge(){
	int flag=0;
	for(int i=0;i<10;i++)
	{
		if(!vis[i]){
			flag=1; break;
		}
	}
	if(!flag)  return true;
	else return false;
}
void oper(long long n)
{
	long long m;
	do
	{
		m=n%10;
		vis[m]=1;
		n/=10;
	}while(n>0);
}
int main()
{	
	//freopen("a.in","r",stdin);
	//freopen("d.txt","w",stdout);
	long long n;
	cin>>t;
	for(int cas=1;cas<=t;cas++)
	{
		memset(vis,0,sizeof(vis));
		cin>>n;
		if(n==0) {
			cout<<"Case #"<<cas<<": INSOMNIA"<<endl;
			continue;
		}
		long long z;
		z=n;
		while(z)
		{
			oper(z);
			if(judge()) break;
			z+=n;
		}
		cout<<"Case #"<<cas<<": "<<z<<endl;
	}
    return 0;
}
