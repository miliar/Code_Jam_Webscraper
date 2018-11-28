//sample_war.cc

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>

using namespace std;

int fairWar( vector<double> v1, vector<double> v2 ){
	int points = 0;
	int n = v1.size();
	if(v1.size() == 1){
		if (v1[0] > v2[0] ){
			points = points + 1;
			return points;
		}
	}
	else{
		int flag = 0;
		points = 0;
		while(v1.size() > 0){
			double k = v1[0];
			for(int i = 0; i < v2.size(); i++){
				if(v2[i] > k){
					v1.erase( v1.begin() );
					v2.erase( v2.begin()+i );
					break;
				}
				else{
					flag = flag + 1;
				}
			}
		if(flag == n){
			v1.erase(v1.begin());
			auto minimum = *std::min_element( v2.begin(), v2.end() );
			v2.erase(std::distance(std::begin(v2),minimum));
		}
	} 
	}
	return 0;
}

int main(){
	vector<double> v1 {0.5,0.1,0.9};
	vector<double> v2 {0.6,0.4,0.3};
	cout << "points: " << fairWar(v1,v2) << endl;
	return 0;
}
