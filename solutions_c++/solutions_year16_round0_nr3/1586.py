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
typedef unsigned int uint;
typedef long double ld;


string toStr(int n)
{
	string res;
	while(n)
	{
		res.pb((n&1)+'0');
		n>>=1;
	}
	reverse(res.begin(),res.end());
	return res;
}

int main()
{
    
    //freopen("input","r",stdin);
    freopen("out.txt","w",stdout);      
    /**/
    
    int J=500;
    int N=32;
    cout<<"Case #1:\n";
    
    int m=3;
    for(int t=0; t<J; t++)
    {
    	string tmp=toStr(m);
    	string a=tmp+string(N-2*(int)tmp.size(),'0')+tmp;
    	cout<<a<<' ';
    	for(int i=2; i<=10; i++)
    	{
    		int qwe=m;
    		ll p=1;
    		ll res=0;
    		while(qwe)
    		{
    			if(qwe&1)
    			{
    				res+=p;
    			}
    			qwe>>=1;
    			p*=i;
    		}
    		cout<<res;
    		if(i==10) cout<<'\n';
    		else cout<<' ';
    	}
    	m+=2;
    }
    
    
    return 0;

}






















