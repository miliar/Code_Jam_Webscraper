//#include <stdio.h>
//#include <math.h>
//#include <ctime>
#include <string>
//#include <vector>
#include <cstdio>
#include <iostream>
//#include <cmath>
#include <stdlib.h>

 using namespace std;
	int deg2[12];
	int P, Q;
	string str;

 int neardegree(int x)
 {
	 int i=0;
	 while (deg2[i]<=x)
		 ++i;
	 return i;
 }

 bool correct()
 {
	 int x=Q;
	 while (x>0 && !(x%2))
	 {
		 x=x/2;
	 }
	 if (x!=0)
	 {
		 if (Q/x<P)
			 return 0;
	 }
	 return 1;
 }

int main(){
	freopen("output.txt", "w", stdout);
	freopen("input.txt", "r", stdin);
	int T, t;
	scanf("%d", &T);
	for (t=1; t<=T;++t)
	{
		cin>>str;
		char buff[10];
		memset(buff, 0, sizeof(buff));
		int i , j=0;
		for (i=0; str[i]!='/'; ++i)
			buff[i]=str[i];
		P=atoi(buff);
		memset(buff, 0, sizeof(buff));
		for (++i; i<str.size(); ++i)
			buff[j++]=str[i];
		Q=atoi(buff);

		printf("Case #%d: ", t);
		int k=1;
		for (i=0; i<12; ++i)
		{
			deg2[i]=k;
			k=k*2;
		}





		if (correct())
		printf("%d\n",neardegree(Q)-neardegree(P));
		else
			printf("impossible\n");

	}
	return 0;
}