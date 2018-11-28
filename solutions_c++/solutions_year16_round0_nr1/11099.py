#include<string>
#include<iostream>
#include<stdlib.h>

using namespace std;


int main(){

int n;

int t,a,k=2,r,m=0,n1,v=1,y=0;

cin>>t;

int p[10]={0};


while(t-->0){

cin>>n;
r=n;


while(m!=10000){
  n1=n;
   while(n)
{   
    
    a=(n % 10);
    if(a==0)
        p[0]=1;
    else if(a==1)
        p[1]=1;
    else if(a==2)
        p[2]=1;
    else if(a==3)
        p[3]=1;
     else if(a==4)
        p[4]=1;
     else if(a==5)
        p[5]=1;
     else if(a==6)
        p[6]=1;
     else if(a==7)
        p[7]=1;
     else if(a==8)
        p[8]=1;
     else if (a==9)
        p[9]=1;
    n /= 10;
}
//cout<<n;
for(int i=0;i<10;i++){
       if(p[i]==1)
          y++;
}
//cout<<y<<endl;
if(y==10)
   break;
else n=r*k;
k++;
m++;
y=0;
}

if(y==10)
   cout<<"Case #"<<v<<": "<<n1<<endl;
else
   cout<<"Case #"<<v<<": INSOMNIA"<<endl;

m=0;
k=2;
v++;
for(int i=0;i<10;i++){
       p[i]=0;
          
}
}
return 0;



}

