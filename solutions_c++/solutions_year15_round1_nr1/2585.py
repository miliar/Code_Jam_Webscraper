#include<iostream>
#include<cstdlib>

using namespace std;
int main () {
    long long int t,sub,n,i,j=1,input[20000],sum1,sum2,diff,mindiff;
    cin>>t;
    while(t){
        t-=1;
        cin>>n;
        for(i=0;i<n;i++){
        cin>>input[i];
        }
        sum1=0;
        sum2=0;
        mindiff=0;
        diff=0;
        sub=0;
for(i=0;i<n-1;i++){
        if(input[i]>input[i+1]&&i!=n-1){
            diff=input[i]-input[i+1];
            sum1+=diff;
        }
        if(diff>mindiff){
            sub=input[i+1];
            mindiff=diff;
               }
}
for(i=0;i<n-1;i++){
 if(input[i]<mindiff){
            sum2=sum2+input[i];
        }
        else{
            sum2+=mindiff;
        }
}
//        if(sum2!=0)
//        sum2=sum2-sub;
        cout<<"Case #"<<j<<": "<<sum1<<" "<<sum2<<endl;
        j++;
    }
    return 0;
}

