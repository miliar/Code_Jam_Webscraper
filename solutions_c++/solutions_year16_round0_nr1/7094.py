#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
long long int check(long long int a[]){
    for(int i=0;i<10;++i){
        if(a[i]==0)
            return 0;
    }
    return 1;
}

int main(){
    long long int t,i;
    cin >> t;
    for(long long int a0 = 0; a0 < t; a0++){
        long long int n,num,x;
       cin >> n;
            long long int a[10]={0};
        if(n==0)
            cout<<"Case #"<<a0+1<<": "<<"INSOMNIA"<<endl;
        else{
       for(i=1;!check(a);++i){
           num=n*i;
           while(num!=0){
               x=num%10;
               a[x]=1;
               num=num/10;
           }
       }
    cout<<"Case #"<<a0+1<<": "<<(i-1)*n<<endl;        
        }}
    return 0;
}
