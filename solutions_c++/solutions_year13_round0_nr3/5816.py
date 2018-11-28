
#include <cstdio>
#include <iostream>
#include <cmath>
#include <math.h>
using namespace std;

#define SMALL
//#define LARGE
int x,y;

int solve(int a,int b) {
	int count = 0;
	int check[3] = {0,0,0};
	int sCheck[3] = {0,0,0};
	for(int i=a;i<=b;i++)
	{
		int tempCount=0;
		double result,Sresult;
		int checkResult,checkSResult;

		double temp = log10((double)i);
		int p = (int)temp;
		check[2] = i/100;
		check[1] = (i%100)/10;
		check[0] = i%10;		
		result = sqrt((double)i);		
		checkResult = (int)sqrt((double)i);

		sCheck[2] = checkResult/100;
		sCheck[1] = (checkResult%100)/10;
		sCheck[0] = checkResult%10;	

		int Stemp = (int)log10(result);
		if(Stemp == 0)
			{
				tempCount+=1;
			}else if(Stemp == 1)
			{
				if(sCheck[0] == sCheck[1])
				{
					tempCount+=1;
				}
			}else if(Stemp==2)
			{
				if(sCheck[0] == sCheck[2])
				{
					tempCount+=1;
				}
			}
		if(result == checkResult && tempCount == 1)
		{
			if(p == 0)
			{
				count+=1;
			}else if(p == 1)
			{
				if(check[0] == check[1])
				{
					count+=1;
				}
			}else if(p==2)
			{
				if(check[0] == check[2])
				{
					count+=1;
				}
			}
		}
	}
	return count;
}

int main() {
	freopen("A-sample.in", "rt", stdin);
	#ifdef SMALL
		freopen("C-small-attempt0.in", "rt", stdin);
		freopen("C-small-attempt0.out", "wt", stdout);
	#endif
	#ifdef LARGE
		freopen("A-large-practice.in", "rt", stdin);
		freopen("A-large-practice.out", "wt", stdout);
	#endif

	int T;					//The number of test cases
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cin>>x>>y;
		cout << "Case #" << i << ": ";
		cout << solve(x,y);
		cout << endl;
	}
	
	return 0;
}