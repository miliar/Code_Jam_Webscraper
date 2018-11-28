#include<iostream>
#include<cstdio>
using namespace std;


int cnt[17];

int T;

void doit(){
    int R,X;
    cin>>R;
    for(int i=1;i<=4;++i){
        for(int j=1;j<=4;++j){
            cin>>X;
            if(i==R) cnt[X]++;    
        }
    }
}

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;++cas){
        memset(cnt,0,sizeof(cnt));
        doit();
        doit();
        int result = -1;
        for(int i=1;i<=16;++i){
            if(cnt[i]==2){
                if(result==-1){
                    result = i;
                }
                else{
                    result = -2;
                }
            }
        }
        cout<<"Case #"<<cas<<": ";
        if(result==-1){
            cout<<"Volunteer cheated!\n";
        }
        else if(result==-2){
            cout<<"Bad magician!\n";
        }
        else{
            cout<<result<<endl;
        }
    }
    return 0;
}



