#include<iostream>
#include<string>
#include<cstdlib>
#include<cstring>
#include<iomanip>
#include<vector>
using namespace std;

/* http://www.programminglogic.com/using-the-built-in-sort-and-search-functions-in-c/
Just keep in mind that the function needs to return a negative number if the first element
is smaller than the second, zero in case they are equal, and a positive number in case the 
first element is greater than the second. The arguments the function take are pointers to 
void, so you need to cast them inside the function as well.*/

int compare (const void *elem1, const void *elem2)
{
    double d = (*(double*)elem1 - *(double*)elem2);
	if(d<0) return -1;
	if(d>0) return +1;
	return 0;
}

int main()
{
	double N[15],K[15];   //for Naomi and Ken
	int cases,n,i,j,naomi,ken;
	int ans1,ans2,index;
	
	int ns,ne,ks,ke;
	cin>>cases;
	index=1;
	while(cases--)
	{
	
	cin>>n;
	for(i=0 ; i<n ; ++i)
		cin>>N[i];
	for(i=0 ; i<n ; ++i)
		cin>>K[i];
	naomi = 0; ken = 0;
	qsort(N,n,sizeof(double),compare);     //uses cstdlib
	qsort(K,n,sizeof(double),compare); 
	std::cout<<setprecision(3)<<fixed;
	
	i=0; j=0;	
	while(i<n && j<n)
	{
		if(N[i]<K[j])
		{
			ken++;
			i++; j++;
		}
		else//N[i]>K[j]
		{
			j++;
			naomi++;
		}
	}
	ans1 = naomi;
	
	naomi = 0; ken = 0;
	ns=0; ks=0; ne=n-1; ke=n-1; 
	
	while(ns<=ne && ks<=ke)
	{
		if(N[ns]<K[ks])
		{
			ken++;
			ns++;
			ke--;
		}
		else
		{
			naomi++;
			ns++;
			ks++;
		}	
	}
	ans2 = naomi;
	
	cout<<"Case #"<<index++<<": "<<ans2<<" "<<ans1<<"\n";
	}
	
	return 0;
}