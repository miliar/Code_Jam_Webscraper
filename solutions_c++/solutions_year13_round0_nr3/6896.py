#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define MAX 1000
int zero(char *s) {
	int i=0;
	int t=0;
	while(s[i]!='\0') {
		if(s[i]!='0')
		{
			t=1;
			break;
		}
		i++;
	}
	if(t==0)
	return 1;
	else return 0;
}
void zeroedit(char *s) {
	int l;
	l=strlen(s);
	int i;
	int k=0;
	int t=1;
	for(i=0;i<l;i++) {
		if(s[i]=='0' && t==1) {
			continue;
		}
		t=0;
		s[k]=s[i];
		k++;
	}
	s[k]='\0';
}
void call_sqrt(char *number,char *result,char *extra);
void reverse(char *from, char *to ) {
		int len=strlen(from);
		int l;
		for(l=0;l<len;l++)
			to[l]=from[len-l-1];
		to[len]='\0';
}

void call_mult(char *first,char *sec,char *result)
{
	char F[MAX],S[MAX],temp[MAX];
	int f_len,s_len,f,s,r,t_len,hold,res;
	f_len=strlen(first);
	s_len=strlen(sec);
	reverse(first,F);
	reverse(sec,S);
	t_len=f_len+s_len;
	r=-1;
	for(f=0;f<=t_len;f++)
	temp[f]='0';
	temp[f]='\0';
	for(s=0;s<s_len;s++){
		hold=0;
		for(f=0;f<f_len;f++){
				res=(F[f]-'0')*(S[s]-'0') + hold+(temp[f+s]-'0');
				temp[f+s]=res%10+'0';
				hold=res/10;
				if(f+s>r) 
					r=f+s;
		}
		while(hold!=0){
			res=hold+temp[f+s]-'0';
			hold=res/10;
			temp[f+s]=res%10+'0';
			if(r<f+s) 
				r=f+s;
			f++;
		}
	}
	for(;r>0 && temp[r]=='0';r--);
		temp[r+1]='\0';
	reverse(temp,result);
}

int call_minus(char *large, char *small, char *result){
	char L[MAX], S[MAX];
	int  l,s,now,hold,diff;
	l=strlen(large);
	s=strlen(small);
	if(l<s)
		return 0;
	if(l==s){
		if(strcmp(large, small)<0)
			return 0;
	}
	reverse(large,L);
	reverse(small,S);
	for(;s<l;s++)
		S[s]='0';
	S[s]='\0';
	for(now=0,hold=0;now<l;now++){
			diff=L[now]-(S[now]+hold);
			if(diff<0){
				hold=1;
				result[now]=10+diff+'0';
			} else{
				result[now]=diff+'0';
				hold=0;
			}
	}
	for(now=l-1;now>0;now--){
			if(result[now]!='0')
			break;
	}
	result[now+1]='\0';
	reverse(result,L);
	strcpy(result,L);
	return 1;
}

void call_sqrt(char *number,char *result,char *extra){
	int num,start,e,mul,l,r=0,len;
	char left[MAX],after[MAX];
	char who[5],temp[MAX],two[5];
	len=strlen(number);
	if(len%2==0){
			num=10*(number[0]-'0') + number[1]-'0';
			start=2;
	} else{
		num=number[0]-'0';
		start=1;
	}
	mul=(int) sqrt(num);
	result[0]=mul+'0';
	result[1]='\0';
	if(num-mul*mul ==0)
			extra[0]='\0';
	else
	sprintf(extra,"%d",num-mul*mul);
	for(;start<len;start+=2){
		e=strlen(extra);
		extra[e]=number[start];
		extra[e+1]=number[start+1];
		extra[e+2]='\0';
		two[0]='2';
		two[1]='\0';
		call_mult(result,two,left);
		l=strlen(left);
		for(mul=9;mul>=0;mul--){
			who[0]=mul+'0';
			who[1]='\0';
			strcat(left,who);
			call_mult(left,who,after);
			if(call_minus(extra,after,temp)==1){
					result[++r]=mul+'0';
					result[r+1]='\0';
					strcpy(extra,temp);
					break;
			} else
				left[l]='\0';
		}
	}
	result[++r]='\0';
}
	
