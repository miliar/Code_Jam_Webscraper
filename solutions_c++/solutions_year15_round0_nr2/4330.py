#include<cstdio>
#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;
void solve(int cs){
    int N;
    cin>>N;
    vector<int>V(N);
    for(int i=0;i<N;i++)cin>>V[i];

    int mi=1<<30;
    for(int i=1;i<=9;i++){
        int cnt=0;
        for(int j=0;j<N;j++){
            cnt+=(V[j]+i-1)/i-1;
        }
        mi=min(mi,cnt+i);
    }

    cout<<"Case #"<<cs<<": "<<mi<<endl;
}
int main(){
    int T;
    cin>>T;
    for(int i=0;i<T;i++)solve(i+1);
    return 0;
}

