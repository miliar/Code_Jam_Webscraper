#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int main(){

	long long int t, k, curSum, minFriends, temp, n;
	string str;
	ifstream fin("A-large.in");
	ofstream fout("test.out");
	fin>>t;
	for(k=1;k<=t;k++){
		fin>>n;
		fin>>str;
		curSum = 0;
		minFriends = 0;
		for(long long int i = 0; i<=n; i++){
			temp = (long long int)(str[i]-'0');
			if(curSum < i){
				minFriends += i-curSum;
				curSum += i-curSum;
			}
			curSum += temp;
			//cout<<temp<<" "<<curSum<<" "<<i<<" "<<minFriends<<" - ";
		}
		fout<<"Case #"<<k<<": "<<minFriends<<"\n";
	}
	fin.close();
	fout.close();
	return 0;
}