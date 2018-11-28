#include<bits/stdc++.h>

using namespace std;

int main(){
    freopen("D-small-attempt4.in","r",stdin);
    freopen("out.txt","w",stdout);
    int x,r,c,t;
    cin >> t;
    string ans="";
    for(int tt=1;tt<=t;tt++){
        ans="";
        cin >> x >> r >> c;
        if(x==1)
            ans="GABRIEL";
        else if(x==2){
            if(!((r*c)%2) && (r>1 || c>1))
                ans="GABRIEL";
        }
        else if(x==3){
            if(!((r*c)%3) && (r>1 && c>1))
                ans="GABRIEL";
        }
        else if(x==4){
            if(!((r*c)%4) && (r>2 && c>2))
                ans="GABRIEL";
        }
        if(!(ans.size()))
            ans="RICHARD";
        cout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}
