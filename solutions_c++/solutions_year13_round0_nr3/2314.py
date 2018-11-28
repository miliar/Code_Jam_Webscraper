#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

long long num[] = {
    1 , 2 , 3 , 11 , 22 ,
    101 , 111 , 121 , 202 , 212 ,
    1001 , 1111 , 2002 , 10001 , 10101 ,
    10201 , 11011 , 11111 , 11211 , 20002 ,
    20102 , 100001 , 101101 , 110011 , 111111 ,
    200002 , 1000001 , 1001001 , 1002001 , 1010101 ,
    1011101 , 1012101 , 1100011 , 1101011 , 1102011 ,
    1110111 , 1111111 , 2000002 , 2001002 ,
};

int main(){
    int t;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++){
	long long a, b; 
	int ans = 0;
	cin >> a >> b;
	//scanf("%d%d", &a, &b);
	for(int i = 0; i < 39; i++){
	    long long d = num[i] * num[i];
	    if(d >= a && d <= b)
		ans++;
	    if(d > b) break;
	}
	printf("Case #%d: %d\n",cas, ans);
    }
    return 0;
}
