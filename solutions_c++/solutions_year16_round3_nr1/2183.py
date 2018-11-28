/*
 * A.cpp
 *
 *  Created on: 11 Apr 2016
 *      Author: xing
 */


#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define DEBUG

int num[27];

bool compare(pair<int, int> a, pair<int, int> b){
	return a.second < b.second;
}

void solve(int index){
	int N, sum = 0;

	vector< pair<int, int> > nums;
	cin>>N;

	memset(num, 0, sizeof(num));



	for(int i = 0;i<N;i++){
		int count;
		cin >> count;
		num[i] = count;
		sum += count;
		nums.push_back( pair<int, int>(i, count) );
	}

	cout<<"Case #"<<index<<":";

	if(N == 2){

		for(int i = 0;2*i<sum;i++){
			cout<<" AB";
		}
		cout<<endl;
		return;

	}

	std::make_heap(nums.begin(),nums.end(), compare);

	pair<int, int> first, second, third;

	first = nums.front();
	std::pop_heap(nums.begin(),nums.end(), compare);nums.pop_back();

	second = nums.front();
	std::pop_heap(nums.begin(),nums.end(), compare);nums.pop_back();

	for(int i = 0;i<(first.second - second.second)/2;i++){
		cout<<" "<<(char)('A'+first.first)<<(char)('A'+first.first);
	}
	if( (first.second - second.second)%2 == 1 ){
		cout<<" "<<(char)('A'+first.first);
	}
	first.second = second.second;

	while(nums.size()){
		third = nums.front();
		std::pop_heap(nums.begin(),nums.end(), compare);nums.pop_back();

		for(int i = 0;i<first.second - third.second;i++){
			cout<<" "<<(char)('A'+first.first)<<(char)('A'+second.first);
		}
		first.second = third.second;
		second.second = third.second;

		for(int i = 0;i<first.second/2;i++){
			cout<<" "<<(char)('A'+first.first)<<(char)('A'+first.first);
		}
		if(first.second%2 == 1){
			cout<<" "<<(char)('A'+first.first);
		}

		first = second;
		second = third;
	}

	for(int i = 0;i<first.second;i++){
		cout<<" "<<(char)('A'+first.first)<<(char)('A'+second.first);
	}
	cout<<endl;




	//cout<<"Case #"<<index<<": "<<endl;
}

int main(){
	int T;

	cin>>T;

	for(int i = 0;i<T;i++){
		solve(i+1);
	}

}
