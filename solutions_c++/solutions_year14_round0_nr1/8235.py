#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <utility>
#include <algorithm>
#include <limits>
#include <time.h>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <vector>
#include <string>
#include <string.h>
#include <sstream>
#include <map>
#include <set>

#define FOR(i,a,b) for (int i=a; i<=b; i++)
#define FORD(i,a,b) for (int i=a; i>=b; i--)
#define p_b push_back
#define m_p make_pair
#define eps 1e-12
#define F first
#define S second
#define INF numeric_limits <int> :: max()
#define tr(Con,it) for(typeof(Con.begin()) it=Con.begin();it!=Con.end();it++)

using namespace std;    
int T;
int x,y,a[10][10],b[10][10],kol,ans;

int main()
{
 #ifndef ONLINE_JUDGE
 freopen("input.txt","rt",stdin);
 freopen("output.txt","wt",stdout);
 #endif 
 scanf("%d\n",&T);
 FOR(q,1,T)
  {
   kol=ans=0;

   scanf("%d\n",&x);
   FOR(i,1,4) 
    {
     FOR(j,1,4) scanf("%d",&a[i][j]);
     scanf("\n");
    }

   scanf("%d\n",&y);
   FOR(i,1,4) 
    {
     FOR(j,1,4) scanf("%d",&b[i][j]);
     scanf("\n");
    }


    FOR(i,1,4)
     {
      FOR(j,1,4)
      if (a[x][i]==b[y][j])
       {
        kol++;
        ans=a[x][i];
       }
     }

   printf("Case #%d: ",q);
   if (kol==0) printf("Volunteer cheated!\n"); else
   if (kol==1) printf("%d\n",ans); else printf("Bad magician!\n");
  }

 return 0;
}

