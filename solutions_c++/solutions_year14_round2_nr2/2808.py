#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int main(){
    int t,i;
    cin>>t;
    for(i=0;i<t;i++){
        int a,b,k,y,count=0,j,x;
        cin>>a;
        cin>>b;
        cin>>k;
//        cout<<(a&b);
        for(j=0;j<a;j++){
            for(x=0;x<b;x++){
                y=(x&j);
                if(y<k){
                    count++;
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<count<<endl;
    }
    return 0;
}
