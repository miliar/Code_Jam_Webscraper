#include <iostream>
#include <fstream>
#include <conio.h>
#include <stdio.h>
#define _USE_MATH_DEFINES
#include <algorithm>
#include <climits>
#include <bitset>
#include <math.h>
#include <string>
#include <vector>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <map>
#include <set>
using namespace std;

//bool isp(long long int a){
//	vector<int>vec;
//	while(a/10){
//		vec.push_back(a%10);
//		a/=10;
//	}
//	vec.push_back(a%10);
//	for(int i=0; i<vec.size()/2; ++i){
//		if(vec[i]!=vec[vec.size()-1-i])return false;
//	}
//	return true;
//}

long long vec[39] = {
1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004
};

int main(){
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//long long int c = 3;
	//long long curr = 1;
	//while(curr<=1E14){
	//	if(isp(curr) && isp((long long)(sqrt(1.*curr))))printf("%I64d,\n", curr);
	//	curr+=c;
	//	c+=2;
	//}
	int t;
	cin >> t;
	long long a,b;
	int n;
	for(int i=0; i<t; ++i){
		scanf("%I64d%I64d", &a,&b);
		n = upper_bound(vec,vec+39,b)-lower_bound(vec,vec+39,a);
		printf("Case #%d: %d\n", i+1,n);
	}
	return 0;
}