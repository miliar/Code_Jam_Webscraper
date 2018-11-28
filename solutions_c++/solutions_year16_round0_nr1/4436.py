
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>
using namespace std;
bool visited[10];
bool check(){
    for(int i=0;i<10;i++)
    {
        if(visited[i]==false)
            return false;
    }
    return true;
}
void func(long long int num){
    while(num){
        visited[num%10]=true;
        num/=10;
    }
}
void init(){
    for(int i=0;i<10;i++)
        visited[i]=false;
}

int main(){
    ofstream fout("A.out");
    int testCase;cin>>testCase;
    long long int n;
    long long int ans = 0;
    long long int cnt;
    for(int t=1;t<=testCase;t++){
        init();
        cnt=1;
        scanf("%lld",&n);
        if(n==0){
            fout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
        }
        else{
        while(!check()){
            ans=n*cnt;
            func(ans);
            cnt++;
        }
        fout<<"Case #"<<t<<": "<<ans<<endl;
        }
        
    }
    
}
