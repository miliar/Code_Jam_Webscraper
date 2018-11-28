#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

vector<string>names(10,"");
int loaded;

bool constructSeq(vector<int>&c, vector<int>&seq, int digit, int usedchars){
	if (usedchars == loaded) return true;
	int touse = -1;
	for (int d = digit; d < 10; d++){
		bool sufficient = true;
		for (int j = 0; j < names[d].size(); j++){
			if (c[names[d][j]] == 0){
				sufficient = false;
			}
		}
		if (sufficient){
			//printf("Trying %d\n",d);
			for (int j = 0; j < names[d].size(); j++){
				c[names[d][j]]--;
			}
			seq.push_back(d);
			if (!constructSeq(c,seq,d,usedchars+names[d].size())){
				for (int j = 0; j < names[d].size(); j++){
					c[names[d][j]]++;
				}
				seq.pop_back();
			}
			else
			{
				return true;
			}
		}
	}
	return false;

}

int main(){
	int n;
	names = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
	scanf("%d",&n);
	for (int i = 0; i < n; i++){
		vector<int>c(256,0);
		loaded = 0;
		string s;
		cin >> s;
		for (int j = 0; j < s.size(); j++){
			c[s[j]]++;
		}
		loaded = s.size();
		vector<int>answer;
		constructSeq(c,answer,0,0);
		printf("CASE #%d: ",i+1);
		for (int j = 0; j < answer.size(); j++){
			printf("%d",answer[j]);
		}
		printf("\n");
	}
}