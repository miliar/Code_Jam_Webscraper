#include<iostream>
#include<cstdio>
#include<string>
#include<cstdlib>
#include<map>
#include<vector>
#include<set>
#include<list>

using namespace std;

typedef long long ll;
typedef double db;

#define pii pair<int,int>
#define F first
#define S second



int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	
	scanf("%d",&t);
	
	for(int k=1;k<=t;k++){
		int n,i,j,ans=0,count=0;
		char s[10005];

		scanf("%d%s",&n,s);

		for(i=0;i<n+1;i++){
			if(s[i]!='0'){
				if(count<i){
					ans=ans+(i-count);
					count=count+s[i]-48+(i-count);
				}
				else count=count+s[i]-48;
			}
		}
		
		printf("Case #%d: %d\n",k,ans);
	}
	
	return 0;
}