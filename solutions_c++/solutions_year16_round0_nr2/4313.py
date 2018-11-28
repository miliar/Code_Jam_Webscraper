#include <bits/stdc++.h>
using namespace std;
string pancakes;
void flip(int n){
	for (int i = 0; i < n; i++){
		pancakes[i] = (pancakes[i] == '-') ? '+' : '-';
	}
}
bool check(){
	for (auto c : pancakes) if (c != '+') return false;
	return true;
}
int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int cases, moves = 0; cin >> cases >> std::ws;
	for (int i = 0; i < cases; i++){
		cin >> pancakes; moves = 0;
		if (pancakes.size() == 1) moves = (pancakes[0] == '-') ? 1 : 0;
		else{
			while (!check()){
				int track = 1; char fc = pancakes[0]; bool f = false;
				while (track < pancakes.size()){
					if (pancakes[track] != fc){
						f = true;
						flip(track);
						break;
					}
					track++;
				}
				if (track == pancakes.size() && !f && !check()) flip(track);
				moves++;
			}
		}
		cout << "Case #" << (i+1) << ": " << moves << "\n";
	}
	return 0;
}