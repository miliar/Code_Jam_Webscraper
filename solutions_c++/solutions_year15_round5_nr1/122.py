#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

const int MAXI = 1000000;

int S[MAXI];
int M[MAXI];
pair<int, int> ordre[MAXI];
vector<int> F[MAXI];

int act;
int result;

int status[MAXI];

const int DEHORS = -1;
const int DEDANS = 1;
const int AJOUTER = 0;

void add(int i)
{
  if (i == 0 || status[M[i]] == DEDANS)
  {
    act++;
    status[i] = DEDANS;
    for (int j=0; j<(int)F[i].size(); j++)
    if (status[F[i][j]] == AJOUTER)
      add(F[i][j]);
  }
  else
  {
    status[i] = AJOUTER;
  }
}

void remove(int i)
{
  if (status[i] == DEDANS)
  {
    act--;
    for (int j=0; j<(int)F[i].size(); j++)
      remove(F[i][j]);
  }
  status[i] = DEHORS;
}

void main2()
{
  int N, D;
  scanf("%d%d", &N, &D);
  
  int S0, AS, CS, RS;
  scanf("%d%d%d%d", &S0, &AS, &CS, &RS);
  
  int M0, AM, CM, RM;
  scanf("%d%d%d%d", &M0, &AM, &CM, &RM);
  
  M[0] = M0;
  S[0] = S0;
  ordre[0] = make_pair(S0, 0);
  for (int i=1; i<N; i++)
  {
    S[i] = (S[i-1] * AS + CS) % RS;
    M[i] = (M[i-1] * AM + CM) % RM;
    ordre[i] = make_pair(S[i], i);
  }
  
  for (int i=1; i<N; i++)
    F[i].clear();
  
  for (int i=1; i<N; i++)
  {
    M[i] %= i;
    F[M[i]].push_back(i);
  }
  
  sort(ordre, ordre + N);
  
  for (int i=0; i<N; i++)
    status[i] = DEHORS;
  
  result = 0;
  act = 0;
  
  int i = 0;
  int j = 0;
  while (i < N)
  {
    while (j < N && ordre[j].first - ordre[i].first <= D)
    {
      add(ordre[j].second);
      j++;
    }
    
    result = max(result, act);
    
    remove(ordre[i].second);
    i++;
  }
  
  printf("%d\n", result);
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int i=1; i<=T; i++)
  {
    printf("Case #%d: ", i);
    main2();
  }
}
