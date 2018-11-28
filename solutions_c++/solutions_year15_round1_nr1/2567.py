#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <vector>
using namespace std;

int main(){
	ifstream in("A-large.in");
	ofstream out("output.out");
	int t, m, n;
	int count1, count2;
	vector<int> vec;
	in>>t;
	for(int i = 0; i< t; i++){
		count1 = 0; 
		count2 = 0;
		int localmax = INT_MIN; 
		in>> n;
		for(int j = 0; j< n; j++){
			in>>m;
			vec.push_back(m);
		}
		for(int j = 1; j< n ;j++){
			if(vec[j] < vec[j-1]){
				count1 += vec[j-1]-vec[j];
			}
			localmax = max(localmax, vec[j-1]-vec[j]);
		}
		for(int j = 0; j< n-1; j++){
			if(vec[j]< localmax){
				count2+= vec[j];
			}else{
				count2+= localmax;
			}
		}
		vec.clear();
		//cout<<"Case #"<<i+1<<": "<<count1<<" "<<count2<<endl;
		out<<"Case #"<<i+1<<": "<<count1<<" "<<count2<<endl;
	}

	in.close();
	out.close();
	return 0;
}