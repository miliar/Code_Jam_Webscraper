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
char str[1010];
int T, Smax;
void eachCase(int cNum){
	int ans=0, currNum=0;
	fscanf(input, "%d%s", &Smax, str);
	for(int i=0; i<=Smax; ++i){
		if(str[i]!='0'){
			if(i>currNum){
				ans+=i-currNum;
				currNum=i+str[i]-'0';
			}
			else currNum+=str[i]-'0';
		}
	}
	fprintf(output, "Case #%d: %d\n", cNum, ans);
}

int main(){
	input=fopen("A-small-attempt0.in", "r");
	output=fopen("out.txt", "w");
	fscanf(input, "%d", &T);
	for(int i=1; i<=T; ++i)
		eachCase(i);
	return 0;
}



