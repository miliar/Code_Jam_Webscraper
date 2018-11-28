#include <cstdio>

int main(){
	int T;
	FILE *fp = fopen("A-large.in","r+");
	FILE *fp1 = fopen("output.txt","w+");
	fscanf(fp,"%d",&T);
	for (int i=1;i<=T;i++){
		bool digit[10];
		long long n,num,time = 1,chk=0;
		fscanf(fp,"%lld",&n);
		for(int i=0;i<=9;i++)
			digit[i]=false;
		for(int temp = n;temp!=0;temp/=10)
			digit[temp%10]=true;
		while(time <=1000){
			chk=0;
			for(int i=0;i<10;i++){
				if(digit[i])
					chk++;
			}
			if(chk==10)
				break;
			++time;
			for(int temp = n*time;temp!=0;temp/=10)
				if(digit[temp%10]==false){
					digit[temp%10]=true;
					chk++;
				}
		}
		if(chk==10)
			fprintf(fp1,"Case #%d: %lld\n",i,n*time);
		else
			fprintf(fp1,"Case #%d: INSOMNIA\n",i);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}
