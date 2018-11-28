#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define lim 1000
#define f first
#define s second
#define lli long long int
#define mp(x,y) make_pair(x,y)
#define pii pair<string,int>
#define vii vector<int>
#define vvi vector<pii>
#define pb push_back
#define sc(x) scanf("%d",&x)
#define ms(a,y) memset(a,y,sizeof(a))
#define all(x) x.begin(),x.end()
#define pi 3.14159
string str;
queue<pii > pq;
unordered_map<string,int> mpk;
bool verify(string sr)
{
      bool f=false;
	  int i;
      for(i=0;i<sr.size();++i)
      {
        if(sr[i]=='-')
        {
           f=true;
           break;
        }
      }
      if(f)
      {
          return false;
      }
      else
      {
          return true;
      }
}

int bfs()
{
	if(verify(str))
    {
       return 0;
    }
  	int i,j;
  	mpk[str]=1;
	pq.push(mp(str,0));
	  while(!pq.empty())
	  {
	      pii y=pq.front();
	      string a=y.f;
	      pq.pop();
	      for(i=0;i<a.size();++i)
	      {
	         string z=a;
	         reverse(z.begin(),z.begin()+i+1);
	         for(j=0;j<=i;++j)
	         {
	                if(z[j]=='-')
	                {
	                    z[j]='+';
	                }
	                else
	                {
	                    z[j]='-';
	                }
	         }
	         if(!mpk[z])
	         {
	            if(!verify(z))
	            {
	               mpk[z]=1;
	               pq.push(mp(z,y.s+1));        
	            }
	            else
	            {
	               return y.s+1;
	            }
	         }
	      }
	  }
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i=0;
	sc(t);
	while(t--)
	{
		cin>>str;
		int r=bfs();
		mpk.clear();
		printf("Case #%d: %d\n",++i,r);
		while(!pq.empty())
		pq.pop();
	}
 	return 0;
}

