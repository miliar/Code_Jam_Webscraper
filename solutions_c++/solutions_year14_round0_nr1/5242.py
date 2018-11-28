#include<stdio.h>
#include<memory.h>
#include<fstream>
using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	int idx = 0;
	int card[17];
	int row1, row2;
	while(idx < T){
		++ idx;
		memset(card, 0, sizeof(card));
		scanf("%d", &row1);
		int tmp;
		for(int i = 0;i < 4;i ++)
			for(int j = 0;j < 4;j ++){
				scanf("%d", &tmp);
				if(i == row1 - 1){
					card[tmp] = 1;
				}
			}
		scanf("%d", &row2);
		int hit = 0;
		int num = 0;
		for(int i = 0;i < 4;i ++)
			for(int j = 0;j < 4;j ++){
				scanf("%d", &tmp);
				if(i == row2 - 1 && card[tmp] == 1){
					++ hit;
					num = tmp;
				}
			}
		ofstream fout;
		fout.open("output.txt", ios::app);
		if(hit == 1){
			printf("Case #%d: %d\n", idx, num);
			fout << "Case #" << idx << ": " << num << endl;
		}
		else if(hit > 1){
			printf("Case #%d: Bad magician!\n", idx);
			fout << "Case #" << idx << ": Bad magician!" << endl;
		}
		else{
			printf("Case #%d: Volunteer cheated!\n", idx);
			fout << "Case #"<< idx << ": Volunteer cheated!" <<endl;
		}
	}
	return 0;
}
