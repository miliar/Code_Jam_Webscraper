#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

typedef long long int64;

int main() {
  int T;
  int shyness_level;
  char  audience [1002];
  int people_mising;
  int sum_people;

  freopen ("A-large.in","r",stdin);
  freopen ("myfile2.txt","w",stdout);

  scanf ("%d", &T);

  for(int cases=1;cases<=T;cases++)
  {
    people_mising=0;
    sum_people=0;
    scanf("%d",&shyness_level);
    scanf("%s",audience);
    printf ("Case #%d: ",cases);

    for(int i = 0; i<= shyness_level; i++)
    {
       sum_people+=audience[i]-48;

       if(sum_people+people_mising<i+1)
       {
         people_mising+=(i+1)-(sum_people+people_mising);
       }
    }
    printf ("%d\n", people_mising);

  }


  fclose (stdout);
  fclose (stdin);

  return 0;
}
