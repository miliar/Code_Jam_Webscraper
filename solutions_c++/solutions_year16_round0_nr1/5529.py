#include <iostream>
#include <stdio.h>
using namespace std;

int calculate(int number){
	if(number ==0){
		return -1;
	}
	int countSize=0;
	int flags[10]={0};
	int count=1;
	int currentNumber,testNumber;
	while(count<=150000){
		currentNumber=count*number;
		testNumber=currentNumber;
		while(testNumber>0){
			int digit=testNumber%10;
			testNumber=testNumber/10;
			if(flags[digit]==0){
				flags[digit]=1;
				countSize++;
			}
		}
		if(countSize>=10){
			return currentNumber;
		}
		count++;
		if(count==150000){
			return -1;
		}
	}
}


int main()
{

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

    	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
	        int number;
	        cin >> number;
		int result=calculate(number);
		if(result==-1){
			cout << "Case #" << i << ": "<< "INSOMNIA" << endl;
		}else{
	      		cout << "Case #" << i << ": "<< result << endl;
		}
	}


    return 0;
}
