#include <cstdio>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstdlib>
using namespace std;
int len,Bit[20];
long long Res,ans[11];
bool checkPrime(long long num){
	bool flag=true;
	if(num<4){
		if(num<2) return false;
		else return true;
	}
	for(long long i=2;i<=(long long)sqrt(num);++i){
		if(num%i==0){
			Res=num/i;
			flag=false;
			break;
		}
	}
	return flag;
}
long long trans(int base){
	long long ans=1;
	for(int i=len-3;i>=0;--i){
		ans*=base;
		if(Bit[i]) ans+=1;
	}
	ans*=base;
	ans+=1;
	return ans;
}
void getBit(int n,int e){
	for(int i=0;i<e;++i){
		if(n&(1<<i)) Bit[i]=1;
		else Bit[i]=0;
	}
}
int main () {
	int now=0,cnt=0,lim=2;
	int T,total;
	FILE* fp=fopen("C-small-attempt0.in","r");
	FILE* fp2=fopen("C.txt","w");
	fscanf(fp,"%d %d %d",&T,&len,&total);
	while(cnt<total){
		int flag=1;
		fill(Bit,Bit+20,0);
		getBit(now,len-2);
		for(int base=2;base<=10;++base){
			long long tmp=trans(base);
			if(checkPrime(tmp)) {
				flag=0;
				break;
			}
			ans[base]=Res;
		}
		if(flag) {
			cnt++;
			if(cnt==1){
				fprintf(fp2,"%s","Case #1:\n");
				//printf("Case #1:\n");
			}

			fprintf(fp2,"1");
			for(int i=len-3;i>=0;--i) 
				fprintf(fp2,"%d",Bit[i]);
				//printf("%d",Bit[i]);
			fprintf(fp2,"1");

			for(int i=2;i<=10;++i)
				fprintf(fp2," %lld",ans[i]);
			fprintf(fp2,"\n");
		}
		++now;
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}