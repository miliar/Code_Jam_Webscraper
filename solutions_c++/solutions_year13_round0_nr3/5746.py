#include <cstdio>


bool chk[1001];
int main(){
	/*int a,b,c,d,e,f;
	for(int i=1;i*i<=1000;i++)
	chk[i*i]=true;

	scanf("%d", &a);

	for(b=0;b<a;b++){
	int cnt=0;
	scanf("%d %d", &c, &d);
	for(int e=c;e<=d;e++){
	int stack[4],tmp,count,flag=0;
	if(chk[e]){
	tmp=e;
	for(count=0;;count++){
	if(tmp/10 || tmp%10){
	stack[count]=tmp%10;
	tmp/=10;
	}
	else
	break;
	}
	count--;
	if(count){
	for(int p = 0 ;p < (count+1)/2;p++){
	if(stack[p]==stack[count-p]){
	flag=1;
	}
	}
	}
	if(!flag)cnt++;
	}

	}
	printf("Case #%d: %d\n",b+1,cnt);
	}*/
	FILE *input;
	FILE *output;
	input = fopen("C-small-attempt3.in","r");
	output = fopen("C-small-attempt3out.txt","w");
	chk[1]=true;
	chk[4]=true;
	chk[9]=true;
	chk[121]=true;
	chk[484]=true;
	int a,b,c,d,e;
	fscanf(input,"%d", &a);

	for(b=0;b<a;b++){
		int cnt=0;
		fscanf(input,"%d %d", &c, &d);
		for(e=c;e<=d;e++)
			if(chk[e])
				cnt++;
		fprintf(output,"Case #%d: %d\n", b+1,cnt);
	}
	return 0;
}