#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define FORC(i,a,b) for(int i=a;i<=b;++i)
#define FORD(i,a,b) for(int i=a;i>b;--i)
#define ini(arr,val) memset(arr,val,sizeof(arr))
#define pii pair<int,int>
#define vi vector<int>
#define f first
#define s second
#define si set<int>
#define pb push_back
#define deb(d,a,b) for(d=a;d<b;++b)
#define p(val) printf("%d ",val)
#define pe(val) printf("%d\n",val)
#define qt queue<int>
#define size(arr) arr.size()
#define pc(s) printf("%c ",s)
#define pce(s) printf("%c\n",s);
#define ll  long long int
int main()
{
   int t;
   cin >> t;
   FOR(it,0,t)
   {
      int a[4][4],b[4][4];
      int n1,n2,ans = 0,count = 0;
      cin >> n1;
      FOR(i,0,4) FOR(j,0,4) cin >> a[i][j];
      cin >> n2;
      FOR(i,0,4) FOR(j,0,4) cin >> b[i][j]; //ei
      
      FOR(i,0,4)//p
         FOR(j,0,4)
            {
               if(a[n1-1][i] == b[n2-1][j]) 
               {
                  count++;
                  ans = a[n1-1][i];
               }
            }
      
      if(count == 1) printf("Case #%d: %d\n",it+1,ans);
      else if(count > 1) printf("Case #%d: Bad magician!\n",it+1);
      else if(!count) printf("Case #%d: Volunteer cheated!\n",it+1);
   }
}