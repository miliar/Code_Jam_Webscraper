

/**
AUTHOR:Rahul Shah
LINK:
WEBSITE:Codechef
PROBLEM:
**/

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<cstring>
#include<stack>
#include<cstdlib>
using namespace std;
#define MOD 1000000007
#define ll long long
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		int n;
		cin>>n;
		string s1,s2;
		cin>>s1>>s2;
		int i=0,j=0;
		int l1=s1.length(),l2=s2.length();
		bool flag=true;
		int cnt=0;
		while(i<l1&&j<l2)
		{
			if(s1[i]==s2[j])
			{
				int tmp1=0,tmp2=0;
				while(i+1<l1&&s1[i+1]==s2[j])
				{
					i++;
					tmp1++;
				}
				while(j+1<l2&&s2[j+1]==s1[i])
				{
					j++;
					tmp2++;
				}
				cnt+=abs(tmp1-tmp2);
			}
			else
			{
				flag=false;
				break;
			}
			i++;j++;
		}
		if(!flag||i!=l1||j!=l2)
		{
			cout<<"Case #"<<tc<<": Fegla won\n";
		}
		else
		{
			cout<<"Case #"<<tc<<": "<<cnt<<"\n";
		}
	}
return 0;
}
