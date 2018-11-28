#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 1e14
//#define MAX 1e3

vector<long long> vec;
char ctemp[111];
bool check(long long n)
{
    int i=0;
    int tot;
    while (n>0) {
        ctemp[i]=n%10;
        n/=10;
        i++;
    }
    tot=i;
    for(i=0; i<(tot+1)/2; i++) {
        if(ctemp[i]!=ctemp[tot-1-i]) {
            return false;
        }
    }
    return true;
}
void precompute()
{
    for (long long i=1; i*i<=MAX; i++) {
        if(check(i*i) && check(i)) {
            vec.push_back(i*i);
        }
    }
}

int main()
{
    int t, caseno=0;
    long long a, b;
    long long ans;
    int i, len;
    precompute();
    len=vec.size();
    scanf("%d", &t);
    //printf("%d %lld\n", (int)vec.size(), vec[(int)vec.size()-1]);
    while (t--) {
        scanf("%lld%lld", &a, &b);
        ans=0;
        for(i=0; i<len;i++) {
        	if(vec[i]>=a && vec[i]<=b)
        		ans++;
				}
        //ans=upper_bound(vec.begin(), vec.end(),b)-lower_bound(vec.begin(), vec.end(), a);
        printf("Case #%d: ", ++caseno);
        printf("%lld\n", ans);
    }
    return 0;
}
