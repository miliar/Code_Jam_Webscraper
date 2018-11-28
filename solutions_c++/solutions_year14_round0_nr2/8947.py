#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)

int main()
{
    freopen ("B-large.in","r",stdin);
    freopen ("output.out","w",stdout);
    
    int T,k=0;
    
    scanf("%d",&T);
    
    while(T--)
    {
		k++;
		
		double C,F,X,I=2,ret=0;
		scanf("%lf %lf %lf",&C,&F,&X);
		
		while(1)
		{
			if(X/I < C/I + X/(I+F))break;
			
			ret += C/I;
			I+=F;
		}
		
		ret += X/I;
		
		printf("Case #%d: %.7lf\n",k,ret);
	}
    
    
}


































