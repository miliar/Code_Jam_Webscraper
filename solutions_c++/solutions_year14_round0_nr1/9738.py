#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	int cases = 0;
	scanf("%d", &cases);
	for(int cas = 0; cas < cases; cas++){
		printf("Case #%d: ", cas + 1);
		int chosen1 = 0;
		scanf("%d", &chosen1);
		vector<vector<int> > v1(4, vector<int> (4, -1));
		for(int i = 0; i< 4; i++){
			for(int j = 0; j < 4; j++){
				scanf("%d", &v1[i][j]);
			}
		}
		int chosen2 = 0;
		scanf("%d", &chosen2);
		vector<vector<int> > v2(4, vector<int> (4, -1));
		for(int i = 0; i< 4; i++){
			for(int j = 0; j < 4; j++){
				scanf("%d", &v2[i][j]);
			}
		}

		vector<int> row1 = v1[chosen1 - 1];
		vector<int> row2 = v2[chosen2 - 1];
		sort(row1.begin(), row1.end());
		sort(row2.begin(), row2.end());
		vector<int> result(8, 0);
		auto it = set_intersection(row1.begin(), row1.end(), row2.begin(), row2.end(), result.begin());
		result.resize(it - result.begin());
		if(result.size() == 1){
			printf("%d\n", result[0]);
		}
		else if(result.size() == 0){
			printf("Volunteer cheated!\n");
		}
		else{
			printf("Bad magician!\n");						
		}		
	}
	return 0;
}
