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
		cNum = 2; // 쿠키버는속도
		fNum = 0; // 농장갯수
		time = 0; // 시간
		fscanf(r, "%lf %lf %lf\n", &C, &F, &X); // 농장쿠키개수 , 농장쿠키버는속도, 목표

		while (true){
			resTime = X / cNum; // 현재속도로 쿠키버는 시간
			if (C / cNum + X / (cNum + F) < resTime){ // 농장 사는 시간 + 다음 농장 하나 사서 남은 시간 체크하는 것보다 
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