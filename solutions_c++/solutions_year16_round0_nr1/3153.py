#include<iostream>
#include<string>
using namespace std;
bool aleary[10];

bool check(){
    for(int i=0;i<10;i++){
        if(!aleary[i])return false;
    }
    return true;
}
void upData(long long n){
    while(n){
        aleary[n%10]=true;
        n/=10;
    }
    return ;
}
long long getAns(long long n){
    for(int i=0;i<10;i++){
        aleary[i]=false;
    }
    long long current=n;
    while(true){
        upData(current);
        if(check()){
            return current;
        }
        current+=n;
    }
}
int main(){
    int t,cas=0;
    cin>>t;
    while(t--){
        long long n;
        cin>>n;
        if(n){
            cout<<"Case #"<<++cas<<": "<<getAns(n)<<endl;
        }
        else{
            cout<<"Case #"<<++cas<<": INSOMNIA"<<endl;
        }
    }
}

