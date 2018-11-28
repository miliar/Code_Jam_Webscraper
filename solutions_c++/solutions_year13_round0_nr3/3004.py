#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

int ans,m,n,t;
long long a,b,sa,sb;
long long i,j,k,p,q,z;//iteratr
char ch;
long long total;
long long digit,num,rev;
int isPalin(long long num)
{
	p = num;
	rev = 0;
	 do
     {
         digit = p%10;
         rev = (rev*10) + digit;
         p = p/10;
     }while (p!=0);
     if (num == rev)
	 {		
		 return 1;
	 }	
	 else
	 {
		 return 0;
	 }
}

int calc()
{	   
	total = 0;
	i = sa;
	while(i<=sb)
	{
		if(isPalin(i) == 1)
		{
			if(isPalin(i*i) == 1)
			{
				//cout << "i:"<<i<<endl;
				total++;
			}
		}
		i++;
	}
	return total;
}

int main(){
	cin >> t;
	//cout<<"Total cases:"<<t<<endl;	
    k = 1;
    while(k<=t)
    {
		cin >> a >> b;
		sa = ceil(sqrt(a));
		sb = floor(sqrt(b));
		ans = calc();
		cout << "Case #"<<k<<": "<<ans<<endl;
        k++;		
    }
	cin >> p;
    return 0;
}