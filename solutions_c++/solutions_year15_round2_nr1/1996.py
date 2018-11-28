#include<iostream>
using namespace std;
const int maxm=1e6+2;
int a[maxm];
int rev(int n){
    int t=0;
    while(n>0){
        t*=10;
        t+=(n%10);
        n/=10;
    }
    return t;
}
/*int f(int k){
    if(k<12)return k;
    if(a[k]>=0)return a[k];
    if(k%10==0){
        a[k]=f(k-1)+1;
    }else{
        a[k]=min(f(k-1),f(rev(k)))+1;
    }
    return a[k];
}*/
int main(){
    for(int i=0;i<maxm;i++){
        a[i]=i;
    }
    for(int i=1;i<maxm;i++){
        a[i]=min(a[i-1]+1,a[i]);
        int r=rev(i);
        //a[i]=min(a[i],a[rev(i)]+1);
        a[r]=min(a[r],a[i]+1);
        //if(i%10!=0)a[i]=min(a[i-1],a[rev(i)])+1;
        //else a[i]=a[i-1]+1;
       // cout<<i<<"----"<<a[i]<<endl;
    }
    int p=0,t;
    cin>>t;
    while(t--){
        p++;
        int n;
        cin>>n;
        //cout<<a[n]<<endl;
         cout<<"Case #"<<p<<": "<<a[n]<<endl;
    }
}
