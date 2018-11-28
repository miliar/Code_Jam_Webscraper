#include <iostream>
#include <cstdio>
#include <cstring>

#define loop(i, n) for(int i = 0; i < n; i++)
#define FOR(i, x, n) for(int i = x; i <= n; i++)
#define mem(x, y) memset(x, y, sizeof(x))

using namespace std;

bool marked[11];
int cnt = 0;

void breakNumber(long long x) {
    
    long long temp = x;
    long long mod = 0;

    while(temp != 0) {   
        mod = temp % 10;
        
        if(!marked[mod]) {
            marked[mod] = true;
            //cout << "mod-> " << mod << " cnt --> " << cnt << endl;
            cnt++;
        }

        temp /= 10;
    }
}

int main() {
   
    freopen("inn.in", "r", stdin);
    freopen("inn.out", "w", stdout);

    int t, cntt; scanf("%d", &t);

    while(true) {
        
        long long x; scanf("%lld", &x);
        long long temp = x;
        long long c = 1;
        
        cnt = 0;
        mem(marked, false);

        while(true) {
            
            if(x == 0) {
                printf("Case #%d: INSOMNIA\n", ++cntt);
                break;
            }
          
            breakNumber(temp);
 
            if(cnt >= 10) {
                printf("Case #%d: %lld\n", ++cntt, temp);
                break;
            }

            temp = x * c++;

            //cout << "hello " << endl;
        }
        
        if(cntt == t) break;
    }

    return 0;
}
