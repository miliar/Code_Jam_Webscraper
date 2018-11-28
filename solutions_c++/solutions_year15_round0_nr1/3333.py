#include<iostream>
#include<fstream>
#include<string>
using namespace std;

const int maxS = 1010;

string A;

int T, S;



int main(){
	ifstream inf("C:\\Users\\labud\\Desktop\\in.txt");
	ofstream outf("C:\\Users\\labud\\Desktop\\out.txt");
	inf >> T;
	int k = 1;
	while (k <= T){
		inf >> S;
		inf >> A;
		int ans = 0, now = 0;
		for (int i = 0; i <= S; i++){
			int tmp = A[i] - '0';
			if (tmp == 0)
				continue;
			if (i > now){
				ans += i - now;
				now = i;
			}
			now += tmp;
		}
		outf << "Case #" << k << ": " << ans << endl;
		k++;
	}
	inf.close();
	outf.close();
	return 0;
}