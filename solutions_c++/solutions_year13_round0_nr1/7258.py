#include<iostream>
#include<stdlib.h>
#include<stdio.h>

void bitmap(int& circle, int& cross, char symbol)
{
	switch(symbol) {
	case 'O':
		circle = (circle << 1) | 0x1;
		cross = (cross << 1);
		break;
	case 'X':
		circle = (circle << 1);
		cross = (cross << 1) | 0x1;
		break;
	case '.':
		circle = (circle << 1);
		cross = (cross << 1);
		break;
	case 'T':
		circle = (circle << 1) | 0x1;
		cross = (cross << 1) | 0x1;
		break;
	}
}

bool check(int player) 
{
	int row1 = 0xf000;
	int row2 = 0x0f00;
	int row3 = 0x00f0;
	int row4 = 0x000f;
	int col1 = 0x1111;
	int col2 = 0x2222;
	int col3 = 0x4444;
	int col4 = 0x8888;
	int cross1 = 0x1248;
	int cross2 = 0x8421;
	if((player&row1) == row1) return true;
	if((player&row2) == row2) return true;
	if((player&row3) == row3) return true;
	if((player&row4) == row4) return true;
	if((player&col1) == col1) return true;
	if((player&col2) == col2) return true;
	if((player&col3) == col3) return true;
	if((player&col4) == col4) return true;
	if((player&cross1) == cross1) return true;
	if((player&cross2) == cross2) return true;
	return false;
}

bool check(int circle, int cross)
{
	int total = circle | cross;
	if(total != 0xffff) return true;
	return false;
}

int main()
{
	FILE * fp = fopen("input.txt","r");
	FILE * fop = fopen("output.txt", "w");
	char sInput[1000];
	int circle, cross;
	
	fgets(sInput,1000,fp);
	int iCount = atoi(sInput);

	for(int i=1;i<=iCount;i++) {
		circle = 0;
		cross = 0;
		for(int j=0;j<4;j++) {
			fgets(sInput,1000,fp);
			bitmap(circle,cross,sInput[0]);
			bitmap(circle,cross,sInput[1]);
			bitmap(circle,cross,sInput[2]);
			bitmap(circle,cross,sInput[3]);
			//printf("%s",sInput);
		}
		fgets(sInput,1000,fp);
		if( check(circle) ) {		// O win
			fprintf(fop,"Case #%d: O won\n",i);
		} 
		else if( check(cross) ) {	// X win
			fprintf(fop,"Case #%d: X won\n",i);
		}
		else if( check(circle,cross) ) {	// not finish
			fprintf(fop,"Case #%d: Game has not completed\n",i);
		}
		else {					// draw
			fprintf(fop,"Case #%d: Draw\n",i);
		}
	}
	//getchar();
	fclose(fop);
	fclose(fp);
	return 0;
}