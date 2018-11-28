#include <cstdio>
#include <vector>
#include <map>

using namespace std;

long long a[10000];
long long b[10000];

int main()
{
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, j;
        vector <long long> v;
        map <long long, long long> mp;
        map <long long, long long>::reverse_iterator it;
        
        scanf("%d", &n);
        
        for (j = 0; j < n; j++) scanf("%lld", &a[j]);
        for (j = 0; j < n; j++) scanf("%lld", &b[j]);
        
        mp[0] = 1;
        
        for (j = 0; j < n; j++) {
            while (mp[a[j]] < b[j]) {
                v.push_back(a[j]);
                
                for (it = mp.rbegin(); it != mp.rend(); it++) {
                    long long x = it->first;
                    long long y = it->second;
                    
                    mp[x + a[j]] += y;
                }
            }
        }
        
        printf("Case #%d:", i + 1);
        for (j = 0; j < v.size(); j++) printf(" %d", v[j]);
        puts("");
    }
    
    return 0;
}
