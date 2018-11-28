#include <iostream>
#include <vector>

using namespace std;

int calcNumFriends(){
	int S_Max, count=0, ans=0;
	string numPeopleString;
	vector<int> numPeople, countPeople;
	cin >> S_Max;
	cin >> numPeopleString;
	for(int i=0; i<=S_Max;i++){
		int tmpNumPeople=int(numPeopleString[i]-'0');
		count+= tmpNumPeople;
		numPeople.push_back(tmpNumPeople);
		countPeople.push_back(count);
	}
	for(int i=S_Max; i>0;i--){
		if (i-countPeople[i-1]>ans){
			ans = i-countPeople[i-1];
		}
	}
	return ans;
}

int main(){
	int T;
	cin >> T;
	for (int i=0; i<T; i++){
		cout << "Case #" <<i+1<< ": " << calcNumFriends() << endl;
	}
	return 0;
}