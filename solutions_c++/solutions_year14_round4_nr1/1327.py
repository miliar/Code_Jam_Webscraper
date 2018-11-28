#include <bits/stdc++.h>
using namespace std;


int a[100005];
int main(){

 freopen("in.c","r",stdin);
 freopen("salida.c","w",stdout);

    int tc , n , cap , nc = 1;
    cin >> tc;

    while(tc--){
        cin >> n >> cap;
        for(int i = 0; i < n; ++i)
            scanf("%d",&a[i]);

        sort(a,a+n);
        int res = 0;
        int le = 0 , ri = n - 1;
        while(le < ri){
            if(a[le] + a[ri] <= cap) le++ , ri--;
            else ri--;
        res++;
        }
        if(le == ri) res++;

        printf("Case #%d: %d\n",nc++,res);

    }







    return 0;
}

