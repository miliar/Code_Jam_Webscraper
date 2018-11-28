#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>

#include <algorithm>
#include <math.h>
#include <vector>

#include <stdio.h>
using namespace std;

int checkFair(int i){
	 int n = i;
	 int rev = 0;
	 int dig = 0;

	 while (n > 0)
	 {
		  dig = n % 10;
		  rev = rev * 10 + dig;
		  n = n / 10;
	 }

	 if( i == rev) 
		return 0;
	 else 
		 return -1;
}


int main()
{

	freopen("D://Source//C++//GCJC//Debug//C-small-attempt0.in", "rt", stdin);
	freopen("D://Source//C++//GCJC//Debug//output.txt", "wt", stdout);

	int testCases = 0;
	

	cin>>testCases;
	
	int A = 0;
	int B = 0;

	int counter = 0;

	for (int t = 0; t < testCases; t++) {
		
		cin>>A;
		cin>>B;

		counter = 0;


		for(int i = A; i <= B; i++) {
			//int squareNum = i*i;
			//if(squareNum < B) {

			//}
			double sqrtVal = sqrt(i);
			int intValue = (int)sqrtVal;

			if(intValue*1000 == (int)(sqrtVal*1000)) {
				if(checkFair(i) == 0) {
					if(checkFair(intValue) == 0)
						counter++;
				}
			}
		}

		cout<<"Case #"<<(t+1)<<": "<<counter<<endl;
	
		
	}


	return 0;
}