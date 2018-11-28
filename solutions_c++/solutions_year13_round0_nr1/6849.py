#include <cstdio>
int main(){
	FILE *input;
	FILE *output;
	input = freopen("A-large.in","r",stdin);
	output = freopen("A-largeout.txt","w",stdout);
	int a,b,c,d,e,f;
	scanf("%d", &a);
	for(b=0;b<a;b++){
		char field[5][5];
		int xflag=0;
		int oflag=0;
		int nflag=0;
		for(c=0;c<4;c++)
			scanf("%s", field[c]);
		for(c=0;c<4;c++){
			//가로
			int xcnt=0;
			int ocnt=0;
			int tcnt=0;
			for(d=0;d<4;d++){
				if(field[c][d]=='O')
					ocnt++;
				else if(field[c][d]=='X')
					xcnt++;
				else if(field[c][d]=='T')
					tcnt++;
				else if(field[c][d]=='.')
					nflag=1;
			}
			if(ocnt+tcnt==4){
				oflag=1;
				break;
			}
			else if(xcnt+tcnt==4)
			{
				xflag=1;
				break;
			}
			tcnt=xcnt=ocnt=0;
			//세로 c <-> d
			for(d=0;d<4;d++)
			{
				if(field[d][c]=='O')
					ocnt++;
				else if(field[d][c]=='X')
					xcnt++;
				else if(field[d][c]=='T')
					tcnt++;
			}
			if(ocnt+tcnt==4){
				oflag=1;
				break;
			}
			else if(xcnt+tcnt==4)
			{
				xflag=1;
				break;
			}
			tcnt=xcnt=ocnt=0;
			//대각선의 경우 대각선
			if(c==0){
				for(d=0;d<4;d++){
					if(field[d][d]=='O')
						ocnt++;
					else if(field[d][d]=='X')
						xcnt++;
					else if(field[d][d]=='T')
						tcnt++;
				}
			}
			else if(c==3){
				for(d=0;d<4;d++){
					if(field[c-d][d]=='O')
						ocnt++;
					if(field[c-d][d]=='X')
						xcnt++;
					if(field[c-d][d]=='T')
						tcnt++;
				}
			}
			if(ocnt+tcnt==4){
				oflag=1;
				break;
			}
			else if(xcnt+tcnt==4)
			{
				xflag=1;
				break;
			}

		}
		if(xflag)
			printf("Case #%d: X won\n",b+1);
		else if(oflag)
			printf("Case #%d: O won\n",b+1);
		else if(nflag)
			printf("Case #%d: Game has not completed\n",b+1);
		else 
			printf("Case #%d: Draw\n",b+1);
	}
	return 0;
}