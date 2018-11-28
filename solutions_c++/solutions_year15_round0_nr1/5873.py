#include<iostream>
#include<stdio.h>
using namespace std;

main(){
 freopen("A-large.in", "r", stdin);
freopen("out.txt", "w", stdout);

int t;
int smax,sum=0,ans=0;
int temp=1;
cin>>t;
while(t--){
        sum=0;
        ans=0;

        cin>>smax;
char myArray[smax+1];
for(int i=0;i<=smax;i++)
{

    cin>>myArray[i];
if(i>0){
sum+=myArray[i-1]-48;


}
if(i<=sum){
    ans+=0;
}
else{
    ans+=i-sum;
    sum+=i-sum;
}


}

    cout<<"Case #"<<temp<<": "<<ans<<"\n";
temp++;
}

}
