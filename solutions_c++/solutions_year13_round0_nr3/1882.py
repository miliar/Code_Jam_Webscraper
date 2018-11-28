#include <cstdio>
#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>

using namespace std ;


int main(void)
{
	vector<long long int> fs ;

	fs.push_back(1) ;
	fs.push_back(4) ;
	fs.push_back(9) ;
	fs.push_back(121) ;
	fs.push_back(484) ;
	fs.push_back(10201) ;
	fs.push_back(12321) ;
	fs.push_back(14641) ;
	fs.push_back(40804) ;
	fs.push_back(44944) ;
	fs.push_back(1002001) ;
	fs.push_back(1234321) ;
	fs.push_back(4008004) ;
	fs.push_back(100020001) ;
	fs.push_back(102030201) ;
	fs.push_back(104060401) ;
	fs.push_back(121242121) ;
	fs.push_back(123454321) ;
	fs.push_back(125686521) ;
	fs.push_back(400080004) ;
	fs.push_back(404090404) ;
	fs.push_back(10000200001) ;
	fs.push_back(10221412201) ;
	fs.push_back(12102420121) ;
	fs.push_back(12345654321) ;
	fs.push_back(40000800004) ;
	fs.push_back(1000002000001) ;
	fs.push_back(1002003002001) ;
	fs.push_back(1004006004001) ;
	fs.push_back(1020304030201) ;
	fs.push_back(1022325232201) ;
	fs.push_back(1024348434201) ;
	fs.push_back(1210024200121) ;
	fs.push_back(1212225222121) ;
	fs.push_back(1214428244121) ;
	fs.push_back(1232346432321) ;
	fs.push_back(1234567654321) ;
	fs.push_back(4000008000004) ;
	fs.push_back(4004009004004) ;

	int T, cases = 1 ;
	long long int A, B ;

	scanf("%d", &T) ;
	while( T-- )
	{
		scanf("%lld%lld", &A, &B) ;
		vector<long long int>::iterator i = lower_bound(fs.begin(), fs.end(), A) ;
		vector<long long int>::iterator f = upper_bound(fs.begin(), fs.end(), B) ;
		printf("Case #%d: %ld\n", cases++, f - i) ;
	}

	return 0 ;
}



