#include<iostream>
#include<cstring>
#include<algorithm>
#include<stdio.h>
using namespace std;
bool array[10];
int main(){
    long long int t,n,temp,temp1,temp2,temp3,i,count,j=1;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    while(j<=t){
       count=0;
       i=2;
       cin>>n;
       temp3=temp2-1;
       temp2=n;
       while(count<10&&temp3!=temp2){
            temp=temp3=temp2;
            while(temp>0&&count<10){
                temp1=temp%10;
                count=array[temp1]==false?count+1:count;
                array[temp1]=true;
                temp/=10;
            }
            if(count==10)
                break;
            temp2=i*n;
            i++;
       }
       if(count==10){
          cout<<"Case #"<<j<<": "<<temp3<<endl;
       }
       else{
            cout<<"Case #"<<j<<": INSOMNIA"<<endl;
       }
       j++;
       for(i=0;i<10;i++){
        array[i]=false;
       }
    }
}
