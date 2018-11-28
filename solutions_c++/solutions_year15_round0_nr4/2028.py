#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("Dsmallin.txt","r",stdin);
    freopen("Dsmallout.txt","w",stdout);
    int n;
    bool done=false;
    cin>>n;
    for (int i=0; i<n; i++){
        int a,b,c;
        cin>>a>>b>>c;
        if (a>=7){
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
            continue;
        }
        if (b*c%a!=0){
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
            continue;
        }
        for (int j=1; j<=(a+1)/2; j++){
            if ((b<j or c<a-j+1) and (c<j or b<a-j+1)){
                cout<<"Case #"<<i+1<<": RICHARD"<<endl;
                done=true;
                break;
            }
        }
        if (done){
            done=false;
            continue;
        }
        if (a==6){
            if (b==4 || c==4){
                cout<<"Case #"<<i+1<<": RICHARD"<<endl;
                continue;
            }
        }
        if (a==5){
            if (b==3 || c==3){
                cout<<"Case #"<<i+1<<": RICHARD"<<endl;
                continue;
            }
        }
        if (a==4){
            if (b==2 || c==2){
                cout<<"Case #"<<i+1<<": RICHARD"<<endl;
                continue;
            }
        }
        cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
    }
    return 0;
}
