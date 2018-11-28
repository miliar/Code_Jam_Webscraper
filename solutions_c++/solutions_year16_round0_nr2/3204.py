#include <bits/stdc++.h>


using namespace std;

int main(){
	int test;
	string s;
	bool positive;
	int segments;
	char prev;

	cin >> test;
	for(int t = 1; t <= test; t++){
		cin >> s;
		if(s[0]=='+') positive = true;
		else positive = false;

		
		prev = s[0];
		segments = 1;
		for(int i = 1; i< s.size(); i++){
			if(s[i]!=prev){
				prev = s[i];
				segments++;
			}
		}

		if(positive) segments -= (segments%2);
		else segments -= (segments%2==0);


 	    cout << "Case #" << t << ": " << segments<< endl;
	}
	return 0;
}