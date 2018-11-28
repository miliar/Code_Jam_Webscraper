#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <bits/stdc++.h>
using namespace std;


int pp[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313};
vector<int> primes (pp, pp + sizeof(pp));

#define cout fout
#define cin fin

int getPrimeFactor(long long int num){
	for(int i=0; primes[i]<=sqrt(num) && i<primes.size()/sizeof(int); i++){
		if(num%primes[i] == 0)
			return primes[i];
	}

	return 0;
}

int main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT
	ofstream fout("C:\\Users\\Harry\\Desktop\\temp");
	ifstream fin("C:\\Users\\Harry\\Desktop\\C-small-attempt0.in");
	int t;
	cin>>t;
	string buff;
	getline(cin, buff);



	for(int tc = 1; tc <=t; tc++){
		int n,j;
		cin>>n>>j;
		long long int min = (1<<n-1) + 1;
		long long int max = (1<<n) - 1;
//		cout<<min << " "<< max<<" total numbers = "<< max - min<<endl;
//		cout<<"sqrt = "<<sqrt(max)<<endl;
		char str[50];
		int count=0;
//		long long int a = 2147483647;
//		int b = 11;
//		char *myStr = "1000000000001001";
//		cout<<"myoperation = "<<a%b<<" " << strtol(myStr,NULL,10) << " "<< getPrimeFactor(strtol(myStr,NULL,5)) << " " << getPrimeFactor(a)<<endl;
		cout<<"Case #"<<tc<<":"<<endl;
		for(int num = min; num<=max && count<j; num+=2){
			sprintf(str,"%d",num);
			itoa (num,str,2);
			int flag = 1;
//			cout<<str<<"\t";
			for(int base = 2; base <=10; base ++){
				long long int currNum = strtoll(str,NULL,base);
				int primeFactor = getPrimeFactor(currNum);
				if(primeFactor == 0){
					flag = 0;
					break;
				}
//				cout<<currNum<<":"<<primeFactor<<" , ";
			}

			if(flag){
				cout<<str<<" ";
				for(int base = 2; base <=10; base ++){
					long long int currNum = strtoll(str,NULL,base);
					int primeFactor = getPrimeFactor(currNum);
					cout<<primeFactor<<" ";
				}
				cout<<endl;
				count++;
			}


//			cout<<endl;

		}
//		cout<<"Case #"<<tc<<": "<< res<<endl;
	}


	fout.close();
	return 0;
}
