#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<fstream>
using namespace std;
void sort(long double A[1001],int n)
{
int i,j;
long double temp;
for(i=0;i<n;i++){
for(j=0;j<n;j++){
if(A[i]<A[j]){
temp=A[i];
A[i]=A[j];
A[j]=temp;
}
}
}
}


int compare (const void * a, const void * b)
{
  if(*(long double*)a > *(long double*)b )
return 1;
 if(*(long double*)a < *(long double*)b )
return -1;
 if(*(long double*)a == *(long double*)b )
return 0;
}
int main()
{
int T,i,j,k,n,lowerBoundN,upperBoundN,lowerBoundK,upperBoundK,wScore[1000],dwScore[1000],ws,dws;
long double N[1001],K[1001];

ifstream fin("D-large.in");
fin>>T;
for(i=0;i<T;i++)
{
	fin>>n;
	for(j=0;j<n;j++)
		fin>>N[j];
	for(j=0;j<n;j++)
		fin>>K[j];
	//sort(N,n);
	//sort(K,n);
	qsort (N, n, sizeof(long double), compare);
	qsort (K, n, sizeof(long double), compare);
	cout<<endl;	
	/*for(j=0;j<n;j++)
		cout<<N[j]<<" ";
	cout<<endl;
	for(j=0;j<n;j++)
		cout<<K[j]<<" ";
	cout<<endl;*/

	lowerBoundN=0;
	lowerBoundK=0;
	upperBoundN=n-1;
	upperBoundK=n-1;
	ws=0;
	dws=0;

/*Normal War*/
	while(lowerBoundN<=upperBoundN)
	{
		if(N[upperBoundN]>K[upperBoundK])
		{
			upperBoundN--;
			lowerBoundK++;
			ws++;
		}
		else
		{
			upperBoundN--;
			upperBoundK--;
		}
	}

	lowerBoundN=0;
	lowerBoundK=0;
	upperBoundN=n-1;
	upperBoundK=n-1;
/*Deceitful War*/
	while(lowerBoundN<=upperBoundN)
	{//cout<<N[upperBoundN]<<" "<<K[upperBoundK]<<endl;
		if(N[upperBoundN]<K[upperBoundK])
		{
			upperBoundK--;
			lowerBoundN++;
			
		}
		else
		{
			upperBoundN--;
			upperBoundK--;
			dws++;
		}
	}

wScore[i]=ws;
dwScore[i]=dws;
}

for(i=1;i<=T;i++){
cout<<"Case #"<<i<<": ";
printf("%d %d",dwScore[i-1],wScore[i-1]);
cout<<endl;
}
return 0;
}
