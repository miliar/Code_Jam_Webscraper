/// #sh

#include<bits/stdc++.h>

using namespace std;

int main(){
    #ifndef ONLINE_JUDGE
        freopen("A-large.in", "r", stdin);
        freopen("ans1_large.out", "w", stdout);
    #endif // ONLINE_JUDGE

    int test;
    scanf("%d", &test);

    for(int t = 1; t <= test; ++t){
        int n, ans = 0, cnt = 0;
        scanf("%d", &n);

        vector<bool> arr(10);

        for(int i=1; i<=100; ++i){

            int val = i * n;
            ans = val;

            while(val){
                int id = val % 10;
                arr[id] = true;
                val /= 10;
            }

            cnt = 0;
            for(int j=0; j<10; ++j)
                if(arr[j])
                    cnt++;
            if(cnt == 10)
                break;
        }

        if(cnt == 10)
            printf("Case #%d: %d\n", t, ans);
        else
            printf("Case #%d: INSOMNIA\n", t);
    }

}
