#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <limits.h>
#include <map>
#define MX 1000002
#define MOD 100000001
#define BASE 5.0

#include <time.h>
#include <stdlib.h>
using namespace std;

char cake[102];

unsigned long long notprime(unsigned long long N){
    if(N<2 || (!(N&1) && N!=2))
        return 0;
    for(unsigned long long i=3; i*i<=N; i+=2){
        if(!(N%i))
            return i;
    }
    return 0;
}

int main(){
	ios_base::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
    //freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    
    int t, n, j;
   // cin >> t >> n >>  j;

	cout << "Case #1:\n";

	unsigned long long num = 32769;

	unsigned long long divide[11];
	unsigned long long basenum;

	//cout << ((num >> 16-0-1)<<16-0-1);
	//cout << endl << ( num >> 15 ) % 2;

	int count = 0;
	while (count < 50){
		int i = 2;
		for (; i<=10; i++){
			basenum = 0;
			for (int j= 0; j<16; j++){
				basenum += ((num >> j) % 2) * pow((float)i, j);
			}
			unsigned long long ret = notprime(basenum);
			if (ret == 0){
				break;
			}
			else{
				divide[i] = ret;
			}
		}
		if (i == 11){
			for(int j = 15; j>=0; j--)
				cout << ((num >> j) % 2);
			cout << " ";
			for (int j = 2; j < 11; j++)
				cout << divide[j] << " ";
			cout << endl;
			count++;
		}
		num += 2;
	}
    return 0;
}