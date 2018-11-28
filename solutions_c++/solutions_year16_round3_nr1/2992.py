#include <iostream>
#include <string>
#include <math.h>
#include <list>
#include <cctype>
#include <stdio.h>
using namespace std;

string calculate(int N,int P[]){
	long sumOfPi=0;
	for(int i=0;i<N;i++){
		sumOfPi+=P[i];
	}
	while(sumOfPi>0){
		int maxFirst=P[0];
		int maxSecond=P[0];
		int checkSame=P[0];
		int firstIndex=0;
		int secondIndex=0;
		int flag=1;
		int numberOfElement=0;
		for(int i=0;i<N;i++){
			if(P[i]!=checkSame){
				flag=0;
			}
			if(P[i]!=0){
				numberOfElement++;
			}
			if(P[i]>=maxFirst){
				maxSecond=maxFirst;
				secondIndex=firstIndex;
				maxFirst=P[i];
				firstIndex=i;
			}
		}
		//cout << "1="<<firstIndex << P[firstIndex]<< endl;
		//cout << "2="<<secondIndex << P[secondIndex]<<endl;
		if(firstIndex!=secondIndex ){
			if(flag==1 && numberOfElement%2!=0){
				printf("%c",firstIndex+65);
				P[firstIndex]=P[firstIndex]-1;
				printf(" ");
			}else{
				printf("%c",firstIndex+65);
				printf("%c",secondIndex+65);
				printf(" ");
				P[firstIndex]=P[firstIndex]-1;
				P[secondIndex]=P[secondIndex]-1;
			}	
		}else{
			printf("%c",firstIndex+65);
			P[firstIndex]=P[firstIndex]-1;
			printf(" ");	
		}
		sumOfPi=0;
		for(int i=0;i<N;i++){
			sumOfPi+=P[i];
		}
	}
}


int main()
{

	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);

    	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		int N;
	        cin >> N;
		int P[N];
		for(int j=0;j<N;j++){
			cin >> P[j];
		}
		cout << "Case #" << i << ": ";
		calculate(N,P);
		cout << endl;

	}


    return 0;
}
