#include<vector>
#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include <set>
using namespace std;

const int N = 10;
int map1[N][N];
int map2[N][N];
int NN=4;

int main() {
//	freopen ("A-small-attempt1.in","r",stdin);
//	freopen ("out.txt","w",stdout);
	set <int> myset;
	pair<set<int>::iterator,bool> ret;
	int t;
	scanf("%d", &t);
	while (t--) {
		myset.clear();
		int n1;
		scanf("%d", &n1);
		for (int i = 0; i < NN; ++i) {
			for (int j = 0; j < NN; ++j) {
				scanf("%d", &map1[i][j]);
			}
		}
		
		for(int j=0; j<NN; j++){
			myset.insert(map1[n1-1][j]);
		}
		
		int n2;
		scanf("%d", &n2);
		for (int i = 0; i < NN; ++i) {
			for (int j = 0; j < NN; ++j) {
				scanf("%d", &map2[i][j]);
			}
		}
		
		int sum=0;
		int card=0;
		for(int j=0; j<NN; j++){
			ret = myset.insert(map2[n2-1][j]);
			if(ret.second==false){
				sum++;
				card=map2[n2-1][j];
			}
		}
		
		static int id = 0;
		if(sum==1){
			cout << "Case #"<< ++id <<": " << card <<endl;
		}
		else if (sum==0){
			cout << "Case #"<< ++id <<": " << "Volunteer cheated!" <<endl;
		}
		else if (sum>0){
			cout << "Case #"<< ++id <<": " << "Bad magician!" <<endl;
		}
		
		
	}
	return 0;
}
