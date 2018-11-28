#include<stdio.h>
#include<string.h>

int T;
char S[102];
int ans;

void twist(int first, int last);
int run(int last,int ans);

int main(){
	int i,j,k;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(k=1;k<=T;k++){
		scanf("%s",S);
		ans = run(strlen(S)-1,0);
		printf("Case #%d: %d\n",k,ans);
		i = strlen(S);
		for(j=0;j<i;j++)S[j]='\0';
	}
	
	return 0;
}

void twist(int first, int last){
	int p,q;
	char flag;
	for(p=first;p<=(first+last)/2;p++){
		q=first+last-p;
		if(p!=q){
			flag = S[p];
			S[p] = S[q];
			S[q] = flag;
			
			if(S[p]=='-')S[p]='+';
			else S[p]='-';
			if(S[q]=='-')S[q]='+';
			else S[q]='-';
			
		}
		else{
			if(S[p]=='-')S[p]='+';
			else S[p]='-';
		}
	}
}

int run(int last, int ans){
	int i,j;
	if(last == 0){
		if(S[last] == '+')return ans;
		else return ans+1;
	}
	else{
		if(S[last] == '+')return run(last-1,ans);
		else{
			if(S[0] == '-'){
				twist(0,last);
				return run(last-1,ans+1);
			}
			else{
				for(i=last-1;i>=0;i--)if(S[i]=='+')break;
				twist(0,i);
				twist(0,last);
				return run(last-1,ans+2);
			}
		}
	}
}
