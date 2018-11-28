#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

char dict[10][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};


bool is_finish(bool s[], int len){
	//printf("is_finished\n");
	for(int i=0; i<len; i++){
		if(!s[i]){
			return false;
		}
	}
	return true;
}

int sch[10] = {0, 6, 4, 2, 8, 7, 3, 5, 9, 1};

vector<int> vec;

int main(void){

	int testcase;
	scanf("%d", &testcase);

	for(int i=0; i<10; i++){
		sort(dict[i], dict[i]+strlen(dict[i]));
		//printf("%s\n", dict[i]);
	}

	for(int t_itr = 1; t_itr <= testcase; t_itr++){

		char str[2222];
		scanf("%s", str);
		int len = strlen(str);

		sort(str, str+len);

		bool visited[2222];

		for(int i=0; i<len; i++){
			visited[i] = false;
		}

		vec.clear();
		while(!is_finish(visited, len)){
			//printf("loop\n");
			bool cv[2222];
			for(int i=0; i<len; i++){
				//printf("%c(%d) ", str[i], visited[i]);
				cv[i] = visited[i];
			}
			//printf("\n");
			
			for(int i=0; i<10; i++){
				int num = sch[i];
				int numlen = strlen(dict[num]);
				//printf("%d : %d numlen\n",i, numlen);
				int idx=0;
				for(int i=0; i<len; i++){
					cv[i] = visited[i];
				}
				for(int j=0; j<len; j++){
					if(!cv[j] && idx < numlen && str[j] == dict[num][idx]){
						cv[j] = true;
						idx += 1; 
						if(idx == numlen){
							break;
						}
					}
				}
				//printf("idx numlen %d %d\n", idx, numlen);
				if(idx == numlen){
					//printf("find %d\n", num);
					for(int j=0; j<len; j++){
						visited[j] = cv[j];
					}
					vec.push_back(num);
					break;
				}
			}
		}

		printf("Case #%d: ", t_itr);
		sort(vec.begin(), vec.end());
		for(int i=0; i<vec.size(); i++){
			printf("%d", vec[i]);
		}
		printf("\n");

	}
	return 0;
}