#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>
#include <algorithm>
#include <cstring>
#include <math.h>
using namespace std;
int main()
{
	long long i,j,k,l,m,n,t;
    double C,F,X,sum,CPS;
    freopen("b1.in","r",stdin);
	freopen("output2.txt","w",stdout);
	cin>>t;
	for(i = 1; i <= t; i++){
		cin>>C>>F>>X;
		sum = 0.0;
		CPS = 2.0;
		while((C/CPS)+(X/(CPS+F)) < (X/CPS)){
			sum += C/CPS;
			CPS += F;
		}
		
		sum += X/CPS;
		cout<<"Case #"<<i<<": ";
		printf("%0.7lf\n",sum);
		
	}
	return 0;
}

