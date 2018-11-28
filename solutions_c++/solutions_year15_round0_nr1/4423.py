#include <cstdio>

int main(int argc, const char* argv[])
{
  size_t T;
  scanf("%ld", &T);
  for (size_t t = 0; t < T; ++t) {
    int s_max;
    scanf("%d ", &s_max);
    long extra = 0;
    long standing = 0;
    for (size_t i = 0; i < s_max + 1; ++i) {
      char c;
      scanf("%c", &c);
      if (standing < i) {
        extra += i - standing;
        standing = i;
      }
      standing += c - '0';
    }
    printf("Case #%ld: %ld\n", t + 1, extra);
  }
  return 0;
}
