#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
//#include<conio.h>
#include<map>

#define MOD 1000000007

using namespace std;

map<int,long long int>array1;

void generate()
{

array1[1]=1;
array1[2]=4;
array1[3]=9;
array1[4]=121;
array1[5]=484;
array1[6]=10201;
array1[7]=12321;
array1[8]=14641;
array1[9]=40804;
array1[10]=44944;
array1[11]=1002001;
array1[12]=1234321;
array1[13]=4008004;
array1[14]=100020001;
array1[15]=102030201;
array1[16]=104060401;
array1[17]=121242121;
array1[18]=123454321;
array1[19]=125686521;
array1[20]=400080004;
array1[21]=404090404;
array1[22]=10000200001;
array1[23]=10221412201;
array1[24]=12102420121;
array1[25]=12345654321;
array1[26]=40000800004;
array1[27]=1000002000001;
array1[28]=1002003002001;
array1[29]=1004006004001;
array1[30]=1020304030201;
array1[31]=1022325232201;
array1[32]=1024348434201;
array1[33]=1210024200121;
array1[34]=1212225222121;
array1[35]=1214428244121;
array1[36]=1232346432321;
array1[37]=1234567654321;
array1[38]=4000008000004;
array1[39]=4004009004004;

}

int main()
{
int t;
int count;
long long int m,n;
generate();

map<int,long long int>::iterator it;

scanf("%d",&t);

for(int i=1;i<=t;i++)
{
	scanf("%lld%lld",&m,&n);
	count=0;


	for(it=array1.begin();it!=array1.end();it++)
	{
		if(it->second>=m&&it->second<=n)
		count++;
	}

	printf("\nCase #%d: %d",i,count);

}


//	getch();
	return 0;
}
