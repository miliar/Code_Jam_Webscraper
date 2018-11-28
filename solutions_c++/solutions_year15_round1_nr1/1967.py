#include<vector>
#include<map>
#include<algorithm>
#include<iostream>
#include<queue>
#include<cstring>
using namespace std;

int ret = 0;
long m, N, T, y,z,curr,bigdrop;
vector<long> v;
int main(){
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cin >> N; y=0;z=0;curr=0;v.clear();bigdrop=0;
		for (int i = 0; i < N; ++i){
			cin >> m;
			//1
			if (m < curr) y=y+(curr-m);

			//2
			v.push_back(m);
			if (curr-m>bigdrop) bigdrop=curr-m;
			curr=m;
		};
		//2
		bigdrop;
		for (int i = 0; i < N-1; ++i){
                   z=z+min(v[i],bigdrop);
		};
            cout << "Case #" << t+1 << ": " << y << " " << z << endl;
	};
};
