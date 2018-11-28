#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

const int maxD = 1010;

int P[maxD];

int T, D, maxP;

int count(int t){
	int ans = t;
	for (int i = 0; i < D; i++){
		ans += (P[i] - 1) / t;
	}
	return ans;
}

int main(){
	ifstream inf("C:\\Users\\labud\\Desktop\\in.txt");
	ofstream outf("C:\\Users\\labud\\Desktop\\out.txt");
	inf >> T;
	int k = 1;
	while (k <= T){
		inf >> D;
		maxP = 0;
		for (int i = 0; i < D; i++){
			inf >> P[i];
			maxP = max(P[i], maxP);
		}
		int ans = maxP;
		for (int i = 1; i < maxP; i++){
			int tmp = count(i);
			ans = min(ans, tmp);
		}
		outf << "Case #" << k << ": " << ans << endl;
		k++;
	}
	inf.close();
	outf.close();
	return 0;
}