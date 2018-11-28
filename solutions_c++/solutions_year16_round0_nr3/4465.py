#include<iostream>
#include<algorithm>
#include<fstream>
#include<cmath>
#include<cstring>
#define ll long long int

using namespace std;
bool flag=true;
long long int j_global,c=0,len;
long long int num,divi[11];
ifstream it;
ofstream ot;

/*
void changeBase(ll x, ll y)
{
   if ( x < y )
   {
      	cout << x;
      	return;
   }
   	ll rem = x%y;
   	changeBase(x/y, y);
   	cout << rem;
}
*/

long long int isPrime(long long int n)
{
//  return 0 represent number is prime else return a divisor
if(n==2)
 return 0;
if(n%2==0)
 return 2;
int a=sqrt(n);
for(int i=3;i<=a;i+=2)
 {
   if(n%i==0)
	return i;
 }
return 0;
}


void generateNum(string prefix, ll  k)
{
  if(c<j_global)
  {
      if (k == 0) 
      {
	prefix=prefix+'1';
	//cout<<prefix<<"\n";
        int b=0;
        for(b=2;b<=10;b++)
         {
	  num=0;
	  for(int i=prefix.length()-1, j=0;i>=0;i--,j++)
	  	  if(prefix[i]=='1')
	  		  num=num+pow(b,j); // number in base b
	 // cout<<num<<"\n";
	  divi[b]=isPrime(num);
	  if(divi[b] ==0)
		break;
         }

	if(b>10)//got a  jam coin
        {
	  ot<<prefix;
	  // convert divi in base 2 to 10
	  for(int b=2;b<=10;b++)
  	   {
		ot<<" "<<divi[b];			
	   }
	  ot<<"\n";
          c++;		  
	}
        return;
       }
	string newPrefix=prefix+'0';
        generateNum(newPrefix, k - 1); 

	newPrefix=prefix+'1';
        generateNum(newPrefix, k - 1); 
  }
}



int main()
{
it.open("C-small-attempt0.in");
ot.open("output.out");
long int t,i,k,n,c;
it>>t;
for(k=1;k<=t;k++)
{
  it>>n>>j_global;
  ot<<"Case #"<<k<<":\n";
  generateNum("1",n-2);	
}
it.close();
ot.close();
return 0;
}
