#include <iostream>
#include <string.h>
#include <stdio.h>
#include <math.h>
using namespace std;

int isPrime(long long int number){
	int flag=0;
  for(long long int i=2;i<=sqrt(number);++i)
  {
      if(number%i==0)
      {
          flag=1;
          break;
      }
  }
  if (flag==0)
	return 1;
  else
	return 0;
}


void getins(string inp){
	long long int number;
	for(int base=2;base<=10;base++){
		number=0;
		long long int mul=1;
		for(int index=17;index>=2;index--){
			if(inp[index]=='1'){
				number+=mul;
			}
			mul*=base;
		}
		for(long long int i=2;i<=number/2;i++){
			if(number%i==0){
				cout << " "<< i;
				break;
			}
		}
	}
}

int main()
{

	freopen("filtered-out.out", "r", stdin);
	freopen("final-outout.out", "w", stdout);

    	int T;
	T=100;
	int counter=0;
	cout << "Case #1:";
	cout << endl;
	for(int i=1;i<=T;i=i=i+2)
	{
	        string str;
	        cin >> str;
		cout << str.substr(2,16);
		getins(str);
		cout << endl;

	}
    return 0;
}
