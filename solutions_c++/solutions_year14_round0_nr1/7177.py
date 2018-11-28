#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <deque>
#include <stack>
#include <algorithm>
#include <climits>
#include <numeric>
#include <utility>
#include <sstream>
#include <cstring>

#define FOR(i,a,n) for(int i=a;i<n;i++)
#define FORE(i,a,n) for(int i=a;i<=n;i++)
#define REV(i,a,n) for(int i=n-1;i>=a;i--)
#define REVE(i,a,n) for(int i=n;i>=a;i--)
#define println printf("\n")
#define sortv(v) sort(v.begin(),v.end())
#define printv(i,v) FOR(i,0,v.size()) {  cout<<v[i]<<" ";}
#define printarr(i,arr,n) for(int i=0;i<n;i++) {cout<<arr[i]<<" ";}
#define scani(a) scanf("%d",&a)
#define scanc(a) scanf("%c",&a)
#define scans(a) scanf("%s",a)
#define pb push_back
#define mp(a,b) make_pair(a,b)

typedef long int LD;
typedef long long LLD;
typedef unsigned long long LLU;

using namespace std;

int main()
{
    int a[5][5];
    int t,x,y;
    vector<int> temp;
    scani(t);
    FORE(i,1,t)
    {
              scani(x);
              FOR(i,0,4)
                        FOR(j,0,4)
                                  scani(a[i][j]);              
              temp.pb(a[x-1][0]);temp.pb(a[x-1][1]);temp.pb(a[x-1][2]);temp.pb(a[x-1][3]);
              scani(y);
              FOR(i,0,4)
                        FOR(j,0,4)
                                  scani(a[i][j]);
              int count=0;
              int val;
              FOR(i,0,4)
              {
                        if((find(temp.begin(),temp.end(),a[y-1][i]))!=temp.end())
                        {
                           count++;
                           val=a[y-1][i];
                        }
              }
              if(count==1)
                          printf("Case #%d: %d\n",i,val);
              else if(count>1)
                          printf("Case #%d: Bad magician!\n",i);
              else if(count==0)
                          printf("Case #%d: Volunteer cheated!\n",i);
              temp.clear();
    }
    fflush(stdin);
    getchar();
    return 0;
}
