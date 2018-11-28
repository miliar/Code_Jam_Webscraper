#include <fstream>
#include <algorithm>

using namespace std;

const int MAX_LOOP=100;
const int MAX_T=100;

typedef __int64 ll;

int T;

bool flg[10];

void count(int x){
	//x‚Ì”Žš‚ðflg‚É’Ç‰Á
	while (x>0){
		flg[x%10]=true;
		x/=10;
	}
}

bool sat(){
	//flg‚ª‚·‚×‚Âtrue‚©
	for (int i=0;i<10;i++){
		if (!flg[i]){
			return false;
		}
	}
	return true;
}

int main(){
	ifstream fin("input.in");
	ofstream fout("output.txt");
	fin>>T;
	for (int i=0;i<T;i++){
		int N;
		fin>>N;
		if (N==0){
			fout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
			continue;
		}
		fill(flg,flg+10,false);
		int j;
		for (j=1;;j++){
			count(N*j);
			if (sat()) break;
		}
		fout<<"Case #"<<i+1<<": "<<N*j<<endl;
	}
	return 0;
}