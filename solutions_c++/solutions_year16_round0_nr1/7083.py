#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <stdio.h> 

using namespace std;


long long CalculateLast(long long iStart)
{
	long long iRes = 0, aa, tri;
	int a[100], temp;
	for(int i=0;i<=10;i++)
		a[i] = 0;
	int iCount = 0;
	for(tri=1; ;tri++)
	{
		aa = iStart*tri;
		do{
			temp = aa%10;
			if(a[temp] == 0){
				a[temp] = 1;
				++iCount;
			}
			aa /= 10;
    		}while(aa);
		if(iCount == 10)break;
	}
	
	return (tri*iStart);
}



int main()
{
	int t;
	long long n, res;
	//freopen("input1.txt","r", stdin);
	//freopen("output1.txt", "w", stdout);	
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		if(n == 0)
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else
			cout<<"Case #"<<i<<": "<<CalculateLast(n)<<endl;
	}
	return 0;
}




