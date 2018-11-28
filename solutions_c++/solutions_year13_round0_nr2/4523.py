#include<stdio.h>

bool ishorizontalallowed[100]; // i번째 row을 깎는게 허락되었는가?
bool isverticalallowed[100]; // i번재 col을 깎는게 허락되었는가?
int map[100][100];
bool used[100][100];
int width;
int height;

int main(){
	int tcnt;
	scanf("%d", &tcnt);

	for(int tcnti = 0; tcnti < tcnt; tcnti++){
		scanf("%d %d", &height, &width);
		
		int maxheight = 0;
		int i, j;
		for(i = 0; i < height; i++){
			for(j = 0; j < width; j++){
				scanf("%d", &map[i][j]);
				used[i][j] = false;
				if(maxheight < map[i][j])
					maxheight = map[i][j];
			}
		}

		for(i = 0; i < height; i++)
			ishorizontalallowed[i] = true;
		for(i = 0; i < width; i++)
			isverticalallowed[i] =true;

		for(i = 0; i < height; i++){
			for(j = 0; j < width; j++){
				used[i][j] = map[i][j] == maxheight ? true : false;
				if(map[i][j] == maxheight){
					ishorizontalallowed[i] = false;
					isverticalallowed[j] = false;
				}
			}
		}
		
		bool hasanswer = true;
		while(true){
			maxheight = -1;
			int maxi, maxj;
			for(i = 0; i < height; i++){
				for(j = 0; j < width; j++){
					if(used[i][j])
						continue;
					if(maxheight < map[i][j]){
						maxheight = map[i][j];
						maxi = i;
						maxj = j;
					}
				}
			}
			if(maxheight == -1)
				break;
			bool possible = true;
			for(i = 0; i < height; i++){
				for(j = 0; j < width; j++){
					if(used[i][j])
						continue;
					if(maxheight == map[i][j]){
						if(!ishorizontalallowed[i] && !isverticalallowed[j]){
							possible = false;
							break;
						}
					}
				}
				if(!possible) break;
			}
			if(!possible){
				hasanswer = false;
				break;
			}
			
			for(i = 0; i < height; i++){
				for(j = 0; j < width; j++){
					if(used[i][j])
						continue;
					if(maxheight == map[i][j]){
						ishorizontalallowed[i] = isverticalallowed[j] = false;
						used[i][j] = true;
					}
				}
			}
		}
		if(hasanswer){
			printf("Case #%d: YES\n", tcnti + 1);
		}else{
			printf("Case #%d: NO\n", tcnti + 1);
		}
	}
	return 0;
}