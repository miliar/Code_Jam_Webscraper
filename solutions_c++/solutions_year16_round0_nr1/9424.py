#include <bits/stdc++.h>
typedef long long int ll;
using namespace std;
set<ll> st;
set<ll> :: iterator it;
void dig(ll n){
int mod;
while(n!=0){
    mod=n%10;
    st.insert(mod);
    n/=10;
}
}
int check(){
int cnt=0;
for(it=st.begin();it!=st.end();it++){
    if(*it>=0&&*it<=9)cnt++;
}
if(cnt==10)return 1;
else return 0;


}
int main()
{
    int t,l=1;
    freopen("tk.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--){
        ll n,p=0;
        cin>>n;
        if(n==0){
            printf("Case #%d: INSOMNIA\n",l++);
            continue;
        }
        int i=1;
        while(1){
            p=n*i;
            dig(p);
            int ok=check();
            if(ok==1)break;i++;
        }
        printf("Case #%d: %I64d\n",l++,p);
        st.clear();

    }
    return 0;
}
