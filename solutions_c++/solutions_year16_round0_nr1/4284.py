#include <bits/stdc++.h>
using namespace std;
typedef long long int64;
struct Time{
    clock_t c_lock=clock();
    ~Time(){
        fprintf(stderr,"\nrunning time: %lums\n",1000*(clock()-c_lock)/CLOCKS_PER_SEC);
    }
}Time;//return running time.
unordered_set<int>num;
int cases,n;
int64 store[1000010];
void getstore(){
    memset(store, 0, sizeof store);
    for(int i=1;i<=1000000;i++){
        num.clear();
        int64 now=0,tmp=0;
        while (num.size()<10) {
            now+=(int64)i;
            tmp=now;
            while (tmp>=10) {
                num.insert(tmp%10);
                tmp/=10;
            }
            num.insert((int)tmp);
        }
        store[i]=now;
    }
}
int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    getstore();
    scanf("%d",&cases);
    for(int i=1;i<=cases;i++){
        scanf("%d",&n);
        printf("Case #%d: ",i);
        if (!n) {puts("INSOMNIA");continue;}
        printf("%lld\n",store[n]);
    }
}