#include <stdio.h>

int main(){
int l= 0;
int t=0; //contains testcases
char c[4][4]; //defines array for the game
int hasDot=0;//definitely cannot expect a dot in the begining
int i,j=0,m=1,n;
FILE *fp = fopen("input.txt","r+");
FILE *fp1 =fopen("output.txt","w+");;
fscanf(fp,"%d\n",&t);


while(t > 0){
    l++;
    m=1;
    //takes the value for the game
   for(i=0;i<4;i++){
    for(j=0;j<4;j++){
        fscanf(fp,"%c",&c[i][j]);
    }
    fscanf(fp,"\n");
   }
   fscanf(fp,"\n");

  for(i=0;i<4;i++){
	for(j=0;j<4;j++){
		printf("%c",c[i][j]);
	    if(c[i][j]=='.'){
		hasDot=1;
	 //   break;
	    }
	}

	printf("\n");
    }
printf("\n");
    //horizontal
    for(i=0;i<4;i++){
	 n =   c[i][0]&c[i][1]&c[i][2]&c[i][3];
  //   printf("%d\n",n);
     if((n==80)||(n==88)){
	 fprintf(fp1,"Case #%d: X won\n",l);
	 m=0;
	 break;
     }else if((n==68 )||(n==79)){
         fprintf(fp1,"Case #%d: O won\n",l);
         m=0;
         break;
     }
    }
    if(m==1){
    //vertical
    for(i=0;i<4;i++){
     n=c[0][i]&c[1][i]&c[2][i]&c[3][i];
   //  printf("%d\n",n);
      if((n==80 )||((n==88))){
         fprintf(fp1,"Case #%d: X won\n",l);
         m=0;
         break;
     }else if((n==68 )||(n==79)){
         fprintf(fp1,"Case #%d: O won\n",l);
         m=0;
         break;
     }
    }
 }
 if(m==1){
    n = c[0][0]&c[1][1]&c[2][2]&c[3][3];
     //printf("diagonal %d\n",n);
     if(n==80 ||n==88){
         fprintf(fp1,"Case #%d: X won\n",l);
         m=0;

    }else  if(n==68||n==79){
         fprintf(fp1,"Case #%d: O won\n",l);
         m=0;

    }
 }
 if(m==1){
     n= c[3][0]&c[2][1]&c[1][2]&c[0][3];
      printf("%d\n",n);
      if(n==80 ||n==88){
         fprintf(fp1,"Case #%d: X won\n",l);
         m=0;

    }else if(n==68 ||n==79){
         fprintf(fp1,"Case #%d: O won\n",l);
         m=0;

    }
 }
 if(m==1){
   if(hasDot){
         fprintf(fp1,"Case #%d: Game has not completed\n",l);
          m=0;
    }else{
        fprintf(fp1,"Case #%d: Draw\n",l);
        m=0;
    }
 }


    hasDot =0;
    t--;
}
return 0;
};


