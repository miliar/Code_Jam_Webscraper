#include <cstdio>
#include <algorithm>
using namespace std;
typedef double ld;
typedef long long LL;
const int NMax=1000;
struct pii {
	int x,y;
};
pii mp(int x,int y) {
	pii ret;
	ret.x=x;ret.y=y;
	return ret;
}
LL pp(pii a,pii b) {
	return (LL)a.x*(LL)b.y-(LL)a.y*(LL)b.x;
}
int N;
pii A[NMax];
int main()
{
	int T;
	FILE *fin=fopen("input.txt","r"),*fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for(int I=1;I<=T;I++) {
		fscanf(fin,"%d",&N);
		for(int i=1;i<=N;i++) {
			int x,y;
			fscanf(fin,"%d%d",&x,&y);
			A[i]=mp(x,y);
		}
		fprintf(fout,"Case #%d:\n",I);
		for(int i=1;i<=N;i++) {
			int ret=N-1;
			for(int j=1;j<=N;j++) if(i!=j){
				int cnt=0,cnt1=0;
				for(int k=1;k<=N;k++) {
					LL x=pp(mp(A[k].x-A[j].x,A[k].y-A[j].y),mp(A[i].x-A[j].x,A[i].y-A[j].y));
					if(x==0) cnt1++;
					if(x<0) cnt++;
				}
				ret=min(ret,min(N-cnt-cnt1,cnt));
			}
			fprintf(fout,"%d\n",ret);
		}
	}
	fclose(fin);fclose(fout);
	return 0;
}
