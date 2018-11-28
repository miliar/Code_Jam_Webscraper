#include <bits/stdc++.h>
using namespace std;

int main(){
    int T;
    cin >> T;
    for(int test = 1; test <= T; ++test){
        int x,l;
        cin >> x >> l;
        string s;
        cin >> s;
        int m[5][5];
        m[1][1]=1,m[1][2]=2,m[1][3]=3,m[1][4]=4;
        m[2][1]=2,m[2][2]=-1,m[2][3]=4,m[2][4]=-3;
        m[3][1]=3,m[3][2]=-4,m[3][3]=-1,m[3][4]=2;
        m[4][1]=4,m[4][2]=3,m[4][3]=-2,m[4][4]=-1;
        int co=0,prev=-1;
        for(int i = 0 ; i < x*l; ++i){
            int po = i%x;int v;
            if(s[po]=='1')v=1;
            if(s[po]=='i')v=2;
            if(s[po]=='j')v=3;
            if(s[po]=='k')v=4;
            if(i==0){
                prev=v;
                if(prev==2){++co;prev=1;}
                continue;
            }
            int f = 0;
            if(prev < 0){
                f=1;
                prev=-prev;
            }
            prev = m[prev][v];
            if(f==1)prev=-prev;
            if(prev==2 && co==0){++co;prev=1;}
            if(prev==3 && co==1){++co;prev=1;}
            if(prev==4 && co==2){++co;prev=1;}
            //cout << co << prev << "\n";
        }
        if(prev==1 && co==3){
            printf("Case #%d: %s\n",test,"YES");
        }
        else{
            printf("Case #%d: %s\n",test,"NO");
        }
    }
    return 0;
}



