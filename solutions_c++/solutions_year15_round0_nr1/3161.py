
#include <cstdio>
#include <algorithm>

using namespace std;

char s[2000];
int a[2000];

int main(void)
{    //freopen("input.txt", "r", stdin);
	 //freopen("output.txt", "w", stdout);

	int t;
     int tt = 1;
     scanf("%d", &t);
     
     while(t--)
     {    int n;
          
          scanf("%d %s", &n, s);
          n++;
          
          for(int i = 0; i < n; i++)
          {    a[i] = s[i] - '0';
          }
          
          int ans = 0;
          
          int have = a[0];
          for(int i = 1; i < n; i++)
          {    if(i > have)
               {    ans += (i - have);
                    have += (i - have);
               }
               have += a[i];
          }
          
          printf("Case #%d: %d\n", tt++, ans);
     }
     return 0;
}
