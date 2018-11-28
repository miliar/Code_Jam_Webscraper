#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int tc;
    int m;
    int stan,c;
    string s;
    cin>>tc;
    int j=1;
    while(j<=tc){
        c=0;
        stan=0;
        cin>>m;
        cin>>s;
        for(int i=0; i<s.length(); i++){
            int i_in=s[i] - '0';
            //cout<<"int at pos: "<<i<<": "<<i_in<<endl;
            if(stan<i && i_in!=0){
                c+=(i-stan);
                stan+=(i-stan);
            }
            stan+=i_in;
            //cout<<"stan: "<<stan<<endl;
        }

        cout<<"Case #"<<j<<": "<<c<<endl;
        j++;
    }
}
