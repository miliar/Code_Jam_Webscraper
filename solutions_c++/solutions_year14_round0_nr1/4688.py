#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
	freopen("A-small-attempt (2).in","r",stdin);
	freopen("A-small-attempt.out","w",stdout);
	int T; //�������ݸ���
	int first,second;
	int magicFirst[4][4];
	int magicSecond[4][4];
	scanf(" %d",&T);
	for(int i = 0;i < T;i ++){
		scanf("%d",&first); // ��һ��������
		for(int j = 0;j < 4;j ++) // ����
			for(int k = 0;k < 4;k ++)
				scanf(" %d",&magicFirst[j][k]);

		scanf(" %d",&second);  // �ڶ���������
		for(int j = 0;j < 4;j ++) // �ڶ��ξ���
			for(int k = 0;k < 4;k ++)
				scanf(" %d",&magicSecond[j][k]);

		int num = 0,flagbad = 0;
		for(int j = 0;j < 4;j ++){
			int flag = 0;
			for(int k = 0;k < 4;k ++){
				if(magicFirst[first-1][j] == magicSecond[second-1][k]){
					if (num != 0){
						flagbad = 1;
						flag = 1;
						break;
					}
					else
						num = magicFirst[first-1][j];
				}
			}
			if(flagbad == 1)
				break;
		}
		if(num == 0)
			printf("Case #%d: Volunteer cheated!\n",i + 1);
		else{
			if(flagbad == 1)
				printf("Case #%d: Bad magician!\n",i + 1);
			else
				printf("Case #%d: %d\n",i + 1,num);
		}
	}
	return 0;
}