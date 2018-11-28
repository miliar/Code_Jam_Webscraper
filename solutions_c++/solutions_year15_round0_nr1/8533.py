#include <cstdio>
using namespace std;

int main() {
 freopen("A-large.in", "r", stdin);
 freopen("out", "w", stdout);
  int t;
  scanf("%d",&t);

  for(int j=1;j<=t;j++){
        int n,counter=0,sum=0;
        char c[1001];
    scanf("%d",&n);
    int n_new=n;
    scanf("%s",c);

    for(int i=0;i<=n_new;i++){
        int newnum=0;
        int num=c[i]-48;

        if(sum<i)
            newnum=i-sum;
        sum+=newnum;
        counter+=newnum;
        sum+=num;

    }

    printf("Case #%d: %d\n",j,counter);
  }

  return 0;
}
