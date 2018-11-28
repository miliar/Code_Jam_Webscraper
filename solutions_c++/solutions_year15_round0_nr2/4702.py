#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t,n,p[1001],i,j,counter,ans[1001],l,answer,tc;
    cin>>t;
    tc=1;
    while(t--){
        cin>>n;
        l=0;
        for(i=0;i<=n-1;i++){
            cin>>p[i];
            l=max(l,p[i]);
        }
        answer=1000000;
        for(i=1;i<=l;i++){
            counter=0;
            for(j=0;j<=n-1;j++){
                if(p[j]%i==0) counter+=(p[j]/i)-1;
                else{counter+=p[j]/i;}
            }
            answer=min(answer,counter+i);
        }
       cout<<"Case #"<<tc<<": "<<answer<<endl;
       tc++;
    }
}
