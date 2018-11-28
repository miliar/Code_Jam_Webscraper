#include <cstdio>
#include <cstring>

void f(int);

int sMax,k,ans,t,sum,temp;
char str[1500];

int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
		f(i);
	return 0;
}

void f(int Case){
	sum=ans=0;
	scanf("%d ",&sMax);
	scanf("%s",str);
//	printf("%s++\n",str);
	sum+=str[0]-'0';
	for(int i=1;i<=sMax;i++){
		temp = i-sum;
		//printf("%d ",temp);
		if(temp>0){
			ans+=temp;
		//	printf("%d|",ans);
			sum+=temp;
		}
		sum+=str[i]-'0';
	}
	printf("Case #%d: %d\n",Case+1,ans);
}