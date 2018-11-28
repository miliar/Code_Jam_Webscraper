#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<string>
using namespace std;


void solve(int num){
    int N;string str;
    cin>>N>>str;
    int sum=0,ans=0;

    for(int i=0;i<=N;i++){
        if(sum<i){
            ans+=i-sum;
            sum=i;
        }

        sum+=str[i]-'0';
    }

    cout<<"Case #"<<num+1<<": "<<ans<<endl;

}
int main(){
    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        solve(i);
    }
    return 0;
}
