#include <stdio.h>

bool is_stupid(int field[][4], int arr[]){
	int i,j;
	int count=0;
	for(i=0; i<4; i++){
		for(j=0; j<4; j++){
			if(field[0][i] == arr[j]){
				count++;
				continue;
			}
		}
	}
	if(count != 1){
		return true;
	}
	for(i=0; i<4; i++){
		for(j=0; j<4; j++){
			if(field[1][i] == arr[j]){
				count++;
				break;
			}
		}
	}
	if(count != 2){
		return true;
	}
	for(i=0; i<4; i++){
		for(j=0; j<4; j++){
			if(field[2][i] == arr[j]){
				count++;
				break;
			}
		}
	}
	if(count != 3){
		return true;
	}
	for(i=0; i<4; i++){
		for(j=0; j<4; j++){
			if(field[3][i] == arr[j]){
				count++;
				break;
			}
		}
	}
	if(count==4){
		return false;
	}
	else{
		return true;
	}
}

int main(void){
	int T;
	int case_count=1;
	scanf("%d", &T);
	while(T--){
		int field[4][4]={};
		int candi_array[4]={};
		int line;
		bool is_cheated=true;
		bool is_bad=false;
		bool is_bad_but_answer=false;
		int bad_count=0;
		char temp_ch='h';
		int i,j;

		scanf("%d", &line);
		for(i=0; i<4; i++){
			for(j=0; j<4; j++){
				scanf("%d",&field[i][j]);
			}
		}
		for(i=0; i<4; i++){
			candi_array[i]=field[line-1][i];
		}
		scanf("%d", &line);
		for(i=0; i<4; i++){
			for(j=0; j<4; j++){
				scanf("%d",&field[i][j]);
			}
		}
		if(is_stupid(field, candi_array)){
			is_bad = true;
		}
		for(i=0; i<4; i++){
			for(j=0; j<4; j++){
				if(field[line-1][i] == candi_array[j]){
					is_cheated=false;
					bad_count+=1;
					temp_ch=candi_array[j];
					if(!is_bad){
						printf("Case #%d: %d\n", case_count++, candi_array[j]);
					}
				}
			}
		}
		if(is_bad && bad_count==1){
			printf("Case #%d: %d\n", case_count++, temp_ch);
			continue;
		}
		if(is_cheated){
			printf("Case #%d: Volunteer cheated!\n", case_count++);
			continue;
		}
		if(is_bad){
			printf("Case #%d: Bad magician!\n", case_count++);
		}
	}
	return 0;
}