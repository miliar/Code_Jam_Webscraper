#include <stdio.h>
#include <string.h>
//freopen("E:/A-small-attempt4.in","r",stdin);
//freopen("E:/a.out","w+",stdout);
__int64 str[200]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,-1};
/*void init()
{
	__int64 i,a,f,b;
	int j,len,str[20];
	for(i=1;i<=10000000;i++){
		a=i;len=0;
		while(a){
			str[len++]=a%10;
			a/=10;
		}
		f=0;
		for(j=0;j<=len/2;j++){
			if(str[j]!=str[len-j-1]){
				f=1;
				break;
			}
		}
		if(f==1)
			continue;
		a=i*i;len=0;
		while(a){
			str[len++]=a%10;
			a/=10;
		}
		f=0;
		for(j=0;j<=len/2;j++){
			if(str[j]!=str[len-j-1]){
				f=1;
				break;
			}
		}
		if(f==0)
			printf("%I64d,",i*i);
	}

}*/

int main()
{
	//freopen("E:/aa.txt","w+",stdout);
	//init();
	freopen("E:/C-large-1.in","r",stdin);
freopen("E:/c.out","w+",stdout);
	int tt,cas=1,i,j,s;
	__int64 a,b;
	scanf("%d",&tt);
	while(tt--)
	{
		scanf("%I64d%I64d",&a,&b);
		s=0;
		for(i=0;str[i]>0;i++){
			if(str[i]>=a && str[i]<=b)
				s++;
			else if(str[i]>b)
				break;
		}
		printf("Case #%d: %d\n",cas++,s);
	}

return 0;
}