#include<iostream>
 #include<fstream>
using namespace std;
typedef long long int big_int;

int main()
{ 
ifstream fin;
ofstream fon;
fin.open("A-large.in",ios::in);
fon.open("sheepOutput",ios::out);


int t,t1;
//cin>>t;
fin>>t;
t1=t;
while(t!=0)
{
big_int n,num;
int cnt=0,r;
int a;
a=2;
bool arr[10]={0,0,0,0,0,0,0,0,0,0};
//cin>>n;
fin>>n;
if(n==0)
fon<< "case #"<<t1-t+1<<": "<<"INSOMNIA"<<"\n";
else
{
while(cnt!=10)
{  num=n;
   
 // cout<<num<<"  ";
   while(num!=0)
   {
   	  r=num%10;
   	  num/=10;
   	  if(arr[r]==0)
   	  {  arr[r]=1;
   	    cnt+=1;
		 }
   }
   num=n;
	n=n*a/(a-1);
	a++;
}
   fon<<"case #"<<t1-t+1<<": "<<num<<"\n";
   
   }
   t--;
}
	return 0;
}
