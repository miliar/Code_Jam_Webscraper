#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int n,tot,ans;
string st;
char ss[1500];
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T; cin>>T;
    for (int tt=1;tt<=T;tt++){
        int p; scanf("%d",&p);
        scanf("%s",ss); st=ss;
        tot=ans=0;
        for (int i=0;i<st.length();i++){
            if (tot>=i){
                tot+=st[i]-'0';
            } else {
                ans+=i-tot;
                tot=i+st[i]-'0';
            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }
}
