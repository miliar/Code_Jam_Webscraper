#include "stdio.h"
#include "stdlib.h"
#include "string.h"


int main(){
	int count[10],Acount[26];
	FILE *fp,*out;
	fp = fopen("A-large.in","r");
	out = fopen("Getting the Digits.txt","w");
	int T=0;
	fscanf(fp,"%d",&T);
	for(int tc=0;tc<T;++tc){
		char buf[3000];
		fscanf(fp,"%s",buf);
		
		for(int i=0;i<10;++i){
			count[i]=0;
		}
		for(int i=0;i<26;++i){
			Acount[i]=0;
		}
		
		int temp;
		for(int i=0;i<strlen(buf);++i){
			temp = buf[i]-'A';
			Acount[temp]++;
		}
		
		//ZERO
		count[0]=Acount['Z'-'A'];
		Acount['Z'-'A']-=count[0];
		Acount['E'-'A']-=count[0];
		Acount['R'-'A']-=count[0];
		Acount['O'-'A']-=count[0];
		
		//TWO
		count[2]=Acount['W'-'A'];
		Acount['T'-'A']-=count[2];
		Acount['W'-'A']-=count[2];
		Acount['O'-'A']-=count[2];
		
		//SIX
		count[6]=Acount['X'-'A'];
		Acount['S'-'A']-=count[6];
		Acount['I'-'A']-=count[6];
		Acount['X'-'A']-=count[6];
		
		//EIGHT
		count[8]=Acount['G'-'A'];
		Acount['E'-'A']-=count[8];
		Acount['I'-'A']-=count[8];
		Acount['G'-'A']-=count[8];
		Acount['H'-'A']-=count[8];
		Acount['T'-'A']-=count[8];
		
		//THREE
		count[3]=Acount['T'-'A'];
		Acount['T'-'A']-=count[3];
		Acount['H'-'A']-=count[3];
		Acount['R'-'A']-=count[3];
		Acount['E'-'A']-=count[3];
		Acount['E'-'A']-=count[3];
		
		//FOUR
		count[4]=Acount['R'-'A'];
		Acount['F'-'A']-=count[4];
		Acount['O'-'A']-=count[4];
		Acount['U'-'A']-=count[4];
		Acount['R'-'A']-=count[4];
		
		//FIVE
		count[5]=Acount['F'-'A'];
		Acount['F'-'A']-=count[5];
		Acount['I'-'A']-=count[5];
		Acount['V'-'A']-=count[5];
		Acount['E'-'A']-=count[5];
		
		//SEVEN
		count[7]=Acount['V'-'A'];
		Acount['S'-'A']-=count[7];
		Acount['E'-'A']-=count[7];
		Acount['V'-'A']-=count[7];
		Acount['E'-'A']-=count[7];
		Acount['N'-'A']-=count[7];
		
		//NINE
		count[9]=Acount['I'-'A'];
		Acount['N'-'A']-=count[9];
		Acount['I'-'A']-=count[9];
		Acount['N'-'A']-=count[9];
		Acount['E'-'A']-=count[9];
		
		//ONE
		count[1]=Acount['O'-'A'];
		
		printf("Case #%d: ",tc+1);
		fprintf(out,"Case #%d: ",tc+1);
		for(int i=0;i<10;++i){
			while(count[i]>0){
				printf("%d",i);
				fprintf(out,"%d",i);
				count[i]--;
			}
		}
		printf("\n");
		fprintf(out,"\n");
	}
}
