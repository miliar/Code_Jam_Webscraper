//
//  A.cpp
//  CODE
//
//  Created by Vikas Yadav on 29/10/14.
//  Copyright (c) 2014 Vikas Yadav. All rights reserved.
//

#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <fstream>
#include <iterator>
#include <memory.h>
#include <cassert>

using namespace std;

typedef long long LL;

#define pb push_back
#define mp make_pair
#define gc getchar_unlocked
#define F first
#define S second
#define endl '\n'

#define PI 3.14159265

string str;

int main(){
	int tt = 1,ttt = 0;
	freopen("blarge.in", "r", stdin);
	freopen("blargeout.out", "w", stdout);
	//double st = clock();
	scanf("%d", &tt);
	while(tt--){
		int x = 0,y,z;
		cin>>str;
		printf("Case #%d: ", ++ttt);
		for(int a=1;a<str.size();a++){
			if(str[a]!=str[a-1])	x++;
		}
		if(str[str.size()-1]=='-')		x++;
		printf("%d\n", x);
	}
	//cout<<(clock()-st)/CLOCKS_PER_SEC<<endl;
	return 0;
}