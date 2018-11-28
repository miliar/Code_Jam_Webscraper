#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <cmath>
#include <algorithm>
#include <map>
#include <fstream>
#include <bitset>
#include <cstring>
#include <utility>
#include <cstdlib>
#include <climits>
#include <ctime>
 
using namespace std;

char pancake[101];

int solve(int end, char target){
	if(end == 0 && pancake[end] != target)
		return 1;
	while(end >= 0 && pancake[end] == target)
		--end;
	if(end == -1)
		return 0;
	if(target == '+'){
		while(end >= 0 && pancake[target] == '-')
			--end;
		return 1 + solve(end, '-');
	}
	else{
		while(end >= 0 && pancake[target] == '+')
			--end;
		return 1 + solve(end, '+');
	}
}
 
int main(){
	ifstream file;
	ofstream output;
	output.open("Output");
	file.open("B-small-attempt0.in");
	int t, i = 1, j;
	string s;
	file >> t;
	while(t){
		file >> s;
		j = 0;
		while(j < s.size()){
			pancake[j] = s[j];
			++j;
		}
		output << "Case #" << i << ": " << solve(j-1, '+') << endl;
		++i;
		--t;
	}
	return 0;
} 
