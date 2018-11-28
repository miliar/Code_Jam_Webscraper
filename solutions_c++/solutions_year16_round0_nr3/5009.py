#include <bits/stdc++.h>
using namespace std;
long long int i,n,arr[11],chk,save;

bool isPrime(long long int num,int base) 
{
    for(long long int lp = 2, mo = sqrt(num); lp <=mo; lp += 1) 
	{
		if(num % lp == 0)
		{
			arr[base]=lp;
			return false;
		}
	}
    return true;
}
bool convertBase(long long int a, int base)
{
	long long sum=0;
	for(int j=15; j>-1; j--)
	{
		sum = sum * base + ((a >> j) & 1);
	}
	if(base==10) save=sum;
	return !isPrime(sum,base);
}
int main() 
{	
	n=(1<<15)+1;
	printf("Case #1:\n");
	for(i=n; ; i+=2)
	{
		if(convertBase(i,2) && convertBase(i,3) && convertBase(i,4) && convertBase(i,5) && convertBase(i,6) && convertBase(i,7) && convertBase(i,8) && convertBase(i,9) && convertBase(i,10))
		{
			++chk;
			cout<<save ;
			for(int lo=2; lo<11; lo++) cout<<' '<<arr[lo];
			cout<<'\n';
		}
		
		if(chk==50) return 0;
	}
	return 0;
}