#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int T;
ll N;
bool arr[11];
int cnt=0;
ll aux;
int ith=1;
ll last;
int cc=1;


void solve( ){

    aux=N*ith;
    last=aux;
    while(aux>0){
        if( !arr [aux%10] ){
            arr[aux%10]=1;
            cnt++;
        }
        aux/=10;
    }
    ith++;
}


int main(){

    //freopen("input.in","r",stdin);
    //freopen("outhput.out","w",stdout);

    cin>>T;
    for(int i=0;i<T;i++){
        cin>>N;
        ith=1;
        cnt=0;
        memset(arr,false,sizeof( arr) );
        if( N==0) cout<<"Case #"<<cc++<<": INSOMNIA"<<endl;
        else{
            while(true){
                solve();
                if(cnt==10) break;
            }
            cout<<"Case #"<<cc++<<": "<<last<<endl;
        }
    }
    return 0;
}
