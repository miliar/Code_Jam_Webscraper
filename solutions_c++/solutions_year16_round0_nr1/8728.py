#include <bits/stdc++.h>

using namespace std;

int main()
{
  int t, a, b, cas = 0;
  scanf("%d", &t);
  bitset<10> saw;
  string num;
  while(t--)
  {
    scanf("%d", &a);
    printf("Case #%d: ", ++cas);
    if(a)
    {
      saw.reset();
      b = 0;
      while(!saw.all())
      {
        b += a;
        num = to_string(b);
        for(int i = 0; i < num.size(); ++i)
          saw[num[i]-'0'] = true;
      }
      printf("%d\n", b);
    }
    else
      puts("INSOMNIA");
  }
  return 0;
}
