#include<cstdio>
#include<cstring>
#include<string>

using namespace std;

int main()
{
  int t = 0;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    char str[1003];
    scanf("%s", str);
    int len = strlen(str);
    string out;
    for (int j = 0; j < len; j++) {
      if (out.length() == 0 || str[j] < out[0])
       out += str[j];
      else
       out.insert(out.begin(), str[j]);
    }
    printf("Case #%d: %s\n", i, out.c_str());
  }

  return 0;
}
