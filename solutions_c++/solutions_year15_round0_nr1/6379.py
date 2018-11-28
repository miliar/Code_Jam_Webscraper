#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<string.h>
using namespace std;



int main(){
	freopen("out.txt","w",stdout);
	freopen("in.txt","r",stdin);

	int a[10000] = {0}, output,total, t,n, x;
	cin>>t;
	string s;
	
	for (int i = 0; i < t; i++) {
		total = output = 0;
		cin >> n;
		cin >> s;
		for (int j = 0; j <= n; j++) {
			a[j] = s[j]-'0';
		}
		for (int j = 0; j <=n ; j++) {
			if(j > total){
				int t1 = j - total;
				total += t1;
				output += t1;
			}
			total += a[j];
		}
		cout <<"Case #"<<i+1<<": "<< output << endl;
	}

}
