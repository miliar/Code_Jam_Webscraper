#include <iostream>
#include <cmath> 
#include <fstream>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

bool judge(int target){
	vector <int> v1,v2;
	while(target){
		int n = target%10;
		target = target/10;
		v1.push_back(n);
	}
	v2 = v1;
	reverse(v1.begin(), v1.end());
	if(v1 == v2) return true;
	else return false;
}
int main(){
	ifstream is("C-small-attempt0.in");
	ofstream os("C-out.txt");
	int T,k,i,A,B,A_sqr,B_sqr,count,target;

	is >> T;
	for(k = 1; k<=T;k++){
		is >> A >> B;
		A_sqr = sqrt((double)A);
		B_sqr = sqrt((double)B);
		count=0;

		for(i=A_sqr;i<=B_sqr+1;i++){
			target = i*i;
			if( target>=A && target <=B){
				if(judge(i)){
					if(judge(target)){
						count++;					
					}
				}
			}
		}
		os<<"Case #" << k << ": "<< count << endl;
	}

	return 0;
}