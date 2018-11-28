#include<iostream>
#include<vector>
#include<stdio.h>
#include<algorithm>
#include<set>
#include<math.h>
#include<string.h>
#include<map>
#define all(c) c.begin(), c.end()
#define tr(container, it) for(typeof(container.begin())it=container.begin();it!=container.end();it++)
#define sz(a) int((a).size()) 
#define pb push_back
#define present(c,x) ((c).find(x)!=(c).end()) 
#define cpresent(c,x) (find(all(c),x)!=(c).end())
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef set<int> si;
typedef long long int lli;

int main()
{
	int t,n,m,i,j,k,flag=0,pcnt=0,mcnt=0;
	char str[105];
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		flag=0;
		cin>>str;
		int l=strlen(str);
		int ic=0;
		i=0;
		while(str[i]=='-')
		{
			flag=1;
			i++;	
		}
		if(flag==1)
			ic++;
		for(;i<l;i++)
		{
			while(str[i]=='+')
				i++;
			if(i==l)
				break;
			ic++;
			while(str[i]=='-')
				i++;
			ic++;
		}
		//if(str[l-1]=='+')
			//ic++;
		printf("Case #%d: %d\n",k,ic);
	}
}

