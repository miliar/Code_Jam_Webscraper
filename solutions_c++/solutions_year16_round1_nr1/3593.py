#include <bits/stdc++.h>

using namespace std;

string mayPab[1050];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin>>T;
    for(int caso=1;caso<=T;caso++){
        string S, aux1, aux2;
        cin>>S;
        mayPab[0]=""+string(1,S[0]);
        for(int i=1;i<S.size();i++) mayPab[i]="";
        for(int i=1;i<S.size();i++){
            //string aux3=S[i];
            aux1=string(1,S[i])+mayPab[i-1];
            aux2=mayPab[i-1]+string(1,S[i]);
            mayPab[i]=max(aux1, aux2);
        }
        cout<<"Case #"<<caso<<": "<<mayPab[S.size()-1]<<endl;
    }
}
