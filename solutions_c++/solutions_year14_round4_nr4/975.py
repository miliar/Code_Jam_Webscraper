#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <cmath>
#include <queue>
#include <algorithm>

using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;

ull count1 = 0;
int m_strings;
ll worst = 0;

ll tris[1 << 8];

int get_bits(int m)
{
  int c = 0;
  for (int i = 0; i < m_strings; ++i)
    if (m & (1 << i))
      ++c;

  return c;
}

void f4(int a1, int a2, int a3, int a4)
{
  int up = 1 << m_strings;
  for (int m1 = 1; m1 < up; ++m1)
  {
    if (get_bits(m1) != a1)
      continue;

    for (int m2 = 1; m2 < up; ++m2)
    {
      if ((m1 & m2) != 0)
        continue;

      if (get_bits(m2) != a2)
        continue;

      for (int m3 = 1; m3 < up; ++m3)
      {
        if ((m3 & (m2 | m1)) != 0)
          continue;

        if (get_bits(m3) != a3)
          continue;

        int m4 = (up - 1) & (~(m1 | m2 | m3));

        ll cur = tris[m1] + tris[m2] + tris[m3] + tris[m4];
        if (cur > worst)
        {
          worst = cur;
          count1 = 1;
        }
        else if (worst == cur)
        {
          ++count1;
        }

      }
    }
  }
}void f3(int a1, int a2, int a3)
{
  int up = 1 << m_strings;
  for (int m1 = 1; m1 < up; ++m1)
  {
    if (get_bits(m1) != a1)
      continue;

    for (int m2 = 1; m2 < up; ++m2)
    {
      if ((m1 & m2) != 0)
        continue;

      if (get_bits(m2) != a2)
        continue;

      

        int m3 = (up - 1) & (~(m1 | m2));

        ll cur = tris[m1] + tris[m2] + tris[m3];
        if (cur > worst)
        {
          worst = cur;
          count1 = 1;
        }
        else if (worst == cur)
        {
          ++count1;
        }

      
    }
  }
}
void f2(int a1, int a2)
{
  int up = 1 << m_strings;
  for (int m1 = 1; m1 < up; ++m1)
  {
    if (get_bits(m1) != a1)
      continue;

  

        int m2 = (up - 1) & (~(m1));

        ll cur = tris[m1] + tris[m2];
        if (cur > worst)
        {
          worst = cur;
          count1 = 1;
        }
        else if (worst == cur)
        {
          ++count1;
        }

  }
}
string S[10];

int main()
{
  freopen("D-small-attempt1.in", "r", stdin);
  freopen("D-result-small2.txt", "w", stdout);

  int c = 0;



  //cout << count1 << endl;

  int T;
  scanf("%d", &T);

  for (int i = 0; i < T; ++i)
  {
    int n;
    cin >> m_strings >> n;
    memset(tris, 0, sizeof(tris));

    for (int i = 0; i < m_strings; ++i)
      cin >> S[i];

    for (int i = 0; i < (1 << m_strings); ++i)
    {
      set<string> sss;

      for (int j = 0; j < m_strings; ++j)
      {
        if (i & (1 << j))
        {
          for (int k = 0; k < S[j].size(); ++k)
            sss.insert(S[j].substr(0, k + 1));
        }
      }

      tris[i] = sss.size() + 1;
    }

    count1 = 0;
    worst = 0;

    if (n == 4)

      for (int a1 = 1; a1 <= m_strings; ++a1)
        for (int a2 = 1; a2 <= m_strings; ++a2)
          for (int a3 = 1; a3 <= m_strings; ++a3)
            for (int a4 = 1; a4 <= m_strings; ++a4)
              if (a1 + a2 + a3 +a4 == m_strings)
                f4(a1,a2,a3,a4);

    if (n == 3)
      for (int a1 = 1; a1 <= m_strings; ++a1)
        for (int a2 = 1; a2 <= m_strings; ++a2)
          for (int a3 = 1; a3 <= m_strings; ++a3)
              if (a1 + a2 + a3 == m_strings)
                f3(a1,a2,a3);

    if (n == 2)
      for (int a1 = 1; a1 <= m_strings; ++a1)
        for (int a2 = 1; a2 <= m_strings; ++a2)
              if (a1 + a2 == m_strings)
                f2(a1,a2);

    if (n == 1)
    {
      worst = tris[(1 << m_strings) - 1];
      count1 = 1;
    }

    printf("Case #%d: %lld %lld", i + 1, worst,count1);



    printf("\n");
  }

  fclose(stdin);
  fclose(stdout);

  return 0;
}