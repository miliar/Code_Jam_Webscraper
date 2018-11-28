#include <iostream>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <vector>

using namespace std;
int main()
{
	ifstream ifs( "B-large.in" );
    string strbuf;
    getline(ifs, strbuf);
    int test = atoi(strbuf.c_str());

int i,n,m;
for(m=0;m<test;m++){
string data1;
int data2[100],data3[100];
int fflag=0;


getline(ifs,strbuf);
//cout<<data[i]<<endl;
stringstream par1(strbuf);
par1>>data1;

for(int y=0;y<100;y++)
{
//  cout<<"data1"<<data1[y];
data2[y]=0;
data3[y]=0;
}
for(i=0;i<data1.length();i++){

if (data1[i]=='+'){data2[i]=1;

}
//cout<<data2[i]<<endl;
}
int j=100;
int f=0;
int c=0;
//cout<<j;
//cout<<"b4 while"<<data2[0]<<endl;
while(fflag==0){
  /*if(data1.length()==1){
    //cout<<"f"<<f;
    cout<<"b4 if"<<data2[0]<<endl;
    c=1;
    if(data2[0]==1&&c==1){
    cout<<"len"<<data1.length()<<"data2"<<data2[0];
    f=1;

    fflag=1;
    break;
     }
   
  }*/
     if((data1.length()==1) && (data2[0]==1)){
        // cout<<"f"<<0;
         break; 
     }
if(fflag==1){break;}
  for(int u=0;u<data1.length();u++)

{
data3[u]=data2[u];
//cout<<"data2"<<data2[u]<<endl;
//cout<<"datathir"<<data3[u]<<endl;
}
  for(int u=0;u<data1.length()-1;u++)
{
  
fflag=data3[u] && data3[u+1];
data3[u+1]=fflag;
//cout<<"data3"<<data3[u];

}
//cout<<"fflag"<<fflag<<endl;
if(fflag==1){break;}
if(j==0){break;}

//find index of -
for(int k=0;k<data1.length();k++){
	if(data2[k]==0){j=k;}
   }
  // cout<<"j"<<j;
   //if(j==100){break;}
//flip bits till index
for(int l=0;l<=j;l++){
       if(data2[l]==0){data2[l]=1;}
       else{
       data2[l]=0;

     }
     
   }
   //commence pancake chcking
 
f=f+1;
if(j==100){break;}
c=2;
}
cout<<"Case #"<<m+1<<": "<<f<<endl;
//cout<<"f"<<f;
}
}
