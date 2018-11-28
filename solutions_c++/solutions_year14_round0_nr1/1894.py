#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int testcase,A[17];


int main () {
  freopen("A-small-attempt0.in","r",stdin);
  freopen("a.out","w",stdout);
  scanf("%d",&testcase);
  for (int TC=1;TC<=testcase;++TC) {
    memset(A,0,sizeof(A));
    int tmp, num = -1, cnt = 0, row;
    scanf("%d",&row);
    for (int i=1;i<=4;++i)
      for (int j=1;j<=4;++j) {
        scanf("%d",&tmp);
        if(i == row) ++A[tmp];
      }
    scanf("%d",&row);
    for (int i=1;i<=4;++i)
      for (int j=1;j<=4;++j) {
        scanf("%d",&tmp);
        if(i == row) ++A[tmp];
      }
    for (int i=1;i<=16;++i)
      if (A[i] == 2) {
        ++cnt;
        num = i;
      }
    if (cnt == 1) printf("Case #%d: %d\n",TC,num);
    else if(cnt == 0) printf("Case #%d: Volunteer cheated!\n",TC);
    else printf("Case #%d: Bad magician!\n",TC);
  }
}
