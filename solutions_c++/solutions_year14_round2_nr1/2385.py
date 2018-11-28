#include <iostream>
#include <cstring>
#include <vector>
#include <cmath>
using namespace std;

int main (int argc, char *argv[])
{
	
	vector<vector<int> > freq;
	int TC;
	cin >> TC;
	for(int i = 0; i < TC; i++){
		int N;
		cin >> N;
		string s1, s2;
		cin >> s1 >> s2;
		bool possible = s1[0] == s2[0];
		int ans = 0;
		int index1 = 0, index2 = 0;
		while(possible){
			char c = s1[index1];
			int count1 = 0, count2 = 0;
			while(index1 < s1.length() && s1[index1] == c){
				count1++;
				index1++;
			}
			while(index2 < s2.length() && s2[index2] == c){
				count2++;
				index2++;
			}
			ans += abs(count1 - count2);
			possible = index1 < s1.length() && index2 < s2.length() && s1[index1] == s2[index2];
		}
		
		if(index1 == s1.length() && index2 == s2.length()){
			cout << "Case #" << i+1 << ": " << ans << endl;
		}else{
			cout << "Case #" << i+1 << ": " << "Fegla Won" << endl;
			
		}
	}
	return 0;
}