int flag;
int che(char *K) {
	int k,flag,i;
	k=strlen(K);
	flag=k-1;
	for(i=0;i<k/2;i++)
	{
		if(K[i]==K[flag])
		flag--;
		else
		return 0;
	}
	return 1;
}
void rever(char *K) {
	int len,i,tmp,t,tmp1;
	len = strlen(K);
	flag = 1;
	for(i=0; i<len; i++) {
		if(K[i] != '9') {
			flag = 0;
			break;
		}
	}
	if(flag == 1) {
		K[0] = '1';
		for(i=1; i<len; i++)
				K[i] = '0';
				K[len] = '1';
				K[len+1] = '\0';
				return ;
	}
	flag = 0;
	for(i=0; i<len/2; i++) {
		if(K[i] < K[len-i-1])
		flag = -1;
		else if(K[i] > K[len-i-1])
		flag = 1;
		K[len-i-1] = K[i];
	}
	if(flag == -1 || flag==0){
		t = 0;
		if(len%2 == 0)
		tmp1 = len/2-1;
		else
		tmp1 = len/2;
		while(K[tmp1-t] == '9') {
			K[tmp1-t] = '0';
			K[len-1-tmp1+t] = '0';
			t++;
		}
		K[tmp1-t] ++;
		K[len-1-tmp1+t] = K[tmp1-t];
	}
}

int check(char *K, char *L) {
	int l,k;
	l=strlen(L);
	k=strlen(K);
	if((strcmp(K,L)>0 && k==l) || k>l)
	return 0;
	else return 1;
}	

/*int main(){
	char fir[MAX],ex[MAX],res[MAX];
	while(scanf("%s",&fir)==1){
		call_sqrt(fir,res,ex);
		printf("%s",res);
		printf("\n");
	}
	return 0;
}
	*/
int main(){
	char K[1000002];
    char L[1000002];

    char fir[MAX],ex[MAX],res1[MAX],res2[MAX];
	int t,i,k;
	scanf("%d\n",&t);
	for(i=0; i<t; i++) {
		int sum=0;
		scanf("%s",K);
		if(zero(K))
		sum++;
		zeroedit(K);
		call_sqrt(K,res1,ex);
		call_mult(res1,res1,fir);
		//printf("*%s*\n",fir);
		if(strcmp(fir,K)==0 && che(K))
		{
			//printf("%s*\n",K);
			sum++;
		}
		//if(che(res1))
		//printf("%s\n",res1);
		scanf("%s",L);
		zeroedit(L);
		call_sqrt(L,res2,ex);
		//printf("%s*\n",res2);
		while(1) {
 
			rever(res1);
			k=check(res1,res2);
			if(k==0)
			break;
			call_mult(res1,res1,fir);
			//printf("**%s\n",fir);
			if(che(fir))
			sum++;
			//printf("%s\n",res1);
		}
		printf("Case #%d: %d\n",i+1,sum);
	}
	return 0;
}
/*int main(){
	char K[1000002];
    char L[1000002];

    char fir[MAX],ex[MAX],res1[MAX],res2[MAX];
	int t,i,k;
	scanf("%d\n",&t);
	for(i=0; i<t; i++) {
		int sum=0;
		scanf("%s",K);
		if(zero(K))
		{	sum++;
			K[0]='1';
			K[1]='\0';
		}
		scanf("%s",L);
		zeroedit(K);
		zeroedit(L);
		while(1) {
 
			rever(K);
			call_sqrt(K,res1,ex);
			call_mult(res1,res1,fir);
			if(strcmp(fir,K)==0)
			sum++;
			k=check(K,L);
			if(k==0)
			break;
			printf("%s\n",K);
		}
		printf("%d\n",sum);
	}
	return 0;
}*/

