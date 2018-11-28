#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;

void main2()
{
  int N, X;
  scanf("%d%d", &N, &X);
  
  multiset<int> val;
  
  for (int i=0; i<N; i++)
  {
    int tmp;
    scanf("%d", &tmp);
    val.insert(tmp);
  }

  int res = 0;
  while (!val.empty())
  {
    res++;
    
    multiset<int>::iterator act = --val.end();
    int tmp = *act;
    val.erase(act);
    
    act = val.upper_bound(X - tmp);
    if (act != val.begin())
    {
      act--;
      //printf("(%d) ", *act);
    //if (act != val.begin())
      val.erase(act);
    }
  }
  
  printf("%d\n", res);
}

int main()
{
  int N;
  scanf("%d", &N);
  
  for (int i=0; i<N; i++)
  {
    printf("Case #%d: ", i+1);
    main2();
  }
}
