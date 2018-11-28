#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
int t;
cin>>t;
int cases =0;
while(t-->0)
{
	cases++;
 double C,f,x;
 //cin>>C>>f>>x;
 scanf("%lf%lf%lf",&C,&f,&x);
 double dold,dnew,cold,cnew,snew,sold,sumc=0,sumd;
 double rate = 2.0000000;
 //cout<<" first division = "<<C/rate<<endl;
 int i=0;
std::cout.precision(7);
  sold = x/rate;
  while(1)
  { 
	cnew = C/rate;
  	dnew = x/rate;
  	if(i==0)
  	{ 
	   dnew = x/rate;
	   snew = dnew;
	   //cnew = 0;
	}
	else{
	   sumc = sumc+cold;
	   snew = sumc+dnew;
     }
     if(snew>sold)
       {
 	    //cout<<"milgaya = "<<sold<<endl;
	    break;
	   }
	//cout<<"snew ="<<snew<<endl; 
	cold = cnew;
	dold = dnew;
	sold = snew;
// 	if(i!=0)
	rate = rate+f;	
	i++;
  }
   //std::cout.precision(7);
  //std::fixed;
  //Case #1: 1.0000000
  printf("Case #%d: %.7lf\n",cases,sold);
  //std::cout <<sold<<endl;// '\n' << b << '\n' << c << '\n';
  
}
cin.get();
cin.get();
return 0;
}
