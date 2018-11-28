#include <iostream>
#include <stdio.h>

using namespace std;

char ch[2000];

int main() {
  int N;
  scanf("%d", &N);

  for (int n=0; n<N; n++) {
    int SMAX;
    scanf("%d", &SMAX);
    scanf("%s", ch);

    int sum =0;
    int help =0;

    int len = strlen(ch);

    for (int k=0; k<len; k++) {
      int num =(ch[k])-'0';

      if (num == 0) continue;

      if (k>sum) {
        help += k-sum;
        sum += help;
      }

      sum+= num;
    }

    cout <<"Case #"<<(n+1)<<": "<<help<<endl;
  }

}
