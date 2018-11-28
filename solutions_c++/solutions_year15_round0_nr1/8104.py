#include<iostream>
#include<vector>
#include<string>
using namespace std ;

void process_testcase(int num)
{
	int max_shyness ;
	cin>>max_shyness ;
	
	string shyness_str ;
	cin>>shyness_str ;
	vector<int> shyness ;
	shyness.resize(max_shyness+1) ;
	for(int i=0 ; i<=max_shyness ; i++) {
		shyness[i] = shyness_str.at(i)-'0';
	}

	int new_invites = 0 ;
	int cur_total = 0 ;
	for(int i=0 ; i<=max_shyness ; i++) {
		if(cur_total < i) {
			int diff = (i-cur_total) ;
			new_invites += diff ;
			cur_total += diff ;
		} 
		cur_total += shyness[i] ;
	}
	cout<<"Case #"<<num<<": "<<new_invites<<endl ;
}

int main()
{
	int num_testcases ;
	cin>>num_testcases ;

	for(int i=1 ; i<=num_testcases ; i++) {
		process_testcase(i) ;
	}
}
