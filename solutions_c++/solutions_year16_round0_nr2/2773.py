#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <string>
#include <fstream>
#include <streambuf>

using namespace std;


string s;
int pd[101][2];
int func(int at,int f){
	if(at == s.size())
		return (f);
	if(pd[at][f]!=-1)
		return pd[at][f];
	int ans = 1000000000;
	if(s[at] == '+'){
		if(!f){
			ans = min(func(at+1,!f)+1,func(at+1,f));
		}else{
			ans = func(at+1,0)+1;
		}
	}else{
		if(!f){
			ans = func(at+1,1)+1;
		}else{
			ans = min(func(at+1,!f)+1,func(at+1,f));
		}
	}
	return pd[at][f] = ans;
}

int main(){


	int t,ca = 1;
	cin>>t;
	while(t--){
		printf("Case #%d: ",ca++);
		cin>>s;
		memset(pd,-1,sizeof pd);
		cout<<min(func(0,0),func(0,1))<<endl;
	}

	return 0;
}