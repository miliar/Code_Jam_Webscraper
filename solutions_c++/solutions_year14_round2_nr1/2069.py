//Author : wiragotama@gmail.com
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <utility>
#include <stack>
#include <queue>
using namespace std ;
typedef long long int LL ;

//for sorting
bool asc (int i,int j) { 
	return (i<j);
}

bool dsc (int i,int j) { 
	return (i>j);
}

//main program
int main () {
	int 	t, n;
	scanf("%d",&t);
	for (int z=1; z<=t; z++) {
		scanf("%d",&n);
		string str[n];
		
		for (int i=0; i<n; i++) {
			cin >> str[i];
		}
		
		int b=0;
		int a=0;
		int result=0;
		while (b<str[0].length() && a<str[1].length() && str[0][b]==str[1][a]) {
			int count=1, count2=1;
			while (b<str[0].length() && str[0][b+1]==str[0][b]) {
				b++;
				count++;
			}	
			while (a<str[1].length() && str[1][a+1]==str[1][a]) {
				a++;
				count2++;
			}
			++a; ++b;
			result += abs(count2-count);
		}
		if (b==str[0].length() && a==str[1].length()) {
			printf("Case #%d: %d\n",z,result);
		}
		else printf ("Case #%d: Fegla Won\n",z);
		
	}
	return 0;
}

