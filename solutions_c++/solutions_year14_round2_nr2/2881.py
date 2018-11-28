#include<iostream>
#include<stdio.h>
#include<fstream>
#include<vector>
#include<algorithm>
#include<string.h>
#define MAX 10
using namespace std;
void initializeArray(int array[MAX])
{
	int i;
	for(i = 0;i < MAX;i++)
{
	array[i] = 0;
}
}
void convertToBinary(int num,int array[MAX])
{
	int i=0;
	while(num!=0)
{
	if(num%2==1)
	array[i] = 1;
	num = num/2;
	i++;
}
}
int convertToDecimal(int array[MAX])
{
	int res=0,i,num = 1;
	for(i = 0;i<MAX;i++)
{
	res = res + array[i]*num;
	num = num*2;
}
return res;
}
int main()
{
	int i,j,T,A,B,K,k;
	int arrayA[MAX],arrayB[MAX],arrayC[MAX],res,val;
	freopen("B-small-attempt0.in","r",stdin); freopen("practice_out.out","w",stdout);
	cin>>T;
	for(i = 0;i<T;i++)
{   res = 0;
	cin>>A>>B>>K;
	cout<<"Case #"<<i+1<<": ";
	for(k = 0;k<A;k++)
{   for(int l = 0;l<B;l++)
{
	initializeArray(arrayA);
	initializeArray(arrayB);
	convertToBinary(k,arrayA);
	convertToBinary(l,arrayB);
	for(j = MAX-1;j>=0;j--)
{
	arrayC[j] = arrayA[j]*arrayB[j];
}
	val = convertToDecimal(arrayC);
	//cout<<val<<" ";
	if (val<K)
	res++;
}
}
cout<<res<<endl;
}
return 0;
}
