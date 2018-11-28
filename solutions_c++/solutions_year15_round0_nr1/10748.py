#include<bits/stdc++.h>

using namespace std;

#define Ss(x) scanf("%s",&x)
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%ld",&x)
#define Sll(x) scanf("%lld",&x)
#define ull unsigned long long
#define ul unsigned long
#define V(x) vector<x>
#define vecit(x) vector<x>::iterator
#define pb(x) push_back(x)
#define Fl(i,a,n) for(i=(a);i<n;i++)
#define Fg(i,n) for(i=(n);i>0;i--)
#define tin freopen("aain.txt","r",stdin)
#define minof(a,b) a>b?b:a
#define maxof(a,b) a>b?a:b
#define strit string::iterator
#define mod 1000000007
#define gc getchar_unlocked
#define pc(x) putchar_unlocked(x);


int main()
{
    long t, n, i, j, ans, sum;
    char s[1000];

    FILE *ptr, *fp;
    ptr = fopen("file.txt", "w");
    fp = fopen("A-small-attempt2.in", "r");
    fscanf(fp, "%ld", &t);
    Fl(j, 1, t + 1) {
        fscanf(fp,"%ld", &n);
        ans = 0;
        fscanf(fp, "%s", s);
        sum = (long)s[0] - 48;
        Fl(i, 1, n + 1) {
            if(s[i] != '0') {
                if(sum >= i) {
                    sum += s[i] - 48;
                } else {
                    ans += i - sum;
                    sum += i - sum;
                    sum += s[i] - 48;
                }
            }
        }
        fprintf(ptr, "Case #%ld: %ld\n",j,ans);
    }
    fclose(ptr);
    return 0;
}
