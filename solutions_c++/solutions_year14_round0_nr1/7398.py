#include <iostream>
#include <set>
using namespace std;
int mm[4][4];
int mm2[4][4];
set<int> myset;

int main()
{
	int cnt;
	cin>>cnt;
	int idx = 1;
	for(;idx<=cnt;++idx){
		int a1,a2;
		cin>>a1;
		--a1;
		for(int i =0;i < 4; ++i){
			for(int j=0; j<4; ++j){
				cin>>mm[i][j];
			}
		}
		cin>>a2;
		--a2;
		for(int i =0;i < 4; ++i){
			for(int j=0; j<4; ++j){
				cin>>mm2[i][j];
			}
		}
		int ans = -1;
		int flag = 0;
		myset.clear();
		for(int i=0; i<4; ++i){
			myset.insert(mm2[a2][i]);
		}
		for(int i=0; i<4; ++i){
			if(myset.find(mm[a1][i]) != myset.end()){
				++flag;
				ans = mm[a1][i];
			}
		}
		printf("Case #%d: ",idx);
		if(flag == 0){
			printf("Volunteer cheated!");
		}
		if(flag == 1){
			printf("%d", ans);
		}
		if(flag > 1){
			printf("Bad magician!");
		}
		printf("\n");

	}
	return 0;
}
