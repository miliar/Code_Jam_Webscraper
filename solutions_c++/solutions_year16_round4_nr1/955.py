#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <utility>
#include <iostream>
using namespace std;
int wow[5000];
vector<int> res;
int X;
bool ok = 0;

int adu(int a,int b){
	//cout<<a<<" "<<b<<endl;
	if (a == b) return -1;
	if (a == 'R' && b == 'P') return 'P';
	if (a == 'R' && b == 'S') return 'R';
	if (a == 'P' && b == 'R') return 'P';
	if (a == 'P' && b == 'S') return 'S';
	if (a == 'S' && b == 'R') return 'R';
	if (a == 'S' && b == 'P') return 'S';
	return -1;
}

bool check(){
	int bz = X;
	int c = 0;
	int tourn[33][33];
	for (int i=0;i<X;i++)
		tourn[0][i] = res[i];
	//cout<<"XX"<<endl;
	while (bz != 1){
		bz/=2;
		for (int i=0;i<bz;i++){
		//	cout<<bz<<" "<<i<<endl;
			int haha = adu(tourn[c][i*2], tourn[c][i*2 + 1]);
			//cout<<haha<<endl;
		//	cout<<bz<<" "<<i<<endl;
			tourn[c+1][i] = haha;
			if (haha == -1)
				return 0;

		}
		c++;
	}
	return 1;
}

int main() {
	int T = 0;
	int tt = 1;
	scanf("%d",&T);
	
	
	while (T--){
		printf("Case #%d: ",tt++);
		int N,R,P,S;
		char a,b,c;
		scanf("%d%d%d%d",&N,&R,&P,&S);
		X = R + P + S;
		res.clear();
		ok = 0;
		for (int i=0;i<P;i++)
			res.push_back('P');
		for (int i=0;i<R;i++)
			res.push_back('R');
		for (int i=0;i<S;i++)
			res.push_back('S');
		//cout<<"AAA"<<endl;
		ok = check();
		//cout<<"AAA"<<endl;
		if (!ok)
		while (next_permutation(res.begin(),res.end())) {
			//cout<<"TEST"<<endl;
			ok = check();
			if (ok)
				break;
		}
		if (ok){
			for (int i=0;i<res.size();i++)
				printf("%c",res[i]);
			printf("\n");
		} else printf("IMPOSSIBLE\n");


		}
}