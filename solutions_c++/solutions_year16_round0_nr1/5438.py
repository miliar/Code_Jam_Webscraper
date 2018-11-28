#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<string>
using namespace std;


int main()
{
bool flag;
ifstream it;
ofstream ot;
it.open("A-large.in");
ot.open("one-output.out");
long long int j,t,i,k;
long long int n,temp,temp1;
it>>t;
for(k=1;k<=t;k++)
{
 int ar[10]={0};
 it>>n;
 flag=true;
 if(n==0)
//   cout<<"Case #"<<k<<": INSOMNIA\n";
   ot<<"Case #"<<k<<": INSOMNIA\n";
 else
 {   
  long long int count=1;
  temp1=n;
  while(flag)
  {
   n=temp1*count;
   count++;
 //  cout<<"n :"<<n<<"\n";
   temp=n;
   while(temp)
    {
	ar[temp%10]++;
	temp=temp/10;
    }
   for(i=0;i<10;i++)
    {
	if(ar[i]==0)
		break;
    }
   if(i==10)
	flag=false;
  }// while flag
//  cout<<"Case #"<<k<<": "<<n<<"\n";
  ot<<"Case #"<<k<<": "<<n<<"\n";

 }

}// tst case
it.close();
ot.close();
return 0;
}
