#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>

using namespace std;

#define MAX_N 101

char str[MAX_N][MAX_N];
int ind[MAX_N];
int counter[MAX_N];

int main()
{
  int t;
  int n;
  scanf("%d",&t);
  for (int k=0; k<t; k++)
  {
    scanf("%d\n",&n);
    for (int i=0; i<n; i++)
      scanf("%s\n", str[i]);
    for (int i=0; i<n; i++)
      ind[i] = 0;
    bool impossible, finished;
    int costo = 0;
    //for (int i=0; i<n; i++)
      //printf("%s\n",str[i]);
    while (true) {
      finished = true;
      for (int i=0; i<n; i++)
        if (strlen(str[i]) != ind[i])
        {
          finished = false;
          break;
        }
      if (finished)
      {
        //printf("finito!\n");
        break;
      }
      char t = str[0][ind[0]];
      //printf("esamino lettera %c\n",t);
      impossible = false;
      for (int i=1; i<n; i++)
        if (str[i][ind[i]] != t)
        {
          impossible = true;
          break;
        }
      if (impossible)
      {
        //printf("impossibile!\n");
        break;
      }
      int sum = 0;
      for (int i=0; i<n; i++)
      {
        int prev = ind[i];
        while (str[i][ind[i]] == t)
          ind[i]++;
        sum += ind[i] - prev;
        counter[i] = ind[i] - prev;
        //printf("stringa %d ne ha %d\n",i,counter[i]);
      }
      //printf("somma %d\n",sum);
      sum = round( (double)sum / (double)n);
      //printf("convergo a %d\n",sum);
      for (int i=0; i<n; i++)
      {
        costo += abs(counter[i]-sum);
        //printf("stringa %d costa %d\n",i,abs(counter[i]-sum));
      }
    }
    if (impossible)
      printf("Case #%d: Fegla Won\n",k+1);
    else
      printf("Case #%d: %d\n",k+1,costo);
  }
  return 0;
}
