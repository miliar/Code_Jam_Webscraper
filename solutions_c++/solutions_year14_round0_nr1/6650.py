#include<iostream>
#include<cstring>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#define mp make_pair
#define pb push_back
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define F first
#define Se second
#define ll long long
#define pp pair<int,int>
#define INF 2000000000
using namespace std;
int T,t,i,j,A,B,f[20];
int a[5][5],b[5][5];
vector<int> ans;

main()
{freopen("A-small-attempt0.in","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d",&T);
 for(t=1;t<=T;t++){
     scanf("%d",&A);
     for(i=1;i<=4;i++)
      for(j=1;j<=4;j++)
      scanf("%d",&a[i][j]);
     
     scanf("%d",&B);
     for(i=1;i<=4;i++)
      for(j=1;j<=4;j++)
      scanf("%d",&b[i][j]);
      
     for(i=1;i<=16;i++)f[i]=0;
     
     ans.clear();
     for(i=1;i<=4;i++)f[a[A][i]]++;     
     for(i=1;i<=4;i++)
       if(f[b[B][i]])ans.pb(b[B][i]);
     cout<<"Case #"<<t<<": ";
     if(!(int)ans.size())cout<<"Volunteer cheated!"<<endl;else
     if((int)ans.size()>1)cout<<"Bad magician!"<<endl;else     
        cout<<ans[0]<<endl;
    }
}
