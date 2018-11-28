#include <cstdio>
#include <set>
#include <cstring>

using namespace std;

bool isvowel(const char &c)
{
     return (c=='a' || c=='i' || c=='u' || c=='e' || c=='o');
}

int main(void)
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t, n, l, i, c, tc=0;
    long long res;
    char chr[1000005];
    set <int> memo;
    set <int> :: iterator it;
    for (scanf("%d", &t);t--;)
    {
        scanf("%s%d", chr, &n);
        res=0;
        l=strlen(chr);
        memo.clear();
        for (c=i=0;i<l;i++)
        {
            (isvowel(chr[i])) ? (c=0) : (c++);
            if (c>=n)
            {
               c--;
               it=memo.insert(i-c).first;
               if (it!=memo.begin())
               {
                  it--;
                  res+=(long long)(i-c-(*it))*(long long)(l-i);
               }
               else
                  res+=(long long)(i+1-c)*(long long)(l-i);
            }
        }
        printf("Case #%d: %lld\n", ++tc, res);
    }
    return 0;
}
