#include <cstdio>
#include <cstring>
#define NMAX 1007
FILE *fin, *fout;
using namespace std;
int t, n, sum , counter, sizen;
char s[NMAX];
int main()
{
    fin = freopen("ovation.in", "r", stdin);
    fout = freopen("ovation.out", "w", stdout);
    scanf("%d", &t);
    for(int i = 0; i< t; i++)
    {
        sum = 0;
        scanf("%d", &n);
        scanf("%s", s);
        sizen = strlen(s);
        counter = s[0] - '0';
        for(int j = 1; j< sizen; j++)
        {
            if(counter >= j)
            {
                counter+=s[j]-'0';
            }
            else
            {
                sum+=j - counter;
                counter = j + s[j] - '0';
            }
        }
        printf("Case #%d: %d\n", i+1, sum);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
