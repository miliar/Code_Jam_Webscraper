#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
char str[101];
vector<long long> fps;
inline bool is_fair(long long num)
{
    sprintf(str,"%lld",num);
    int len = strlen(str);
    for (int i = 0 ; i != len ; ++i)
        if (str[i] != str[len - i - 1])
            return false;
    return true;
}
inline void solve(int case_id)
{
    long long l,r;
    scanf("%lld%lld",&l,&r);
    long long ans = 0;
    for (auto it = fps.begin(); it != fps.end(); ++it)
        if (l <= *it && *it <= r)
        {
            ++ans;
            fprintf(stderr,"%lld\n",*it);
        }
        else if (*it > r)
            break;
    printf("Case #%d: %lld\n",case_id,ans);
}
int main()
{
#ifdef INDEED_OFFLINE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif // INDEED_OFFLINE
    long long tmp = 0;
    for (long long i = 1 ; i <= 10000000 ; ++i)
        if (is_fair(i) && is_fair(tmp = i*i))
            fps.push_back(tmp);
    int test_cases = 0;
    scanf("%d\n",&test_cases);
    for (int i = 1 ; i <= test_cases ; ++i)
        solve(i);

    return 0;
}
