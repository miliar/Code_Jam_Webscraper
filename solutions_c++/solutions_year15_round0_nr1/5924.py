#include <iostream>
using namespace std;


int answer(void){
	int s;
	cin >> s;
	int count = 0;
	int friends_needed = 0;
	for (int q = 0; q < s+1;++q){
		char mander;
		cin >> mander;
		int a = (int)(mander-'0');		
		if (count < q) {friends_needed += q - count; count=q;}
		count += a;
		//printf("_ c : %i _ f : %i _ q : %i _ a :%i \n",count,friends_needed,q,a);
		}
	return friends_needed;
	}

int main(void){
	int t;
	cin >> t;
	for (int q = 0; q < t; ++q){
		printf("Case #%i: %i\n", q+1, answer());
		}
	}
