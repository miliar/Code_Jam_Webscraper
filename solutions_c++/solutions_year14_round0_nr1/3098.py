#include<bits/stdc++.h>
using namespace std;

void solve(){
    set<int> s,t,w;
    int n;
    scanf("%d",&n);
    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++){
            int x;
            scanf("%d",&x);
            if(i==n) s.insert(x);
        }
    scanf("%d",&n);
    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++){
            int x;
            scanf("%d",&x);
            if(i==n) t.insert(x);
        }
    for(set<int>::iterator i=s.begin();i!=s.end();i++)
        if(t.find(*i)!=t.end()) w.insert(*i);
    if(w.size()==1) printf("%d",*w.begin()); else
    if(w.empty()) printf("Volunteer cheated!");
        else printf("Bad magician!");
}

int main(){
    //freopen("1.txt","r",stdin);
    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("2.txt","w",stdout);

    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
        printf("\n");
    }

    return 0;
}
