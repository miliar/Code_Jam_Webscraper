#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
string ans = "z";
void dfs(int r, int p, int s, string now){
    int i;
    if(r+p+s == 0){
        string aa = now;
        while(now.size() > 1){
            string nxt = "";
            for(i=0;i<now.size();i+=2){
                if(now[i] == now[i+1])
                    return;
                if(now[i] == 'P' && now[i+1] == 'S' || now[i] == 'S' && now[i+1] == 'P')
                    nxt += "S";
                else if(now[i] == 'R' && now[i+1] == 'S' || now[i] == 'S' && now[i+1] == 'R')
                    nxt += "R";
                else
                    nxt += "P";
            }
            now = nxt;
        }
        ans = min(ans, aa);
    }
    else{
        if(r > 0)
            dfs(r - 1, p, s, now + "R");
        if(p > 0)
            dfs(r, p - 1, s, now + "P");
        if(s > 0)
            dfs(r, p, s - 1, now + "S");
    }
}
int main()
{
    int tn, n, p, s, r;
    freopen("gcas.in", "r", stdin);
    freopen("gcas.out", "w", stdout);
    scanf("%d",&tn);
    for(int tt = 1;tt<=tn;tt++){
        scanf("%d%d%d%d",&n,&r,&p,&s);
        ans = "Z";
        dfs(r, p, s, "");
        if(ans == "Z")
            ans = "IMPOSSIBLE";
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}
