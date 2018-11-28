#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
static char ques[500];
char result[30000],temp[20],restemp[40];
int pc,o,chk=0,times=0,cname[1100];
char xo/*,*no*/,cnm[4];
void dec();
void check();
void main(){
FILE *fp,*fo;
fp=fopen("input.in","r");
fo=fopen("output.txt","w");
int val=0;
for(int p=0;p<220;p++)
	ques[p]=0;
for(int i=0;i<220;i++){
	ques[val]=fgetc(fp);
	val++;
	}
for(int m=0;m<5;m++){
	if(ques[m]=='\n'){
		pc=m-1;
		//printf("%d",pc);
		break;
	}
}
int h=pc,s,d,f;
for(int k=1;h>=0;h--){
	//times=times+((int)((ques[h]-'0')*k));
	s=(int)(ques[h]-'0');
	times=times+(s*k);
	//printf("%d*\n",times);
	k=k*10;
}
//times=ques[0]-'0';
result[0]='\0';
for(o=1;o<=times;o++){
	cname[o-1]=o;
	dec();
	chk=0;
	//printf("*");
	//puts(restemp);
	//strcat(result,restemp);
}
//printf("%d",times)		;
fputs(result,fo);
/*int s;
scanf("%d",&s);*/
//				getch();
}
void dec(){
pc=pc+2;
for(int l=0;l<19;l++){
	temp[l]=ques[pc];
	//printf("%c",ques[pc]);
	pc++;
	}
check();
}
void check(){
	int t=19,dotcount=0,cpy=0;
	//char restemp[30];
	sprintf(cnm,"%d",cname[o-1]);
	char cno[4];
	cno[0]='\0';
	strcat(cno,cnm);
	//printf("**%c**",cno);
	//char no[4];
	char vxo[2];
	//no[0]='\0';
	//strcat(no,cnm);
	//vxo[0]=(char)xo;
	//no[strlen(cno)]='\0';
	vxo[1]='\0';
	//printf("**%c %c**",no[0],vxo[0]);
	for (int l=0;l<19;l++){
		if(temp[l]=='T')
		t=l;
	}
	for(int test=0;test<2;test++){
		if(chk==0)
			xo='X';
		if(chk==1)
			xo='O';
		temp[t]=xo;
		vxo[0]=(char)xo;
		for (int x=0;x<16;x++){
			if((temp[x]==xo && temp[x+1]==xo && temp[x+2]==xo && temp[x+3]==xo) || (temp[0]==xo && temp[6]==xo && temp[12]==xo && temp[18]==xo) || (temp[3]==xo && temp[7]==xo && temp[11]==xo && temp[15]==xo)){
			restemp[0]='\0';
			strcat(restemp,"Case #");
			strcat(restemp,cno);
			strcat(restemp,": ");
			strcat(restemp,vxo);
			strcat(restemp," won\n");
			//gets(restemp);
			cpy++;
			//printf("Case #%d : %c Won\n",o,xo);
			break;
			}
			if(x<=3){
				if(temp[x]==xo && temp[x+5]==xo && temp[x+10]==xo && temp[x+15]==xo){
					restemp[0]='\0';
					strcat(restemp,"Case #");
					strcat(restemp,cno);
					strcat(restemp,": ");
					strcat(restemp,vxo);
					strcat(restemp," won\n");
					cpy++;
					//puts(restemp);
					//printf("Case #%d : %c Won\n",o,xo);
					break;
				}
			}
			if(temp[x]=='.')
			dotcount++;
		}
	chk++;
	}
	if(dotcount!=0 && cpy==0){
		restemp[0]='\0';
		strcat(restemp,"Case #");
		strcat(restemp,cno);
		strcat(restemp,": Game has not completed\n");
			}
	if(dotcount==0 && cpy==0){
		restemp[0]='\0';
		strcat(restemp,"Case #");
		strcat(restemp,cno);
		strcat(restemp,": Draw\n");
			}
	//result[0]='\0';
	strcat(result,restemp);
}