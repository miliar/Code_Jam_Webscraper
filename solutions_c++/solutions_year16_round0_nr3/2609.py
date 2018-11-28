#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <string>
#include <cmath>

using namespace std;

int N, J;

long long int base(long long int i, int b){
	long long int sum=0;
	for(int j=0;j<N;j++){
		//cout << (i & (1<<j)) << endl;
		if(i & (1<<j))
			sum += pow(b,j);
	}
	return sum;
}

int isPrime(double num)
{
	int isprime = 0;
	for(long long int i = 2; i <= sqrt(num); i += 2)
	{
		if(i % 2 == 0)
			i++;

		if(  ((long long int)num)% i == 0)
		{
			isprime = 1;
			break;
		}
	}

	return isprime;
}

long long int factor(double num)
{
	for(long long int i = 2; i <= sqrt(num); i++)
	{
		if(((long long int)num)% i == 0)
		{
			return i;
		}
	}
}


string base2(long long int i){
	string str="";
	for(int j=N-1;j>=0;j--){
		str.append( to_string((long long int)(i/ pow(2,j))));
		i = i - (long long int)(i/ pow(2,j)) * (long long int)pow(2,j);
	}
	return str;
}


int main(){
	//run. ./main < in.txt > out.txt
	int TC;
	cin >> TC;
	for(int tc=1;tc<=TC;tc++){
		printf("Case #%d:\n", tc);
		cin >> N >> J;

		for(long long int i= (1<<(N-1))+1;i<(1<<N);i++){
			if(i%2==1){
				int b=2;
				while(b<=10){
					long long int k = base(i, b);
					//cout << "base " << b << "is " << k << endl;
					if(isPrime((double)k)==0)
						break;
					b++;
				}
				if(b==11){
					//cout << i << endl;
					cout << base2(i);
					for(int k=2;k<=10;k++){
						cout << " " << factor(base(i,k));
					}
					cout << endl;
					J--;
				}
				if(J==0)
					break;
			}
		}
	}
	return 0;
}