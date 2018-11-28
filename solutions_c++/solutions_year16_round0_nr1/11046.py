#include<bits/stdc++.h>
using namespace std;

int getMask(int mask, long long val){
    while(val > 0){
        int dig = val % 10;
        mask |= (1<<dig);
        val /= 10;
    }
    return mask;
}

int main(){

    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int t;
    scanf("%d", &t);

    for(int kase = 1; kase <= t; kase++){
        int n;
        scanf("%d", &n);

        long long val = n;
        int mask = 0;
        bool found = false;
        for(int i=1; i<=100000; i++){
            val = n * i;
            mask = getMask(mask, val);
            // cout << "Val: " << val << " mask: " << mask << endl;
            if(mask == 1023){
                found = true;
                break;
            }
        }
        if(found) printf("Case #%d: %lld\n", kase, val );
        else printf("Case #%d: INSOMNIA\n", kase);
    }

    return 0;
}
