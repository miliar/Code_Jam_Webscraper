#include <iostream>
#include <vector>
#include <string>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#define infin 2147483647
#define LLinfin 9223372036854775807
#define pb push_back
#define rs resize
#define mp make_pair
#define sz(x) int((x).size())
#define VV(x) vector<vector<x> >
#define all(x) (x).begin(), (x).end()
using namespace std;
typedef pair<int, int> PII;
typedef long long LL;

int main(){
	int tests, ans, in;
	cin>>tests;
	for(int t=1; t<=tests; t++){
		cin>>ans;
		vector<int> cards (16);
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				cin>>in;
				if(i+1 == ans) cards[in-1] = 1;
			}
		}
		cin>>ans;
		int poss = 0;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				cin>>in;
				if(i+1 == ans){
					cards[in-1]++;
					if(cards[in-1] == 2) poss++;
				}
			}
		}
		printf("Case #%d: ", t);
		if(!poss) cout<<"Volunteer cheated!"<<endl;
		else if(poss > 1) cout<<"Bad magician!"<<endl;
		else for(int i=0; i<16; i++) if(cards[i] == 2) cout<<i+1<<endl;
	}
}