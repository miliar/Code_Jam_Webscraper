#include <bits/stdc++.h>
using namespace std;
//for cin with white space cin.getline(var,sizeof(var)); with  char var[100];
#define lli long long int
#define pb push_back
#define mp make_pair
#define sd(a) scanf("%lld",&a)
#define pd(a) printf("%lld\n",a)
#define F first
#define S second
// string s= to_string(int ); int to str
//***dont forget to clear the vector using v.clear();***
#define setl set<long long int>
#define sets set<string>
#define msetl multiset<long long int>
#define msets multiset<string>
#define vll vector<lli>
#define vstr vector<string>
#define pii pair<int , int>
#define SZ(x) (int)x.size()
#define v.all (v.begin(),v.end())

int main()
{
    lli t,x,y,n,k,m,ans;

   sd(t);
   for(int i=1;i<=t;i++)
  {
      bool a[10]={0};
	ans=0;
	sd(n);
	if(n==0){
        cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        continue;
	}
	m=0;
	x=1;
	while(m!=10){
        y=x*n;
        x++;
        ans=y;
        while(y>0)
        {
                int b=y%10;
                y=y/10;
                if(a[b]==0)
                {
                    a[b]=1;
                    m++;
                }
        }
	}
	printf("Case #%d: %lld\n",i,ans);

  }
    return 0;

}
