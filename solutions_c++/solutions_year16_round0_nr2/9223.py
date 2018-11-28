#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<cstring>

using namespace std;

int main(){


int t,c=0,h=0,a=0,k=0,y=0,f=0,l=1,i=0;

cin>>t;
//string m1;
int m[118];

while(t-->0){
string m1;
cin>>m1;
 
while(m1[i]!='\0'){i++;c++;}
//cout<<c<<endl;
for(i=0;i<c;i++){
  if(m1[i]=='+')m[i]=1;
  else m[i]=0;
}
//for(i=0;i<c;i++){
  //cout<<m[i]<<" ";
//}
m[i]=2;      


while(h!=c){
   h=0;
   f=0;
   for(i=0;i<c;i++){
          if(m[i]==1){h++;}
   }
   for(i=0;i<c;i++){
          if(m[i]==0){f++;}
   }
   if(f==c){++a;
     break;}
   if(h==c)break;
   int q=0,w=0;
   while(m[q]!=1){ if(w==c)break;w++;q++;}
   for(i=0;i<w;i++){m[i]=1;k=1;}
   if(k==1)
   a++;
   h=0;
   for(i=0;i<c;i++){
          if(m[i]==1){h++;}
   }
   if(h==c)break;
   q=0;w=0;
   while(m[q]!=0){if(w==c)break;w++;q++;}
   for(i=0;i<w;i++){m[i]=0;y=1;}
   if(y==1)   
   a++;
}
i=0;
c=0;
k=0;
y=0;
h=0;

cout<<"Case #"<<l<<": "<<a<<endl;
l++;
a=0;

}
return 0;
}


        
