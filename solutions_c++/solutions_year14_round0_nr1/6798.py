#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<queue>
#include<stack>
#include<deque>
#include<map>
#include<set>
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define UP upper_bound
#define LB lower_bound
#define LL long long 
#define Pi 3.14159265358
#define si size()
#define en end()
#define be begin()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ii set<int>::iterator i
#define is set<string>::iterator i
using namespace std;
int fix[17];
int a[5][5], b[5][5];
int n, m, k, x, i, j, t, r, l;
main(){
       freopen("A.in","r",stdin);
       freopen("A.out","w",stdout);
       cin>>t;
       for(x=1;x<=t;x++)
        {
         m=0;
         memset(fix,0,sizeof(fix));
         scanf("%d",&r);
         for(i=1;i<=4;i++)
           for(j=1;j<=4;j++)
             scanf("%d",&a[i][j]);
         scanf("%d",&l);
         for(i=1;i<=4;i++)
           for(j=1;j<=4;j++)
             scanf("%d",&b[i][j]);
         for(i=1;i<=4;i++)
           fix[a[r][i]]=1;
         for(i=1;i<=4;i++)
           if(fix[b[l][i]])
            { k=b[l][i]; m++; }
         if(!m)cout<<"Case #"<<x<<": Volunteer cheated!\n";else
         if(m==1)cout<<"Case #"<<x<<": "<<k<<endl;
         else cout<<"Case #"<<x<<": Bad magician!\n";
        }
       //system("pause");
       }
