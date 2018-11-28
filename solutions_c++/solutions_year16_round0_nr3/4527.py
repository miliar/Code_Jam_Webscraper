#include <iostream>
#include <string.h>
#include <stdio.h>
#include <math.h>
using namespace std;

long long int convertToBinary(int dec){
	long long int sum=0;
	long long int rem;
	int i=1;
    do
    {
        rem=dec%2;
        sum=sum + (i*rem);
        dec=dec/2;
        i=i*10;
    }while(dec>0);
}
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
int getStatus(string inp){
	int len=inp.length();
	if(!(inp[2]=='1' && inp[17]=='1')){
		return 0;
	}
	long long int number;
	int flag=0;
	for(int base=2;base<=10;base++){
		number=0;
		int mul=1;
		for(int index=17;index>=2;index--){
			if(inp[index]=='1'){
				number+=mul;
			}
			mul*=base;
		}
		if(isPrime(number)){
			return 0;
		}
	}
return 1;	
}

void getDivisor(string inp){
	long long int number;
	for(int base=2;base<=10;base++){
		//cout << "working..." << base << " ..... "<< endl;
		number=0;
		long long int mul=1;
		for(int index=17;index>=2;index--){
			if(inp[index]=='1'){
				number+=mul;
			}
			mul*=base;
		}
		//cout << number <<  endl;
		for(long long int i=2;i<=number/2;i++){
			//cout << "inside divide " << endl;
			if(number%i==0){
				cout << " "<< i;
				break;
			}
		}
//cout << "at the end of ..." << base << " ..... "<< endl;
	}
}

int main()
{

	freopen("filtered-out.out", "r", stdin);
	freopen("final-outout.out", "w", stdout);

    	int T;
	//cin >> T;
	T=50;
	int counter=0;
	cout << "Case #1:";
	cout << endl;
	for(int i=1;i<=T;i=i++)
	{
	        string str;
	        cin >> str;
		cout << str.substr(2,16);
		getDivisor(str);
		//int result=getStatus(str);
		//if(result==1){
		//	cout << str;
		//	cout << endl;
		//}
		cout << endl;
	      	//cout << "Case #" << i << ": "<< result << endl;
		
	}
	//cout << "Counter=" << counter;


    return 0;
}
