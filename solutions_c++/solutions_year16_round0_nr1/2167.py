#include<iostream>
#include<cstdio>
using namespace std;

int fun(int N){
    if (N==0) return -1;
    int digitmask=0;
    
    int n=0;
    while(digitmask!=(1<<10)-1 ){
        n+=N;
        int t=n;
        while(t){
            digitmask|=(1<<(t%10) );
            t/=10;
        }
    }
    return n;

}
void test(){
    for(int i=0;i<=20;i++)
        cout<<i<<" "<<fun(i)<<endl;
}
int main(){
    //test();
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int N,T;
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>N;
        int r=fun(N);
        if(r==-1)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else cout<<"Case #"<<i<<": "<<r<<endl;
    }
    return 0;
}