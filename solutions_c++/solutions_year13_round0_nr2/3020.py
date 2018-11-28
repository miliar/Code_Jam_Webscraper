#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

int main()
{
  freopen("B-large.in", "rt", stdin);
  freopen("B-large.out", "wt", stdout);

  int T;
  int N, M;
  int pat[100][100];

  cin>>T;
  
  for (int t=1; t<=T; t++)
  {
    printf("Case #%d: ", t);
   
    cin>>N>>M;
    int rowMax[100] = {0};
    int colMax[100] = {0};    
   
    //read pat 
    for (int i = 0; i < N; ++i)
    {
      for (int j = 0; j < M; ++j)
      {
        int h;
        cin>>h;
        pat[i][j] = h;

        //cout<<i<<j<<h<<endl;
        if (h > rowMax[i]) rowMax[i] = h;
        if (h > colMax[j]) colMax[j] = h;
      }
    }
    
    //check if every point is rowMax or colMax
    bool pass = true;
    for (int i = 0; i < N; ++i)
    {
      if(!pass) break;
      for (int j = 0; j < M; ++j)
      {
        //cout<<pat[i][j]<<rowMax[i]<<colMax[j]<<endl;

        if (pat[i][j] != rowMax[i] && pat[i][j] != colMax[j])
        {  
          pass = false;
          break;
        }
      }
    }

    if (pass) printf("YES\n");
    else printf("NO\n");

  }
}
