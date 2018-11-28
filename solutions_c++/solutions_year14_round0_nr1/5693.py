#include <cstdio>
#include <vector>
using namespace std;

const char *badMagician = "Bad magician!";
const char *cheater = "Volunteer cheated!";
int answerX,answerY;
int ans; // problem answer
void debug(const std::vector<int> v){
	for(int i =0;i < v.size(); i++){
		printf("%d ",v[i]);
	}
	printf("\n");
}

void read(int cas){

	scanf("%d",&answerX);
	vector<int> init;
	for(int i = 1;i <= 4; i++){
		for(int j =1;j <= 4; j++){
			int x;
			scanf("%d",&x);
			if(i == answerX)
				init.push_back(x);

		}
	}
	vector<int> changes;
	scanf("%d",&answerY);
	for(int i = 1;i <= 4; i++){
		for(int j =1;j <= 4; j++){
			int x;
			scanf("%d",&x);
			if(i == answerY){
				changes.push_back(x);
			}
		}
	}

	vector<int> difference;
	for(int i =0 ; i < changes.size(); i++){
		bool isIn = false;
		for(int j =0; j< init.size(); j++){
			if(changes[i] == init[j]){
				isIn = true;
				break;
			}
		}
		if(isIn == true)
		difference.push_back(changes[i]);
	}
	if(difference.size() == 1){
		printf("Case #%d: %d",cas, difference[0]);
	}else{
		if(difference.size() > 1){
			printf("Case #%d: %s",cas, badMagician);
		}else{
			if(difference.size() == 0){
				printf("Case #%d: %s",cas, cheater);
			}
		}
	}

}

int main(){
	int T;
	scanf("%d",&T);
	for(int i =0 ; i < T ; i++){
		
		read(i+1);
		printf("\n");
	}
	return 0;
}