#include <bits/stdc++.h>

using namespace std;

int main(){

    int t;
    cin>>t;
    for (int i=1;i<=t;i++){
        long long int k;
        cin>>k;
        if (k==0){
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
        else{
            int m[10]={0,0,0,0,0,0,0,0,0,0};
            int count=0,l=1;
            while(count!=10){
                long long int j=l*k;
                while(j!=0){
                    if(m[j%10]==0){
                        m[j%10]=1;
                        count++;
                    }
                    j=j/10;
                }
                l++;
            }
            cout<<"Case #"<<i<<": "<<(l-1)*k<<endl;
        }
    }
return 0;
}