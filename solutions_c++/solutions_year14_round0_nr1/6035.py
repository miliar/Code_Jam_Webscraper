#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<cstdio>

using namespace std;

vector<int> cards1, cards2;
int ans1, ans2;

void getInput(){ // a case.
	cards1 = cards2 = vector<int>(16, 0);
	cin >> ans1;
	for(auto& v: cards1){
		cin >> v;
	}
	
	cin >> ans2;
	for(auto& v: cards2){
		cin >> v;
	}
	
	ans1 -= 1;
	ans2 -= 1; // 1-base to 0-base
}

string solve(){
	int sameCard = 100;
	int sameCards =  0;
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j){
			if(cards1[4*ans1 + i] == cards2[4*ans2 + j]){
				sameCards += 1;
				sameCard = cards1[4*ans1 + i];
			}
			if(sameCards > 1) return "Bad magician!";
		}
	}
	
	if(sameCards == 0) return "Volunteer cheated!";
	
	stringstream sst;
	sst << sameCard;
	string answer;
	sst >> answer;
	return answer;
}

int main(){
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output_a.txt", "w", stdout);
	int tc;
	cin >> tc;
	
	for(int i=1; i<=tc; ++i){
		getInput();
		string ans = solve();
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}





















