#include<string>
#include<iostream>
#include<stdlib.h>

using namespace std;


int main(){

long long int score;
//cin>>score;
long long int n=0;
long long int t;
int a;
long long int k=2;
long long int r;
long long int p=0;
long long int g;
cin>>t;
long long int v=1;
int c=0;
int m[10]={0};
//for(int i=0;i<10;i++){
  //     cout<<m[i]<<endl;
          //c++;
//}

while(t-->0){

cin>>score;
r=score;


while(p!=10000){
  g=score;
   while(score)
{   
    
    a=(score % 10);
    if(a==0)
        m[0]=1;
    else if(a==1)
        m[1]=1;
    else if(a==2)
        m[2]=1;
    else if(a==3)
        m[3]=1;
     else if(a==4)
        m[4]=1;
     else if(a==5)
        m[5]=1;
     else if(a==6)
        m[6]=1;
     else if(a==7)
        m[7]=1;
     else if(a==8)
        m[8]=1;
     else if (a==9)
        m[9]=1;
    score /= 10;
}
//cout<<score;
for(int i=0;i<10;i++){
       if(m[i]==1)
          c++;
}
//cout<<c<<endl;
if(c==10)
   break;
else score=r*k;
k++;
p++;
c=0;
}

if(c==10)
   cout<<"Case #"<<v<<": "<<g<<endl;
else
   cout<<"Case #"<<v<<": INSOMNIA"<<endl;

p=0;
k=2;
v++;
for(int i=0;i<10;i++){
       m[i]=0;
          //c++;
}
}
return 0;



}

