#include <iostream>
#include <cstdio>

using namespace std;

int selec[18];
void init(){
    for(int i=1;i<=16;i++) selec[i]=0;
}

int main(){
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int cas;
    cin>>cas;
    for(int i=1;i<=cas;i++){
        init();
        int f, c;
        for(int h=0;h<2;h++){
            cin>>f;
            for(int j=0;j<4;j++){
                for(int k=0;k<4;k++){
                    cin>>c;
                    if(j==f-1) selec[c]+=1;
                }
            }
        }
        int res=0;
        int card;
        for(int j=1;j<=16;j++){
            if(selec[j]==2){
                if(res==0){
                    card=j;
                    res=1;
                } else {
                    res=2;
                    break;
                }
            }
        }
        if(res==0) cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
        if(res==1) cout<<"Case #"<<i<<": "<<card<<endl;
        if(res==2) cout<<"Case #"<<i<<": Bad magician!"<<endl;
    }
    return 0;
}
