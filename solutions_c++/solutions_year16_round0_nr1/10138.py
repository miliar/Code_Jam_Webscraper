#include <cstdio>
#include <set>

int main() {

  int t, count = 1;

  scanf("%d", &t);
  while (t--) {
    int n;
    scanf("%d", &n);

    int a_d = 0b1111111111;
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n", count++);
    } else {
      int v;
      for (int i = 1; ;i++) {
        v = i * n;
        int m_p = 1;
        while (m_p * 10 <= v) m_p *= 10;
        int rest = v;
        for (; m_p > 0; m_p /= 10) {
          int d = rest / m_p;
          rest %= m_p;
          int d_b = 1 << d;
          a_d &= ~d_b;
          if (a_d == 0) {
            goto end_case;
          }

        }

      }

    end_case:
      printf("Case #%d: %d\n", count++, v);
    }
  }

  return 0;
}
