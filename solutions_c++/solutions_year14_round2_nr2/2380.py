#include <iostream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <math.h>
#include <limits.h>
#include <time.h>
#include <vector>
#include <utility>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define LIM_UI UINT_MAX
#define LIM_UL ULLONG_MAX
//iterations
#define repi(i,a,b) for(int i=a;i<=b;++i)
#define repd(i,a,b) for(int i=a;i>=b;--i)

int main(){
	ios::sync_with_stdio(false);
	int t,a,b,k;
	cin>>t;
	int c=1;
	while(c<=t){
		cin>>a>>b>>k;
		int count=0;
		for(int i=0;i<a;++i){
			for(int j=0;j<b;++j){
				int temp = i&j;
				if(temp<k){
					++count;
				}
			}
		}
		cout<<"Case #"<<c<<": "<<count<<"\n";
		++c;
	}
	return 0;
}