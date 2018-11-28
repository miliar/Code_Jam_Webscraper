#include <bits/stdc++.h>
#define ll long long
#define modl 1000000007

using namespace std;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        ll n;
        scanf("%lld",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",t);
        }
        else{
            set<int> st;
            for(int i=1;;i++){
                ll num=i*n;
                int k=10;
                while(num/k!=0){
                    st.insert(num%k);
                    num/=10;
                }
                st.insert(num);
                if(st.size()==10){
                    printf("Case #%d: %lld\n",t,(i*n));
                    break;
                }
            }
        }
    }
    return 0;
}
