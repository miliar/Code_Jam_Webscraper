#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>
#include <limits.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <functional>
#include <vector>
#include <numeric>
#include <deque>
#include <bitset>
#include <iostream>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		lint x;
		cin >> x;
		printf("Case #%d: ",i);
		if(x == 0){
			cout << "INSOMNIA" << endl;
			continue;
		}
		set<int> s;
		for(lint j=x; j; j/=10){
			s.insert(j%10);
		}
		lint p = x;
		while(s.size() != 10){
			p += x;
			for(lint j=p; j; j/=10){
				s.insert(j%10);
			}
		}
		cout << p << endl;
	}
}