#include <bits/stdc++.h>
using namespace std;
#ifndef M
#define M 1000000007
#endif
typedef pair<int,int>pp;
typedef std::vector<pp> vpp;
typedef long long ll;
#ifndef pb
#define pb push_back 
#endif 
int min(int x,int y){return(x<y)?x:y;}
int max(int x,int y){return(x>y)?x:y;}
int main(int argc, char const *argv[])
{
	int t;
	scanf("%d",&t);
	string x[10]={"FOUR","EIGHT","ZERO","TWO","SIX","FIVE","NINE","SEVEN", "ONE","THREE" };
	int blah[10]={4,8,0,2,6,5,9,7,1,3};
	std::vector<int> vv;
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		string s,h,v;
		cin>>s;
		v.assign(s);
		for(int i=0;i<10;i++)
		{
			int flag=0;
			while(flag==0)
			{
				for(int j=0;j<x[i].size();j++)
					if(s.find(x[i][j])==-1)
					{
						flag=1;
						s.assign(v);
						break;
					}
					else
						s[s.find(x[i][j])]='0';
				if(flag==0)
				{
					vv.pb(blah[i]);
					v.assign(s);
				}
			}
		}
		sort(vv.begin(),vv.end());
		for(int j=0;j<vv.size();j++)
			printf("%d",vv[j]);
		printf("\n");
		vv.clear();
	}
	return 0;
}