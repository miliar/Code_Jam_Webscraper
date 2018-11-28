#include <iostream>
#include <stdio.h>
#include <vector>
#include <memory>
#include <unordered_map>
#include <algorithm>
#include <string>

using namespace std;
using namespace std::string_literals;
namespace std
{
	template<typename C, typename V> auto find(C &Container, const V &Value) { return std::find(begin(Container), end(Container), Value); }
	template<typename C, typename P> auto find_if(C &Container, P Pred) { return std::find_if(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto find_if_not(C &Container, P Pred) { return std::find_if_not(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto all_of(C &Container, P Pred) { return std::all_of(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto any_of(C &Container, P Pred) { return std::any_of(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto none_of(C &Container, P Pred) { return std::none_of(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto count_if(const C &Container, P Pred) { return std::none_of(cbegin(Container), cend(Container), Pred); }
	template<typename C, typename V, typename P> auto lower_bound(C &Container, const V &Val, P Pred) { return std::lower_bound(begin(Container), end(Container), Val, Pred); }
	template<typename C, typename V, typename P> auto upper_bound(C &Container, const V &Val, P Pred) {	return std::lower_bound(begin(Container), end(Container), Val, Pred); }
	template<typename C, typename P> auto remove_if(C &Container, P Pred) {	return std::remove_if(begin(Container), end(Container), Pred); }
	template<typename C, typename P> auto generate(C &Container, P Pred) { return std::generate(begin(Container), end(Container), Pred); }
}

void Solve(int tc)
{
	string s;
	cin >> s;
	int64_t counts['Z'+1]= {};
	for(int i='A'; i<='Z'; ++i)
	{
		counts[i]=count(s.begin(), s.end(), i);
	}
	int64_t num_counts[10]= {};
	num_counts[0]=counts['Z'];
	num_counts[2]=counts['W'];
	num_counts[6]=counts['X'];
//	num_counts[7]=counts['V'];
	num_counts[8]=counts['G'];
	num_counts[3]=counts['H']-num_counts[8];
	num_counts[4]=counts['U'];
	num_counts[5]=counts['F']-num_counts[4];
	num_counts[9]=counts['I']-(num_counts[8]+num_counts[6]+num_counts[5]);
	num_counts[1]=counts['O']-(num_counts[0]+num_counts[4]+num_counts[2]);
	num_counts[7]=counts['V']-num_counts[5];
	int l=0;
	for(int i=0; i<=9; ++i)
	{
		l+=num_counts[i];
	}
	std::vector<char> result;
	result.resize(l+1,0);
	char *p=result.data();
	for(int i=0; i<=9; ++i)
	{
		if(num_counts[i])
		{
			std::fill(p, p+num_counts[i], '0'+i);
			p+=num_counts[i];
		}
	}
	printf("Case #%d: %s\n", tc, result.data() );
}

int main()
{
	int t;
	cin >> t;
	for(int tc=1; tc<=t; ++tc)
	{
		Solve(tc);
	}
}