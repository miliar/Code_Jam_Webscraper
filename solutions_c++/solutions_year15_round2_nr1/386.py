#include <cstdio>
#include <queue>
using namespace std;

int inverse(int a)
{
  int res = 0;
  while (a > 0)
  {
    res = res * 10 + a % 10;
    a /= 10;
  }
  return res;
}

const int N = 1000000;
const int INFINI = 1000000000;
int dist[N+1];

int main()
{
  for (int i=0; i<=N; i++)
    dist[i] = INFINI;
  
  dist[1] = 1;
  queue<int> encours;
  encours.push(1);
  while (!encours.empty())
  {
    int act = encours.front();
    encours.pop();
    if (act+1 <= N && dist[act+1] == INFINI)
    {
      dist[act+1] = dist[act]+1;
      encours.push(act+1);
    }
    if (inverse(act) <= N && dist[inverse(act)] == INFINI)
    {
      dist[inverse(act)] = dist[act]+1;
      encours.push(inverse(act));
    }
  }
  
  int T;
  scanf("%d", &T);
  for (int i=0; i<T; i++)
  {
    int a;
    scanf("%d", &a);
    printf("Case #%d: %d\n", i+1, dist[a]);
  }
}
