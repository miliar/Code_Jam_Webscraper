#include <iostream>
#include <cstdio>
#include <set>
#include <algorithm>
using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	int case_number = 1;
	while(T--){
		int row1,row2;
		set<int> s1,s2,intersect;
		scanf("%d",&row1);
		int arr1[4][4], arr2[4][4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d", &arr1[i][j]);
			}
		}
		for(int i=0;i<4;i++){
			s1.insert(arr1[row1-1][i]);
		}

		scanf("%d",&row2);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d", &arr2[i][j]);
			}
		}
		for(int i=0;i<4;i++){
			s2.insert(arr2[row2-1][i]);
		}

		set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),std::inserter(intersect,intersect.begin()));

		int size = intersect.size();
		if(size == 0)
			printf("Case #%d: Volunteer cheated!\n", case_number);
		else if(size>1)
			printf("Case #%d: Bad magician!\n", case_number);
		else
			printf("Case #%d: %d\n", case_number,*(intersect.begin()));

		case_number++;
	}
}
