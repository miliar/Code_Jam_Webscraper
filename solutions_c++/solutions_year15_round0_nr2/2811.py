#include <cstring>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <stack>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <cmath>
#include <algorithm>
#include <stdio.h>
#include <queue>
#include <stack>
#include <cstdlib>
#include <string>
#include <ctime>
#include <bitset>
using namespace std;

FILE *input, *output;
int arr[1010], D, T;
void eachCase(int cNum){
	fscanf(input, "%d", &D);
	int larNum=0;
	for(int i=0; i<D; ++i){
		fscanf(input, "%d", arr+i);
		if(arr[i]>larNum) larNum=arr[i];
	}
	int ans=1010;
	for(int i=1; i<=larNum; ++i){
		int special=0;
		for(int j=0; j<D; ++j)
			special+=(arr[j]-1)/i;
		ans=min(ans, special+i);
	}
	fprintf(output, "Case #%d: %d\n", cNum, ans);
}
int main(){
	input=fopen("in.txt", "r");
	output=fopen("out.txt", "w");
	fscanf(input, "%d", &T);
	for(int i=1; i<=T; ++i)
		eachCase(i);
	return 0;
}



