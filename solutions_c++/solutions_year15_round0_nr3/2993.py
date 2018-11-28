#include<stdio.h>
#include<math.h>
#include<time.h>

static int sign;
char multi(char a, char b){
	if(a=='1'){
		return b;
	}
	if(a=='i'){
		if(b=='1'){
			return 'i';
		}
		if(b=='i'){
			sign=(sign+1)%2;		
			return '1';
		}
		if(b=='j'){		
			return 'k';
		}
		if(b=='k'){
			sign=(sign+1)%2;		
			return 'j';
		}

	}
	if(a=='j'){
		if(b=='1'){
			return 'j';
		}
		if(b=='i'){
			sign=(sign+1)%2;		
			return 'k';
		}
		if(b=='j'){
			sign=(sign+1)%2;
			return '1';
		}
		if(b=='k'){		
			return 'i';
		}

	}
	if(a=='k'){
		if(b=='1'){
			return 'k';
		}
		if(b=='i'){	
			return 'j';
		}
		if(b=='j'){
			sign=(sign+1)%2;
			return 'i';
		}
		if(b=='k'){	
			sign=(sign+1)%2;
			return '1';
		}

	}

}

int main(){	
	int T;
	int X;
	int L;
	int i;
	int j;
	int k;
	char c;
	char mtotal;
	int mi,mj,mk;
	FILE *fp_input,*fp_output;
	fp_input=fopen("C-small-attempt1.in","rb");
	//fp_input=fopen("A-small-practice.in","rb");
	fp_output=fopen("output.in","w");
	fscanf(fp_input,"%d\n",&T);
	//printf("%d\n",T);
	for(i=1;i<=T;i++)
	{
		//fscanf(fp_input,"\n");
		fscanf(fp_input,"%d ", &L);
		fscanf(fp_input,"%d\n", &X);
		//printf("%d %d\n", L, X);
		mtotal='1';
		mi=0;
		mj=0;
		mk=0;
		sign=0;
		for(j=1;j<=X;j++){
			for(k=1;k<=L;k++){
				fscanf(fp_input,"%c",&c);
				/*if(j==1){
					printf("%c",c);
				}*/
				mtotal=multi(mtotal,c);
				if(mtotal=='i' && mi==0 && sign==0){
					mi=1;
				}
				if(mtotal=='k' && mj==0 && mi==1 && sign==0){
					mj=1;
				}
			}
			if(j!=X){
					fseek(fp_input, -L, 1);
			}
			else{
				fscanf(fp_input,"\n");
			}
		}
		if(mtotal=='1'&& mj==1 && mi==1 && sign==1){
				mk=1;
				fprintf(fp_output,"Case #%d: YES\n", i);
				printf("Case #%d: YES\n", i);
		}
		else{
			fprintf(fp_output,"Case #%d: NO\n", i);
			printf("Case #%d: NO\n", i);
		}
	}
	fclose(fp_input);
	fclose(fp_output);
	getchar();
}