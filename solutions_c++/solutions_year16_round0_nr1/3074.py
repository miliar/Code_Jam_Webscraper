#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <string>

using namespace std;


bool check(unordered_set<int> set){
	for(int i=0;i<10;i++){
		if(set.find(i)==set.end())
			return false;
	}
	return true;
}

int main(){
	//run. ./main < in.txt > out.txt
	int TC;
	cin >> TC;
	for(int tc=1;tc<=TC;tc++){
		printf("Case #%d: ", tc);
		int n;
		cin >> n;
		if(n==0)
			cout << "INSOMNIA" <<endl;
		else{
			unordered_set<int> set;
			int j=1;
			while(!check(set)){
				string str = to_string(j*n);
				for(int k=0;k<str.length();k++){
					set.insert((int)str[k]-48);
				}
				j++;
			}
			cout << (j-1)*n << endl;
		}
		


	}

	

	return 0;
}