# include <bits/stdc++.h>
using namespace std;

inline void myreverse(string & s, int index){
    reverse(s.begin(),s.begin()+index+1);
    for(int i=0 ; i<=index ; i++){
        if(s[i]=='+') s[i]='-';
        else s[i]='+';
    }
}

inline bool done(string & s){
    for(char & c : s){
        if(c=='-') return false;
    }
    return true;
}

int solve(string & s){

    int ans = 0 , fm , fp;

    while(!done(s)){
        for(int i=s.length()-1 ; i>=0 ; i--){
            if(s[i]=='-'){
                fm = i;
                break;
            }
        }

        if(s[0]=='-'){
            myreverse(s,fm);
        }else{
            for(int i=fm-1 ; i>=0 ; i--){
                if(s[i]=='+'){
                    fp = i;
                    break;
                }
            }

            myreverse(s,fp);
        }
        ans++;
    }
    return ans;
}

int main(){
    freopen("pancka.in","r",stdin);
    freopen("pancka.out","w",stdout);
    int t;
    cin>>t;
    for(int f=1 ;f<=t ; f++){
        string s;
        cin>>s;
        printf("Case #%d: %d\n",f,solve(s));
    }
}
