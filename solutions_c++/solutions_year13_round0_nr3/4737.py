#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>

using namespace std; 

int t;
int main()
{
	long long int a,b,count=0,temp,i,leng,j;
	int flag1,flag2,temp1,temp2;
	double a_sqr,b_sqr;
	char bla[40];
	int arr[]={0,1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011 ,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};
/*
		temp=i;
		sprintf(bla,"%lld",temp);
		leng=strlen(bla);
		for(j=0;j<leng/2;j++)
		{
//			printf("%lld %lld %lld\n",j,leng-j-1,leng);
			if(bla[j]!=bla[leng-(j+1)])
			{
				break;
			}
		}
		if(j<leng/2){arr[i]=count;continue;}
		else{
		temp=i*i;
		sprintf(bla,"%lld",temp);
		leng=strlen(bla);
//		printf("length is %lld\n",leng);
		for(j=0;j<leng/2;j++)
		{
//			printf("%lld %lld %lld\n",j,leng-j-1,leng);
			if(bla[j]!=bla[leng-(j+1)])
			{
				break;
			}
		}
		if(j>=leng/2){count++;arr[i]=count;printf("i==%lld || ",i);}
		else{arr[i]=count;}}*/
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		flag1=0;flag2=0;
		scanf("%lld %lld",&a,&b);
		a_sqr=sqrt(a);
		if((a_sqr-(int)a_sqr)==0){flag1=1;}
		b_sqr=sqrt(b);
		if((b_sqr-(int)b_sqr)==0){flag2=1;}
//		printf("%d\n",lower_bound(arr,arr+39,(int)b_sqr)-arr);
	//	printf("so.. %d %d\n",(int)b_sqr,(int)a_sqr);
		temp1=arr[lower_bound(arr,arr+40,(int)a_sqr)-arr];
		if(temp1==(int)a_sqr && flag1==0){flag1=1;}
		else{flag1=0;}
		temp2=arr[lower_bound(arr,arr+40,(int)b_sqr)-arr];
		if(temp2==(int)b_sqr){flag2=1;}
		else{flag2=0;}
//		printf("%d\n",flag2);
//		printf("%d ",(lower_bound(arr,arr+40,4)-arr));
//		printf("%d\n",(lower_bound(arr,arr+40,(int)a_sqr)-arr));
		printf("Case #%lld: %ld\n",i+1,(lower_bound(arr,arr+40,(int)b_sqr)-arr)-(lower_bound(arr,arr+40,(int)a_sqr)-arr)+flag2-flag1);
	}
	return 0;
}

