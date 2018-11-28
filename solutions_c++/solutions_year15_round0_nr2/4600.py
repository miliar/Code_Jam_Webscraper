#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(std::vector<int> P,int a=0,int b=0){
	if(a!=0){
		P.push_back(a);
	}
	if(b!=0){
		P.push_back(b);
	}
	
	int result = *std::max_element(P.begin(),P.end());
	if(result<4){
		return result;
	}
	
	
	int bestSubResult = result;
	int sp = 1;
	bool flag = false;
	P.erase(std::max_element(P.begin(),P.end()));
	
	for(int i = (result%2!=0)?(int)(result/2)-1:(int)(result/2); i <= (int)(result/2); i++){
		int r = solve(P,i,result-i);
		if(bestSubResult > r){
			bestSubResult = r;
			flag = true;
		}
	}
	if(flag)
		return bestSubResult + sp;
	return bestSubResult;
}

int main(int argc, char* argv[])
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int T = 0;
	cin >> T;

	for (int x = 1; x <= T; x++) {
		cout << "Case #" << x << ": ";
		int y = 0;
		int D;
		std::vector<int> P;
		cin >> D;

		for (int i = 0; i < D; i++){
			int pi = 0;
			cin >> pi;
			P.push_back(pi);
		}
		
		y  = solve(P);
		
		cout << y << endl;
	}
	return 0;
}



