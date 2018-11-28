#include<cstdio>

int main(){
	int n;
	scanf("%d", &n);

	for(int i=0; i<n;i++){
		char a[16];
	
		scanf("%s", a);
		scanf("%s", a+4);
		scanf("%s", a+8);
		scanf("%s", a+12);
		int finish = 0;
				
		for(int j = 0; j<4;j++){
			int X = 1;
			for(int k = 0; k < 4; k++){
				if(a[j * 4 + k] != 'X' && a[j * 4 + k] != 'T')
					X = 0;
			}
			if(X == 1){
				printf("Case #%d: X won\n",i+1);
				finish = 1;
			}
		}
		if(finish == 1)
			continue;
		for(int j = 0; j<4;j++){
			int X = 1;
			for(int k = 0; k < 4; k++){
				if(a[j + k*4] != 'X' && a[j  + k*4] != 'T')
					X = 0;
			}
			if(X == 1){
				printf("Case #%d: X won\n",i+1);
				finish = 1;
			}
		}
		if(finish == 1)
			continue;
		int X = 1;
		for(int k = 0; k < 4; k++){
			if(a[k*5] != 'X' && a[k*5] != 'T')
				X = 0;
		}
		if(X == 1){
				printf("Case #%d: X won\n",i+1);
			continue;
		}
		X = 1;
		for(int k = 0; k < 4; k++){
			if(a[k*3 + 3] != 'X' && a[k*3 + 3] != 'T')
				X = 0;
		}
		if(X == 1){
				printf("Case #%d: X won\n",i+1);
			continue;
		}

		finish = 0;
				
		for(int j = 0; j<4;j++){
			int X = 1;
			for(int k = 0; k < 4; k++){
				if(a[j * 4 + k] != 'O' && a[j * 4 + k] != 'T')
					X = 0;
			}
			if(X == 1){
				printf("Case #%d: O won\n",i+1);
				finish = 1;
			}
		}
		if(finish == 1)
			continue;
		for(int j = 0; j<4;j++){
			int X = 1;
			for(int k = 0; k < 4; k++){
				if(a[j + k*4] != 'O' && a[j  + k*4] != 'T')
					X = 0;
			}
			if(X == 1){
				printf("Case #%d: O won\n",i+1);
				finish = 1;
			}
		}
		if(finish == 1)
			continue;
		X = 1;
		for(int k = 0; k < 4; k++){
			if(a[k*5] != 'O' && a[k*5] != 'T')
				X = 0;
		}
		if(X == 1){
				printf("Case #%d: O won\n",i+1);
			continue;
		}
		X = 1;
		for(int k = 0; k < 4; k++){
			if(a[k*3 + 3] != 'O' && a[k*3 + 3] != 'T')
				X = 0;
		}
		if(X == 1){
				printf("Case #%d: O won\n",i+1);
			continue;
		}

		finish = 0;
		for(int j = 0; j < 16; j++){
			if(a[j] == '.'){
				printf("Case #%d: Game has not completed\n",i+1);
				finish = 1;
				break;	
			}
		}
		if(finish)
			continue;
		else
				printf("Case #%d: Draw\n",i+1);
	
		
	}
}
