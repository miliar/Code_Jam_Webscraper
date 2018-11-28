#include <iostream>
#include <cstdio>
#include <cstdlib>

int main() {
  freopen("in.in", "r", stdin);
  freopen("out.txt", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
    int a,total=0,count1=0;
    char aud[10000];
    scanf("%d",&a);
    scanf("%s",aud);
    total=0,count1=0;
    for(int i=0;i<=a;i++)
    {
        total+=aud[i]-48;

        if(i>=total)
        {
            count1++;
            total++;
        }
    }
    printf("%d\n",count1);
  }
    return 0;
}
