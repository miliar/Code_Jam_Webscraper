#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int main()
{
	freopen("A-small-attempt1.in.txt","r",stdin);
	freopen("A-small-attempt1.out.txt","w",stdout);
	int row1,cases,row2,i,j;
	int data,ans,deadFlag = 0;
	int s[17]={0};

	cin >> cases;

	for (int c = 1; c <= cases; c++){

		ans = -1;
		deadFlag = 0;
		for(i = 0; i < 17; ++i)
			s[i] = 0;
		
		cin >> row1;
		for (i = 1; i < 5; ++i)
			for (j = 0; j < 4; ++j){
				cin >> data;
				if (i == row1){
					s[data] = 1;
					// printf("%d\n",data);
				}
			}
		
		cin >> row2;
		// printf("Row2=%d\n",row2);
		for (i = 1; i < 5; ++i)
			for(j = 0; j < 4; ++j){
				cin >> data;
				if ((i == row2)&&(s[data] == 1)) {
					if (ans != -1)
						deadFlag = 1;
					ans = data;
				}
					// printf("#######%d\n", data);
				
			}
		printf("Case #%d: ",c);
		if (deadFlag) {
			printf("Bad magician!\n");			
		}else{
			if (ans == -1){
				printf("Volunteer cheated!\n");
			}else{
				printf("%d\n", ans);
			}
		}
	}
}