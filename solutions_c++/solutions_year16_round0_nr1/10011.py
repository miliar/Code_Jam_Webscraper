#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <utility>

using namespace std;

bool used[10];

void split(int n){
    int k;
    if(n==0){
        used[0]=1;
    }
    while(n){
        k=n%10;
        n/=10;
        used[k]=1;
    }
}

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,T;
    cin>>T;
    for(t=1;t<=T;t++){
        int N,i,j;
        
        bool allused,ans;
        //N=t;
        cin>>N;
        
        for(i=0;i<10;i++)
            used[i]=0;
        ans=0;
        for(i=1;i<1000001;i++){
            split(N*i);
            allused=1;
            for(j=0;j<10;j++){
                //cout<<used[j]<<' ';
                if(used[j]==0){
                    allused=0;
                }
            }
            //cout<<endl;
            if(!allused)
                continue;
            else{
                ans=1;
                cout<<"Case #"<<t<<": "<<i*N<<endl;
                break;
            }
        }
        if(!ans){
            cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
        }
    }
    return 0;
}