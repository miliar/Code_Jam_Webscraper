#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <sstream>
#include <map>
#include <list>
#include <locale>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <sstream>
#include <ctime>
#include <cassert>
#include <climits>
#include <fstream>
#include <string>
using namespace std;



int main() {
	int test=0;
	cin>>test;
	int test_case=1;
	while(test--){
		
		long long int A,B,K;
		cin>>A;
		cin>>B;
		cin>>K;
		long long int count=0;
		for(long long int i=0;i<A;i++){
			for(long long int j=0;j<B;j++){
				if((i&j)<K)
					count++;
			}
		}
		cout<<"Case #"<<test_case<<": "<<count<<endl;
		test_case++;
	}
}