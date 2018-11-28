/* user :codelord
    contest : codejam2015 qualification
    problem:  third
    
	date: 11-4-2015
*/
 
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <string>
#include <cassert>
 
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
 
#define forup(i,a,b) for(int i=a; i<b; ++i)
#define fordn(i,a,b) for(int i=a; i>b; --i)
#define rep(i,a) for(int i=0; i<a; ++i)
 
#define dforup(i,a,b) for(i=a; i<b; ++i)
#define dfordn(i,a,b) for(i=a; i>b; --i)
#define drep(i,a) for(i=0; i<a; ++i)
 
#define slenn(s,n) for(n=0; s[n]!=13 and s[n]!=0; ++n);s[n]=0
 
#define gi(x) scanf("%d",&x)
#define gl(x) scanf("%lld",&x)
#define gd(x) scanf("%lf",&x)
#define gs(x) scanf("%s",x)
 
#define pis(x) printf("%d ",x)
#define pin(x) printf("%d\n",x)
#define pls(x) printf("%lld ",x)
#define pln(x) printf("%lld\n",x)
#define pds(x) printf("%.12f ",x)
#define pdn(x) printf("%.12f\n",x)
#define pnl() printf("\n")
 
#define fs first
#define sc second
#define ll long long
#define pb push_back
#define limit  100004
 
int mat[5][5]={ {0,0,0,0,0},
				{0,1,2,3,4},
				{0,2,-1,4,-3},
				{0,3,-4,-1,2},
				{0,4,3,-2,-1}};

int main()
{
	int t;
	gi(t);
	int L,X;
	int ans;
	char s[20000];
	char p[20000];
//	rep(i,5)
//	{
//		rep(j,5)
//			cout<<mat[i][j]<<" ";
//		cout<<endl;
//		
//	}
	
	for(int itr=1;itr<=t;itr++)
	{
		p[0]='\0';
		gi(L);
		gi(X);
		scanf("%s",s);
		int m=0;
		int total = L*X;
		for(int j=0;j<X;j++)
		{	strcat(p,s);
		}
		//printf("%s\n",p);
		int ans=1;
		int isneg = 0;
		int isexisti=0;
		int isexistk=0;
		for(int i=0;i<total;i++)
		{	
			if(p[i]=='i')
			{
				//cout<<ans<<" i:";	
				if(isneg)
					ans = -mat[-ans][2];
				else
					ans = mat[ans][2];
				//cout<<ans<<endl;	
			}
			else if(p[i]=='j')
			{	//cout<<ans<<" j:";
				if(isneg)
					ans = -mat[-ans][3];
				else
					ans = mat[ans][3];
			//	cout<<ans<<endl;
			}
			else
			{	//cout<<ans<<" k:";
				if(isneg)
					ans = -mat[-ans][4];
				else
					ans = mat[ans][4];
			//	cout<<ans<<endl;
			}
			if(ans<0)
			 	isneg=1;
			else
				isneg=0;
			if(ans==2)
				isexisti=1;
			if(ans==4&&isexisti==1)
				isexistk=1;	
		}
		
		if(ans==-1&&isexisti==1&&isexistk==1)
			{printf("Case #%d: YES\n",itr);
			}
			else
			printf("Case #%d: NO\n",itr);
	}

} 






