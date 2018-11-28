#include <bits/stdc++.h>

using namespace std;

char gana(int X, int R, int C){
    if (C>R) swap(R, C);
    if(X==1) return 'G';
    if (X==2){
        if (((R*C)%2)==0) return 'G';
        return 'R';
    }
    if (X==3){
        if(((R*C)%3)!=0) return 'R';
        if(C==1) return 'R';
        return 'G';
    }
    if (((R*C)%4)!=0) return 'R';
    if (C<=2) return 'R';
    return 'G';
}

int main(){
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int N;
    cin>>N;
    for(int cas=1;cas<=N;cas++){
        char res;
        int x, r, c;
        cin>>x>>r>>c;
        res=gana(x, r, c);
        if(res=='R'){
            cout<<"Case #"<<cas<<": RICHARD"<<endl;
        } else {
            cout<<"Case #"<<cas<<": GABRIEL"<<endl;
        }
    }
    return 0;
}
