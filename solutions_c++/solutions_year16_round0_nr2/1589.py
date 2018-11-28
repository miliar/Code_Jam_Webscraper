#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

#define ff first
#define ss second
/*
unordered_map<string,bool> m;
int method2(string s){
    string ss = "";
    for(int i=0;i<s.size();i++)ss+="+";
    queue<pair<string,int>> q;
    q.push({s,0});
    m[s] = true;
    while(!q.empty()){
        string s = q.front().ff;
        int y = q.front().ss;
        q.pop();
        if(s==ss){
            return y;
        }
        for(int i=0;i<s.size();i++){
            string r = s;
            for(int j=0;j<=i;j++){
                if(s[i-j]=='+')r[j]='-';
                else r[j]='+';
            }
            if(m.find(r)==m.end()){
                m[r]=true;
                q.push({r,y+1});
            }
        }
    }
}
*/

int method1(string s){
    int x  = 0;
    string ss = "";
    for(int i=0;i<s.size();i++)ss+="+";
    while(s!=ss){
        int y = 0;
        while(s[0]==s[y])y++;
        char c = s[0];
        for(int i=0;i<y;i++){
            if(c=='+')s[i]='-';
            else s[i]='+';
        }
        x++;
    }
    return x;
}
/*
void test(string s){
    if(s.size()==10){
        m.clear();
        if(method1(s)!=method2(s))cout << "shit\n";
        else cout << "prop\n" ;
    }
    else{
        test(s+"+");
        test(s+"-");
    }
}
*/

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outbig.txt","w",stdout);
    //test("");
    int t;
    scanf("%d",&t);
    for(int I=1;I<=t;I++){
        string s;
        cin >> s;
        printf("Case #%d: %d\n",I,method1(s));
    }
    return 0;
}
