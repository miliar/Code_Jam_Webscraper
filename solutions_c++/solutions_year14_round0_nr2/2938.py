#include <stdio.h>
int main(){
	FILE *r, *s;
	double C, F, X;
	double cNum, resTime,time;
	int fNum;

	int roundNum, currRound = 0;

	r = fopen("B-large.in", "r");
	s = fopen("B-large.out", "w");
	fscanf(r, "%d\n", &roundNum);

	while (currRound < roundNum){
		cNum = 2; // ��Ű���¼ӵ�
		fNum = 0; // ���尹��
		time = 0; // �ð�
		fscanf(r, "%lf %lf %lf\n", &C, &F, &X); // ������Ű���� , ������Ű���¼ӵ�, ��ǥ

		while (true){
			resTime = X / cNum; // ����ӵ��� ��Ű���� �ð�
			if (C / cNum + X / (cNum + F) < resTime){ // ���� ��� �ð� + ���� ���� �ϳ� �缭 ���� �ð� üũ�ϴ� �ͺ��� 
				time += C / cNum;
				fNum++;
				cNum = 2 + F * fNum;
			}
			else {
				time += resTime;
				fprintf(s,"Case #%d: %.7lf\n",currRound+1, time);
				break;
			}
		}
		currRound++;
	}
}