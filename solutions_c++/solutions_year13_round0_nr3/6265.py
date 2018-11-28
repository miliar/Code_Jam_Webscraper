#include <cstdio>
#include <iostream>
#include <math.h>
using namespace std;

//#define MAX_SIZE 100

int isPalindrome(int x) {
	int a[4];
	int k=0, length=0;
	for(int m=0; m<4; m++)
		a[m]=-1;
	int temp=x;
	do {
		int d = temp%10;
		a[k++] = d;
		temp = temp/10;
	} while(temp>0);
	if(x<10)
		return 1;
	else {
		for(int m=0; m<4; m++)
			if(a[m]!=-1) length++;
		int left=0;
		int right = length-1;
		while(left<right) {
			if(a[left]!=a[right]) {
				return 0;
			}
			left++;
			right--;
		}
	}
	return 1;
}


int main() {
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small-attempt0.out", "wt", stdout);

	int T;
	cin>>T;

	for(int i=1; i<=T; i++) {
		int lb, ub, count=0;
		cin>>lb>>ub;
		for(int j=lb; j<=ub; j++) {
			bool pa=false, sq=false; 
			if(isPalindrome(j)) pa=true;
			int min = 0, max = 1000;
			int answer = 0;
			int test = 0;
			while(1) {
				test = (min + max) / 2;
				answer = test * test;
				if(j > answer) 
					min = test;
				else if(j < answer)
					max = test;
				if(j == answer) {
					//printf("%d is a perfect square of %d\n", j, test);
					if(isPalindrome(test))
						sq=true;
					break;
				}
				if((max - min) <= 1)
					break;
			}
			if(pa==true && sq==true) count++;
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
}