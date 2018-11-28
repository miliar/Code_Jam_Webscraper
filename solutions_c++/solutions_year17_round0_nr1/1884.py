#include <bits/stdc++.h>
#define ii pair<int, int>
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define vii vector< pair<int, int> >
typedef long long ll;
using namespace std;
char s[1005];
int main()
{
    int tt;
    scanf("%d", &tt);
    for(int qq = 1; qq<= tt; qq++)
    {
        double clock_start = clock();
        int n;
        scanf("%s", s);
        n = strlen(s);
        int k; scanf("%d", &k);
        int cnt = 0;
        for(int i = 0; i+k-1< n; i++)
        {
            if(s[i] == '+') continue;
            for(int j = i; j< i+k; j++)
            {
                s[j] = (s[j] == '-')?'+':'-';
            }
            cnt++;
        }
        bool bad = 0;
        for(int i = 0; i< n; i++) if(s[i] == '-') bad = 1;
        printf("Case #%d: ", qq);
        if(bad) printf("IMPOSSIBLE\n");
        else printf("%d\n", cnt);
        fprintf(stderr, "Test %d solved in %.2lf s.\n", qq, (clock()-clock_start)/CLOCKS_PER_SEC);
    }
	return 0;
}
