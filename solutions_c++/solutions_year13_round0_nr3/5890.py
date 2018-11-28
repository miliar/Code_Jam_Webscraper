#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <sstream>
using namespace std;

vector<int> num(1010,0);

bool isPalin(int i) {
	stringstream ss;
	ss << i;
	string str = ss.str();	
	string str1= str;
        reverse(str.begin(),str.end());
	return(str1 == str)?true:false; 
}

int func(int a,int b) {
int ans = num[b]-num[a];
	if (num[a]!=num[a-1])ans++;
	return ans;
}
void precompute() {
	for (int i=1;i<40;i++){
		if (isPalin(i)) {
			if (isPalin(i*i)) {
				num[i*i]=1;
			}
		}
	}
	for(int i=0;i<num.size();i++) {
		num[i]=num[i-1]+num[i];
	}
}
int main() {
	precompute();
	int t;
	cin >> t;
	vector<vector<int> > vec(t,vector<int>(2,0));
	for (int i=0;i<t;i++){
		cin >> vec[i][0];
		cin >> vec[i][1];
	}

	for(int i=0;i<vec.size();i++){
		int ams = func(vec[i][0],vec[i][1]);
		printf("Case #%d: %d\n",i+1,ams);
	}
	return 0;
}
