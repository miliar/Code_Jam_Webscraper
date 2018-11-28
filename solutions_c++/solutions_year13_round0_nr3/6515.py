#include<stdio.h>
#include<memory.h>
#include<math.h>



#define N 100

FILE *in = fopen("input.txt","rt");
FILE *out = fopen("output.txt","wt");

void process(int c){
	int i, j, k, n, m, a, b;
	__int64 temp;
	char data[N+10];
	int ans=0;
	bool flag;
	fscanf(in,"%d%d",&a,&b);
	n = sqrt(double(a));
	m = sqrt(double(b));
	if(n*n<a)n++;
	if(m*m>b)m--;
	for(i=n;i<=m;i++){
		flag = true;
		temp = i;
		k = 0;
		do{
			data[k++] = temp%10;
			temp/=10;
		}while(temp>0);
		flag = true;
		for(j=0;j<k/2;j++){
			if(data[j] != data[k-j-1]){
				flag = false;
				break;
			}
		}
		if(!flag)
			continue;
















		temp = (__int64)i*(__int64)i;
		k = 0;
		do{
			data[k++] = temp%10;
			temp/=10;
		}while(temp>0);
		flag = true;
		for(j=0;j<k/2;j++){
			if(data[j] != data[k-j-1]){
				flag = false;
				break;
			}
		}
		if(flag)
			ans++;
	}
	fprintf(out,"Case #%d: %d\n",c,ans);
}

int main(){
	int i, j;
	fscanf(in,"%d",&j);
	for(i=0;i<j;i++)
		process(i+1);
	fclose(in);
	fclose(out);
	return 0;
}