
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>

using namespace std;

double c,f,x;

    double sumx[10000000];
double hasWon() {
double addition=2.0;

    double sum1=0.0,sum2=0.0;

    long long int i=1;
    int k;
    sum1=x/addition;
    sumx[0]=c/addition;

    while(1)
    {
        //addition=2.0;
        addition+=f;

        sum2=sumx[i-1]+x/addition;
  /*      k=i;
        while(k>0)
        {
            sum2+=c/addition;
            addition+=f;
            k--;
        }
*/
        sumx[i]=c/addition+sumx[i-1];

      //  sum2+=x/addition;

           // printf("%lf\n",sum2);
           // printf("%lld\n",i);
        if(sum2>sum1)
            break;
        sum1=sum2;
        sum2=0.0;
        i++;
    }
// printf("%lld\n",i);
return sum1;
}

int main() {
    freopen("A-small.in", "r", stdin);
    freopen("small.txt", "w", stdout);
    int T;
    double ans;

    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {

        scanf("%lf", &c);
        scanf("%lf", &f);
        scanf("%lf", &x);
        //printf("%0.7lf %0.7lf %0.7lf\n", c,f,x);
        ans=hasWon();

        printf("Case #%d: %0.7lf\n", t, ans);
    }

	return 0;
}
