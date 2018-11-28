#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<vector>
#include<iostream>
#include<fstream>
#include<map>
using namespace std;
#define MP make_pair
#define REP(i, N) for(int i = 0; i<(N); i++)
#define CLR(ary) memset((ary), 0, sizeof(ary))

const int INF = 987654321;
int numC;
int L, X;
pair<char, int> table[150][150];
char Ls[10012];

int inds[4] = {'1', 'i', 'j', 'k'};
int main(){
	table['1']['1'] = MP('1', 1);table['1']['i'] = MP('i', 1);table['1']['j'] = MP('j', 1);table['1']['k'] = MP('k', 1);
	table['i']['1'] = MP('i', 1);table['i']['i'] = MP('1', -1);table['i']['j'] = MP('k', 1);table['i']['k'] = MP('j', -1);
	table['j']['1'] = MP('j', 1);table['j']['i'] = MP('k', -1);table['j']['j'] = MP('1', -1);table['j']['k'] = MP('i', 1);
	table['k']['1'] = MP('k', 1);table['k']['i'] = MP('j', 1);table['k']['j'] = MP('i', -1);table['k']['k'] = MP('1', -1);
	
	
	freopen("C-small-attempt1.in", "r", stdin);
	ofstream cout("C-small.out");
	scanf("%d", &numC);
	for(int cases = 1; cases <= numC; cases++){
		scanf("%d %d %s", &L, &X, Ls);
		bool found = false;
		string targ;
		if(L*X >= 3){
			for(int i = 0; i<X; i++)targ += Ls;
			int N = targ.size();
			//cout<<"targ = "<<targ<<endl;
			vector<pair<char, int> > pSum(targ.size());
			pSum[0].first = Ls[0];
			pSum[0].second = 1;
			for(int i = 1; i<targ.size(); i++){
				pSum[i].first = table[pSum[i-1].first][targ[i]].first;
				pSum[i].second = pSum[i-1].second * table[pSum[i-1].first][targ[i]].second;
			}
			if(pSum[N-1].first != '1' || pSum[N-1].second != -1){
				//cout<<pSum[N-1].first<<" and "<<pSum[N-1].second<<endl;
			}else{
				for(int i = 0; i<targ.size()-2 && !found; i++){
					if(pSum[i].first == 'i'){
						for(int j = i+1; j<targ.size()-1 && !found; j++){
							if(table['i']['j'].first == pSum[j].first){
								found = true;
							}
						}
					}
				}
			}
			
		}


		string ans;
		if(found)ans = "YES"; else ans = "NO";
		cout<<"Case #"<<cases<<": "<<ans<<endl;
	}
	return 0;
}
