#include<cstdio>
#include<algorithm>
using namespace std;
unsigned long long moteSize[1000002];
void osmos(int cse){
	unsigned long long iSize,nMote,ans=0;
	scanf("%llu%llu",&iSize,&nMote);
	for(int i=0;i<nMote;i++)
		scanf("%llu",&moteSize[i]);
	sort(&moteSize[0],&moteSize[nMote]);
	for(int i=0;i<nMote;i++){
		if(moteSize[i]<iSize) iSize+=moteSize[i];
		else{
			int tmp,j;
			if(iSize-1==0) j=2147483647;
			else for(j=0,tmp=iSize;tmp<=moteSize[i];tmp+=tmp-1,j++);
			if(nMote-i <= j){
				ans+=nMote-i;
//				printf("delete: %llu <= %d\n",nMote-i,j);
				break;
			}else{
				ans+=j;
				iSize=tmp+moteSize[i];
//				printf("insert: %d\n",j);
			}
		}
	}
	printf("Case #%d: %llu\n",cse,ans);
	return;
}
int main(){
	int num;
	freopen("Osmos.in","r",stdin);
	freopen("Osmos.out","w",stdout);
	scanf("%d",&num);
	for(int i=1;i<=num;i++)
		osmos(i);
	return 0;
}
