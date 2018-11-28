#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <utility>
#include <set>
#include <map>

using namespace std;

#define pb push_back
#define mp make_pair
#define F first
#define S seccond
#define For(i,n) for (int i = 0; i < n; i++)

int main()
{
    freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
    int t;
    scanf("%d\n", &t);
    For(q,t)
    {
            int n;
            scanf("%d\n", &n);
            string s1, s2;
            cin >> s1;
            cin >> s2;
            int ans = 0;
            int i = 0, j = 0;
            int a = 0, b = 0;
            s1 += "+";
            s2 += "+";
            bool x = true;
            while (true)
            {
                  if (s1[i] != s2[j])
                     {
                            x = false;
                            break;
                     }
                  if (s1[i] == '+')
                     break;
                  for (int p = i; i < s1.size() - 1; p++)
                  {
                      if (s1[p] != s1[p + 1])
                      {
                                a = p - i + 1;
                                i = p + 1;
                                break;
                      }
                  }
                  for (int p = j; j < s2.size() - 1; p++)
                      if (s2[p] != s2[p + 1])
                         {
                                b = p - j + 1;
                                j = p + 1;
                                break;
                         }
                  ans += abs(a - b);
            }
            cout << "Case #" << q + 1 << ": ";
            if (!x)
               cout << "Fegla Won" << endl;
            else cout << ans << endl;
    }
    return 0;
}
