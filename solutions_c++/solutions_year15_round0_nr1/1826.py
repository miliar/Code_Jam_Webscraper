
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <algorithm>

using namespace std;

int T;

void input(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
}



void solve(){
    int n,s,res,x;

    string str;
    cin>>T;
    for (int t=0;t<T; t++) {
        s=0; res =0; //init
        cin>>n;
        getline(cin,str);
        while (str[0]==' ') {
            str.erase(0,1);
        }

        for (int i=0; i<=n; i++) {
            x= int(str[i])-int('0');
            if (i!=0 && x!=0) {
                res+=max(i-s,0);
                //cout<<max(i-s,0);
                //cout<<i-s<<endl;
                s=max(s,i);
            }
            //cout<<s<< " "<<x<<endl;
            s+= x;

        }
        cout<<"Case #"<<t+1<<": "<<res<<endl;
    }
}

void output(){

}

void process(){
    input();
    solve();
    output();
}

int main() {
    process();
    return 0;
}

