#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f first
#define s second

int a[100];

int main(){

    freopen ("A-large.in", "r", stdin);
	freopen ("ans.out","w",stdout);
    int t;
    scanf("%d", &t);
    for(int z = 1; z <= t; ++z){

        int n;
        printf("Case #%d: " , z);

        scanf("%d" , &n);
        if(n == 0){
            printf("INSOMNIA\n");
            continue;
        }

        for(int i = 0; i < 10; ++i)a[i] = 0;
        ll i = 1, k = 10;
        while(true){

            ll tmp = n*i;

            while(tmp){
                if(!a[tmp%10])--k;
                a[tmp%10] = 1;
                tmp /= 10;
            }

            if(k == 0)break;
            ++i;

        }
        ll tmp = n*i;
        printf("%I64d\n" ,tmp);
    }

    return 0;
}
