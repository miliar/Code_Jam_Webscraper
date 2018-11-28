#include <iostream>
#include <vector>

int main()
{
	using namespace std;
	int n;
	cin >> n;
	for (int k = 0; k < n; k++){
		string c;
		cin >> c;
		vector<bool> pan;
		for ( auto s: c){
			if(s == '+'){
				pan.push_back(true);
			} else if (s == '-') {
				pan.push_back(false);
			}
		}
		bool solve = false;
		int l = pan.size();
		int flips = 0;
		while(!solve) {
			//break;
			int i = l - 1;
			int j = 0;
			while(i > -1 && pan[i]){
				i--;
			}
			if(i == -1){
				solve = true;
				continue;
			}
			flips ++;
			if(pan[0]){
				flips++;
				while(pan[j] && j < l){
					pan[j] = false;
					j++;
				}
				j = 0;	
			}
			vector<bool> temp;
			for(int t = i; t > -1; t--){
				temp.push_back(!pan[t]);
			}
			for(int t = 0; t <= i; t++){
				pan[t] = temp[t];
			}
		}
		cout << "Case #" << k + 1 << ": " << flips << endl;
	}	
}
