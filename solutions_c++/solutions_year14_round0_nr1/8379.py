#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define SMALL
#define LARGE
int main() {

	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small-attempt0.out","wt",stdout);
	/*
#ifdef SMALL
	freopen("A-small.txt","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
  */
  int nt, ans1, ans2, c, r, result, value, i, j, len;
  int table1[4][4],table2[4][4];
  vector<int> answer;
  cin>>nt;
  len = nt;

  while(nt--)
  {
    c=0;
    cin>>ans1;
    for(i=0;i<4;i++)
    {
      for(j=0;j<4;j++)
      {
        cin>>table1[i][j];
      }
    }

    c=0;
    cin>>ans2;
    for(i=0;i<4;i++)
    {
      for(j=0;j<4;j++)
      {
        cin>>table2[i][j];
      }
    }

    result = 0;
    value = 0;

    for(i=0;i<4;i++)
    {
      for(j=0;j<4;j++)
      {
        if(table1[ans1-1][i]==table2[ans2-1][j])
        {
          result += 1;
          value = table1[ans1-1][i];
        }
      }
    }

    if(0 == result)
    {
      answer.push_back(0);
    }
    else if(1 == result)
    {
      answer.push_back(value);
    }
    else if(1 < result)
    {
      answer.push_back(-1);
    }
  }

	for(i=0;i<len;i++)
  {
    if(answer[i] == 0)
      cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
    else if(answer[i] == -1)
      cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
    else
      cout<<"Case #"<<i+1<<": "<<answer[i]<<endl;
  }

	return 0;
}
