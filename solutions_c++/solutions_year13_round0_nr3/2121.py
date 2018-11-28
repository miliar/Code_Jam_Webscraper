#include <cstdio> //PROG: GCp3
#include <cstring>
#include <algorithm>
using std::sort;
bool isPalin(long long x){
	char buff[1024];
	sprintf(buff,"%I64d",x);
	int i,N;
	for (N=0;buff[N];N++);
	for (i=0;i<N/2;i++)
		if (buff[i]!=buff[N-i-1])
			return false;
	return true;
}
long long ary[1000000];int an;
int main(){
	#ifdef JACK1_NOTEBOOK
	freopen("GCp3_in.txt","r",stdin);
	freopen("GCp3_out.h","w",stdout);
	#endif
	int TN,TI,a,b,i,j,k,p,q,ans;
	long long x;
	//for (x=0;x<=10000005;x++){
	ary[an++]=1;
	ary[an++]=4;
	ary[an++]=9;
	for (x=10;x<=100005;x++){
		j=x%10;
		if (j==1||j==2){
			if (isPalin(x))
				if (isPalin(x*x)){
					ary[an++]=x*x;
				}
		}
	}
	//for (i=0;i<an;i++)
	//	printf("ary[%d]=%I64d\n",i,ary[i]);
	scanf("%d",&TN);
	for (TI=1;TI<=TN;TI++){
		scanf("%d%d",&a,&b);
		p=std::lower_bound(ary,ary+an,a)-ary;
		q=std::upper_bound(ary,ary+an,b)-ary;
		//printf("[%d,%d] -> range(%d,%d)\n",a,b,p,q);
		printf("Case #%d: %d\n",TI,q-p);
	}
}
