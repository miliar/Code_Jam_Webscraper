#include<cstdio>
#include<iostream>
using namespace std;

bool isbetween(int i, int a, int b) {
  return i>=a && i<=b;
}

int main() {
  int TCn;
  int pal[10] = {1,4,9,121,484};
  scanf("%d", &TCn);

  for (int TC = 1; TC <= TCn; ++TC) {
    printf("Case #%d: ", TC);

    int a, b;
    scanf("%d%d", &a, &b);

    int count = 0;

    for (int i =0; i <5; ++i)
      if (isbetween(pal[i],a,b))
	++count;
    
    printf("%d\n",count);

  }

  return 0;
}
