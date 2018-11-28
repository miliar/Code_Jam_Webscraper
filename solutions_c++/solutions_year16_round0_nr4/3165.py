#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
vector<ll> ans;
main()
{
    freopen("Q4in.txt","r",stdin);
    freopen("Q4out.txt","w",stdout);


    int t;
    scanf("%d",&t);
    for(int kase=1;kase<=t;kase++){
        int k,c,s;
        scanf("%d%d%d",&k,&c,&s);
        int id=0;
        ans.clear();
        for(;id<k;){
            ll tmp=0;
            for(int j=0;j<c&&id<k;j++,id++){
                tmp=tmp*k+id;
            }
            ans.push_back(tmp);
        }
        printf("Case #%d:",kase);
        if(((int)ans.size())<=s){
            for(ll p:ans) printf(" %lld",p+1);
            printf("\n");
        }
        else{
            printf(" IMPOSSIBLE\n");
        }
    }
}
