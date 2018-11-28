#include <iostream>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <vector>

using namespace std;
int main()
{
ifstream ifs( "A-large.in" );
    string strbuf;
    getline(ifs, strbuf);
    int test = atoi(strbuf.c_str());
    //cout<<test;
string data[100000];
int i,n,m;
int fflag=0;
int r;
for(i=0;i<test;i++){
r=i;
//cout<<"r"<<r<<endl;
getline(ifs,data[i]);
//cout<<data[i]<<endl;
stringstream par1(data[i]);
//cout<<"row"<<i<<endl;
int data1[10],data2[10],data3[10];
for(int y=0;y<10;y++)
{
data1[y]=0;
//cout<<data1[y];
data2[y]=0;
data3[y]=0;
}
int n;

par1>>n;
//cout<<"n"<<n<<endl;

int rem,num;
int inc=1;
num=n;
int fflag=0;
while(fflag==0)
{
//for each case process. break when all is 1
//num=n;
if (n==0){cout<<"Case #"<<r+1<<": INSOMNIA"<<endl;
break;}
	int j;
	j=0;
for (int k = 0; num>0; k++) {
rem = num %10;
//cout<<"rem\t"<<rem;
num = num / 10;
data1[k]=rem;
//cout<<"data\t"<<data1[k];
j=j+1;
//cout<<"j"<<j;
}
for(int p=0;p<j;p++){
   for(int l=0;l<10;l++)
       if(data1[p]==l){
                   data2[l]=1;
  //                 cout<<"datasec\t"<<data2[l]<<endl;
 
         }
  }
  for(int u=0;u<10;u++)
{
data3[u]=data2[u];
//cout<<"datathir"<<data3[u]<<endl;
}
for(int u=0;u<9;u++)
{
fflag=data3[u] && data3[u+1];
data3[u+1]=fflag;
}
inc=inc+1;
num=n*inc;
//num=n;
//cout<<"n"<<num<<endl;
}
if(n!=0){
cout<<"Case #"<<r+1<<": "<<num-n<<endl;}
}
}
