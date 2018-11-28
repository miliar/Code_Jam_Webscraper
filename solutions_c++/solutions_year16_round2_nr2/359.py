#include<bits/stdc++.h>
#include<cstdlib>   
#define sf(x) scanf("%d",&x)
#define pf(x) printf("%d ",x)
#define sf2(x,y) scanf("%d %d",&x,&y)
#define pf2(x,y) printf("%d %d ",x,y)
#define sf3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define pf3(x,y,z) printf("%d %d %d ",x,y,z)
#define sfc(c) scanf(" %c",&c)
#define pfc(c) printf("%c",c)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define INF 2000000000
#define ENDL puts("")


using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef unsigned int uint;
typedef long double ld;



string s1,s2;


bool check(string &s, int num)
{
	for(int i=s.size()-1; i>=0; i--)
	{
		if(s[i]=='?')
		{
			num/=10;
			continue;
		}
		if(s[i]-'0'!=(num%10))
		{
			return false;
		}
		num/=10;
	}
	return true;
}


int main()
{
    
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);      
    /**/
	
	
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
    	cin>>s1>>s2;
    	int k=1;
    	for(int i=0; i<s1.size(); i++)
    	{
    		k*=10;
    	}
    	int res=INF;
    	int C=INF;
    	int J=INF;
    	for(int i=0; i<k; i++)
    	{
    		if(check(s1,i))
    		for(int j=0; j<k; j++)
    		{
    			if(check(s2,j))
    			{
    				if(abs(i-j)<res)
    				{
    					res=abs(i-j);
    					C=i;
    					J=j;
    				}
    			}
    		}
    	}
    	int buf1[10],buf2[10];
    	memset(buf1,0,sizeof(buf1));
    	memset(buf2,0,sizeof(buf2));
    	for(int i=0; i<5; i++)
    	{
    		buf1[i]=C%10;
    		buf2[i]=J%10;
    		C/=10;
    		J/=10;
    	}
    	printf("Case #%d: ",t);
    	for(int i=s1.size()-1; i>=0; i--)
    	{
    		printf("%d",buf1[i]);
    	}
    	printf(" ");
    	for(int i=s1.size()-1; i>=0; i--)
    	{
    		printf("%d",buf2[i]);
    	}
    	printf("\n");
    }
    
    
    
    return 0;
}











