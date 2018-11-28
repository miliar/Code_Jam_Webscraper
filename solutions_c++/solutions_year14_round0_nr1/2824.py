#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <string.h>
using namespace std;

// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fillarr(a,v)                memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair

vector<int> solve(vector< pair<int, vector<int> > >& chests, queue<int>& keys)
{

}

int main() {
   int t;
   int va[4][4];
   int vb[4][4];
   s(t);
   
   forall(k,1,t+1)
   {
   int a,b,x;
   s(a);
   forall(i,0,4)
      forall(j, 0, 4)
   {
      s(x);
      va[i][j] = x;
   }
   s(b);
   forall(i,0,4)
      forall(j,0,4)
   {
      s(x);
      vb[i][j] = x;
   }
   int num, c = 0;
   a--;
   b--;
   forall(i,0,4)
      forall(j,0,4)
      {
      if(va[a][i] == vb[b][j])
         {
            c++;
            num = va[a][i];
         }
      }
   cout<<"Case #"<<k<<":"<<" ";
   if(c > 1)
      cout<<"Bad magician!"<<"\n";
   else
   if(c == 0)
      cout<<"Volunteer cheated!"<<"\n";
   else
      cout<<num<<"\n"; 
   }
    return 0;
}
