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
#define vv(x) vector<vector<x> >
#define all(x) (x).begin(), (x).end()
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;

int main(){
	int tests;
	cin>>tests;
	for(int t=1; t<=tests; t++){
		printf("Case #%d: ", t);
		int a, b, k;
		cin>>a>>b>>k;
		int svar = 0;
		for(int i=0; i<a; i++){
			for(int j=0; j<b; j++){
				if((i&j) < k) svar++;
			}
		}
		cout<<svar<<endl;
	}
}