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
using namespace std;
//long long rev(long long num)
//{
//	if(num==0)
//	{
//		return 0;
//	}
//	long long mod=0;
//	while(num>0)
//	{
//		mod *= 10;
//		mod += num%10;
//		num /=10;
//	}
//	return mod;
//}

int main() {
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int test;
	long long arr[] = {1,4,9,121,484,10201,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404};
	cin >> test;
	for (int i = 1; i <= test; i++) {
		long long A,B;
		cin >> A >> B;
		int k = 0,count = 0;
		while(true){
			if(arr[k] >= A && arr[k] <= B)
				count ++;
			if(arr[k] > B)
				break;
			k ++;
		}
		cout << "Case #" << i << ": " << count <<endl;

	}
	return 0;
}
