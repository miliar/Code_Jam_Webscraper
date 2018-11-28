#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;
const int NMax=1100;
int N,M,A[NMax];
LL Ceil(LL a,LL b) {
	if(a%b==0) return a/b;
	return a/b+1LL;
}
LL check(LL a,int b) {
	LL ret=0;
	a++;
	for(int i=1;i<=b;i++) ret+=Ceil(a,(LL)A[i]);
	a--;
	for(int i=b+1;i<=N;i++) ret+=Ceil(a,(LL)A[i]);
	return ret;
}
int main()
{
	FILE *fin=fopen("input.txt","r"),*fout=fopen("output.txt","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int I=1;I<=T;I++) {
		printf("%d\n",I);
		fscanf(fin,"%d%d",&N,&M);
		for(int i=1;i<=N;i++)
			fscanf(fin,"%d",A+i);
		int ret=-1;
		for(int i=1;i<=N;i++) {	
			LL l=0,r=(LL)M;
			while(l<r) {
				if(l+1==r) break;
				LL mid=(l+r)>>1LL;
				LL cnt=check((LL)mid*(LL)A[i],i);
				if(cnt==M) {
					ret=i;
					break;	
				}
				if(cnt<=M) l=mid;
				else r=mid;
			}
			if(ret==-1) {
				LL cnt=check((LL)l*(LL)A[i],i);
				if(cnt==M)
					ret=i;
			}
			if(ret!=-1) break;
		}
		fprintf(fout,"Case #%d: %d\n",I,ret);
		if(ret==-1) {
			puts("Here");
			getchar();getchar();
		}
	}
	fclose(fin);fclose(fout);
	return 0;
}
