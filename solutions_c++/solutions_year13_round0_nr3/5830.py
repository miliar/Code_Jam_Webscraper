#include<iostream>
#include<math.h>
using namespace std;
bool is_pal(long int j){
    int a[2000000],i=0,ip=1;
     while(j!=0){
        a[i++]=j%10;
        j/=10;
    }
    for(int j=0;j<i/2;j++){
        if(a[j]!=a[i-1-j]){
               ip=0;
               break;
        }
    }
    if(ip==0) return false;
    else return true;
}
bool fairnsquare(long int j){
    if(floor((float)sqrt(j))!=ceil(((float)sqrt(j))))
    return false;
    if(is_pal(j)&&is_pal(sqrt(j)))
        return true;
    return false;
}
int main(){
int n,arr[10000],k=0;
long int a,b;
cin>>n;
for(int i=0;i<n;i++){
int c=0;
cin>>a>>b;
for(long int j=a;j<=b;j++)
if(fairnsquare(j)) c++;
arr[k++]=c;
}
for(int i=0;i<k;i++)
cout<<"Case #"<<i+1<<": "<<arr[i]<<endl;
return 0;
}
