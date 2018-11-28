#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <iomanip>
#include<cstring>
using namespace std;
#define rep(i,n) for(int i = 0; i < n; ++i)
#define pii pair<int,int>

bool marked(bool arr[]){
    rep(i,10){
        if(arr[i]==false){
            return false;
        }
    }
    return true;
}

void mark(long int n,bool arr[]){
    while(n){
        arr[n%10]=true;
        n/=10;
    }
}


int main(){
    int M;
    cin>>M;
    rep(i,M){
        long int N,ans;
        cin>>N;

        if(N==0){
            cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
            continue;
        }

        ans=N;
        bool marks[10]={};
        while(!marked(marks)){
            //cout<<"debug:"<<ans<<endl;
            mark(ans,marks);
            ans+=N;
        }

        cout<<"Case #"<<i+1<<": "<<ans-N<<endl;
    }

    return 0;
}
