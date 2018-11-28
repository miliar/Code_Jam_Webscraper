#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

long int tobin(int in){
long int ans=0;
int k=0;
while(1){
    ans+=(in%2)*pow(10,k);
    k++;
    if(in==1)
        break;
    in=in/2;


}
return ans;
}

long int base(long int nu,int ba){
long int ans=0;
long int pro=1;
while(nu>0){
    ans=ans+pro*(nu%10);
    nu=nu/10;
    pro=pro*ba;
    }
return ans;
}

int iscomp(long int nu,int a[],int bb){
int i,j;
j=1;
long int k=sqrt(nu);
for(i=2;i<k+1;i++){
    if(nu%i==0){
        a[bb]=i;
        j=0;
        break;
        }
    }
if(j==0)
    return 1;
return 0;
}

int main(){
ifstream infile("1.in");
ofstream outfile("2.in");
int qwe,qwer,qwert;
infile>>qwe;
infile>>qwer;
infile>>qwert;
outfile<<"Case #1:"<<endl;
int cont=1;
int val,n,x,asd;
int a[10];
for(val=32769;val<65535;val=val+2){
    for(n=2;n<11;n++){
    if(iscomp(base(tobin(val),n),a,n)==1)
        x=1;
    else{
        x=0;
        break;
        }
    }
    if (x==1){
        outfile<<tobin(val);
        for(asd=2;asd<11;asd++){
            outfile<<" "<<a[asd];
            }
        outfile<<endl;
        cont++;
        }
    if(cont>50)
        break;
    }
}
