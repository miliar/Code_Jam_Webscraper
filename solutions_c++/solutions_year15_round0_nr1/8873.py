#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std ; 
ifstream fin("A-large.in")	;	
ofstream fout("A-large.out")	;	
long long t , n , temp , l  = 0 ; 
string input ; 


int main()

{
	ios_base::sync_with_stdio(0)	;	
	fin>>t ; 
	vector<long long> nums  ; 
	while(t)
	{
		l++ ; 
		nums.clear() ; 
		fin>>n  ;
		fin>>input ; 
		for (long long i = 0; i < n+1; ++i)
		{
			for (long long j = 0; j < input[i] - '0'; ++j)
			{
				nums.push_back(i) ; 
			}
		}
		
		std::sort(nums.begin() , nums.end()) ; 
		long long res = 0 ;
		long long stoodUps = 0 ; 
		for (long long i = 0; i < n; ++i)
		{
			if (stoodUps >= nums[i])
			{
				stoodUps++ ; 
			}
			else{
				res += (nums[i] - stoodUps) ;
				stoodUps = nums[i]+1 ; 
			}
		}
		fout<<"Case #"<<l<<": "<<res<<endl ; 

		t-- ; 
	}


	return 0 ; 
}