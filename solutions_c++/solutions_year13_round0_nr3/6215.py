#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

#define SIZE 1001

bool fair[SIZE];
bool square[SIZE];
bool fsq[SIZE];

int count[SIZE];


int main() {
	int num[5];
	
	memset(fair, 0, sizeof fair);
	memset(square, 0, sizeof square);
	memset(fsq, 0, sizeof fsq);
	memset(count, 0, sizeof count);
	
	for(int i = 1; i <= 1000; i++) {
		int n = i;
		memset(num, 0, sizeof num);
		
		int nc = 1;
		
		num[nc - 1] = n % 10;
		n /= 10;
		
		if(n) nc++;
		else goto hi;
		
		num[nc - 1] = n % 10;
		n /= 10;
		
		if(n) nc++;
		else goto hi;
		
		num[nc - 1] = n % 10;
		n /= 10;
		
		if(n) nc++;
		else goto hi;
		
		num[nc - 1] = n % 10;
		n /= 10;
		
		if(n) nc++;
		else goto hi;
		
		hi:
		
		//cout << num[3] << num[2] << num[1] << num[0] << " " << nc << endl;
		
		if(nc == 1) fair[i] = true;
		else if(nc == 2) fair[i] = num[0] == num[1];
		else if(nc == 3) fair[i] = num[0] == num[2];
		
		if(fair[i] && (i * i <= 1000)) square[i * i] = true;
	}
	
	for(int i = 1; i <= 1000; i++) {
		fsq[i] = fair[i] && square[i];
		
		if(fsq[i]) {
			for(int j = i; j <= 1000; j++)
				count[j]++;
		}
	}
	
	
	int T;
	cin >> T;
	
	for(int c = 1; c <= T; c++) {
		int a, b;
		
		cin >> a >> b;
		
		cout << "Case #" << c << ": " << count[b] - count[a - 1] << endl;
	}
}
