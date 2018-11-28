#include <bits/stdc++.h>

using namespace std;

vector<long long> divs[55];

long long ct(long long f, int base) {
    long long ans = 0, mult = 1;
    while(f) {
        ans += (f%10)*mult;
        mult *= base;
        f /= 10;
    }
    return ans;
}

long long tot(long long mask) {
    long long mask2 = 0,mult=1;
    while(mask) {
        mask2 += mask%2*mult;
        mult *= 10;
        mask /= 2;
    }
    return mask2;
}

int main() {
    freopen("coinin.txt","r",stdin);
    freopen("coinout.txt","w",stdout);

    int t,n,j;
    scanf("%d",&t);
    scanf("%d %d",&n,&j);
    for(int mask10 = 1<<(n-1), c = 0; c < j; mask10++) {
        long long mask = tot(mask10);
        //printf("%lld %d\n",mask,c);
        if(mask%2 == 0) continue;
        vector<long long> temp;
        temp.push_back(mask);
        for(int i = 2; i<= 10; i++) {
            long long res = ct(mask,i);
            for(long long j=2;j*j<=res;j++)
                if(res % j == 0) {
                    temp.push_back(j);
                    break;
                }
        }
        if(temp.size() == 10) {
            divs[c++] = temp; /*
            for(int p=1;p<temp.size();p++) {
                printf("%lld in base %d is %lld, divisor is %lld\n",
                       mask,p+1,ct(mask,p+1),temp[p]);
            }*/
        }
    }
    printf("Case #1:\n");
    for(int i=0;i<j;i++) {
        for(int z=0;z<divs[i].size();z++) {
            printf("%s%lld",z?" ":"",divs[i][z]);
        }
        puts("");
    }
    return 0;
}
