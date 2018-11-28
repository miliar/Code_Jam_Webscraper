#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <utility>
#include <iterator>
#include <functional>
#include <numeric>
#include <string>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <climits>
#include <cassert>
#include <algorithm>
#define debug(x) cerr<<#x<<"="<<(x)<<endl
#define ISS istringstream
#define _USE_MATH_DEFINES
#define SS stringstream

using namespace std;



template<typename T>
void printvec(vector<T> a){
	for(long long i=0;i<a.size();i++)
		cout<<a[i]<<" ";
	cout<<endl;
}

template<typename T, size_t N>
T * end(T (&ra)[N]) {
    return ra + N;
}

typedef long long ll;

int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		ll r,t;
		cin>>r>>t;
		ll result =0;
		while(true){
			t-= ((r+1)*(r+1) - (r*r));
			if(t>=0){
				result++;
				r+=2;
			}
			else
				break;
		}
		cout<<"Case #"<<i+1<<": "<<result<<endl;
	}
	return 0;
}