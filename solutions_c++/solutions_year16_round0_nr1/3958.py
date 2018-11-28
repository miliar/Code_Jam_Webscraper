#include <bits/stdc++.h>
using namespace std;
int sum=0;
int used[10]={0};
void coun(long long n){
    while(n>0){
        if(!used[n%10])sum++;
        used[n%10]=1;
        n/=10;
    }
}
int main(){
    long long n,i,cas,j;
    cin>>cas;
    for (j=0;j<cas;j++){
        for (i=0;i<10;i++)
            used[i]=0;
        sum=0;
        cin>>n;
        cout<<"Case #"<<j+1<<": ";
        if(n==0){
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        for (i=1;;i++){
            coun(i*n);
            if(sum==10)break;
        }
        cout<<n*i<<endl;
    }
}
