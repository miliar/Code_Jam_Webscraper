#include<cstdio>
#include<cstring>
#include<memory.h>

char str[101];

int max(int a,int b){return a>b?a:b;}

bool is_consonant(char c){
	return !(c == 'a' || c== 'e' || c == 'i' || c=='o' || c=='u');
}

int c[101];

int num_consecute(int left, int right){
	if( left == 0 ) return c[right];
	return c[right] - c[left-1];
}

int main(){
	int T, casenum;
	FILE *in=fopen("consonants.in","rt");
	FILE *out=fopen("consonants.out","wt");
	fscanf(in,"%d",&T);
	int n;
	int len, i, j;
	
	for(casenum = 1; casenum <= T; casenum++){
		fscanf(in,"%s %d", str, &n);
		memset(c, 0, sizeof(c));		
		len = strlen(str);
		for(i=0;i <= len - n;++i) {
			bool flag=true;
			for(j=0;j < n; ++j){
				if(!is_consonant(str[i+j])){
					flag = false;					
				}
			}		
			if(flag) c[i] = 1;
		}
		
		int cnt = 0;
		for(i=0;i<len;++i){
			int flag = false;
			for(j=i+1; j <= len; ++j){
				if(flag) {cnt++; continue;}
				
				int k;
				for(k=i; k <= j-n; ++k){
					if(c[k]) { flag=true; break;}
				}				
				if(flag) 
					cnt++;
			}
		}
		fprintf(out, "Case #%d: %d\n", casenum, cnt);
	}
	fclose(out);
	fclose(in);
	return 0;
}