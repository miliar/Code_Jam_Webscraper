#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <stdio.h>


// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
// Useful constants
#define INF                         (int)1e9
#define EPS                         1e-9
// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<b;i++)

using namespace std;
int digits[10];

int main(){

	vector<string> numbers(1000000);
	int t;
	s(t);
	int i = t;
	while(t--){
		int temp, digit, ogtemp;
		int N = 1;
		int flag = 0;
		s(temp);
		ogtemp = temp;
		if(temp == 0){
			cout << "Case #" << i-t <<": " << "INSOMNIA" << endl;
		}else{
			while(N < 200){

				while(temp > 0){
					digit = temp%10;
					digits[digit] = 1;//1 = seen else unseen
				//	numbers.at(ogtemp) = numbers.at(ogtemp) << digit <<"";
					temp/=10;
				}

				N++;
				temp = ogtemp*N;
				for(int i = 0; i < 10; i++){
					if(digits[i] == 0){
						flag++;
					}
				}
				if(flag == 0){
					for(int i = 0; i < 10; i++){
						digits[i] = 0;
					}
					break;
				}else if(N == 200){
					cout << "Case #" << i-t <<": " << "INSOMNIA" << endl;
					break;
				}
				flag = 0;
			}//testing for 200 numbers

		cout << "Case #" << i-t << ": " << (N - 1)*ogtemp << endl;
		}//else ends
	}
	return 0;
}