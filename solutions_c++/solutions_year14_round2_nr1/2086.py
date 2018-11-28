#include<cstdio>
#include<cstring>
#define MAX(A, B) (A > B ? A : B)
#define ABS(A) (A >= 0 ? A : -A)

using namespace std;

char f[100][100];

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    int cases;
    scanf("%d", &cases);
    
    for(int currentCase = 1; currentCase <= cases; currentCase++)
    {
            int n;
            scanf("%d", &n);
            if (n != 2)
            {
                  printf("bad\n");
                  continue;
            }
            
            char s1[100], s2[100];
            scanf("%s", s1);
            scanf("%s", s2);
            
            memset(f, 0, sizeof(char) * 100 * 100);
            int i, j;
            for(i = 0; s1[i]; i++)
            {
                    for(j = 0; s2[j]; j++)
                    {
                        if(s1[i] == s2[j])
                        {
                                 if(i > 0 && j > 0 && f[i - 1][j - 1])
                                 {
                                      f[i][j] = f[i - 1][j - 1] + 1;
                                 }
                                 else if(i == 0 && j == 0)
                                 {
                                      f[i][j] = 1;
                                 }
                        }
                        if(i > 0 && s1[i] == s1[i - 1])
                        {
                             f[i][j] = MAX(f[i][j], f[i - 1][j]);
                        }
                        if(j > 0 && s2[j] == s2[j - 1])
                        {
                             f[i][j] = MAX(f[i][j], f[i][j - 1]);
                        }
                    }
            }
            /*
            for(int p = 0; p < i; p++)
            {
                    for(int q = 0; q < j; q++)
                    {
                            printf("%d", f[p][q]);
                    }
                    printf("\n");
            }
            printf("\n");*/
            
            printf("Case #%d: ", currentCase);
            if(f[i - 1][j - 1])
            {
                       int d1 = f[i - 1][j - 1] - i;
                       int d2 = f[i - 1][j - 1] - j;
                       printf("%d\n", ABS(d1) + ABS(d2));
            }
            else
            {
                    printf("Fegla Won\n");
            }
    }
    
    return 0;
}
