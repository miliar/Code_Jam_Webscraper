#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
    int i, T;
    scanf("%d",&T);
    for(i=0;i<T;i++){
          vector<int> r;
          int j, k, a, b, A[4][4], B[4][4];
          scanf("%d",&a);
          a-=1;
          for(j=0;j<4;j++)
              for(k=0;k<4;k++)
                  scanf("%d",&A[j][k]);
          scanf("%d",&b);
          b-=1;
          for(j=0;j<4;j++)
              for(k=0;k<4;k++)
                  scanf("%d",&B[j][k]);
          for(j=0;j<4;j++)
              for(k=0;k<4;k++)
                   if(A[a][j]==B[b][k])
                       r.push_back(A[a][j]);
          if(r.empty())
              printf("Case #%d: Volunteer cheated!\n",i+1);
          else if(r.size()>1)
              printf("Case #%d: Bad magician!\n",i+1);
          else
              printf("Case #%d: %d\n",i+1,r.back());
    }
    return 0;
}