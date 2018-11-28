#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#define LL long long
#define MP make_pair
#define PB push_back
#define ff first
#define ss second
#define DEBUG(x) cerr<<#x<<" "<<(x)<<endl;

using namespace std;
int zlicz[20];
int main()
{
  int t, x, y;
  scanf("%d", &t);
  for(int z=1; z<=t; z++)
  {
    printf("Case #%d: ", z);
    scanf("%d", &x);
    for(int i=1; i<=16; i++)zlicz[i] = 0;
    vector<int>ans;
    ans.clear();
    int p;
    for(int i=1; i<=4; i++)
    {
      for(int j=1; j<=4; j++)
      {
	scanf("%d", &p);
	if(i == x)zlicz[p]++;
      }
    }
    scanf("%d", &y);
    for(int i=1; i<=4; i++)
    {
      for(int j=1; j<=4; j++)
      {
	scanf("%d", &p);
	if(i == y && zlicz[p])
	  ans.PB(p);
      }
    }
    if(ans.size() == 0)
      printf("Volunteer cheated!\n");
    if(ans.size() == 1)
      printf("%d\n", ans[0]);
    if(ans.size() > 1)
      printf("Bad magician!\n");
  }
  return 0;
}