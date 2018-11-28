#include<stdio.h>
#include<string>
#include<string>
#include<math.h>


using namespace std;

inline bool isP(long long i)
{
	int j,k;
	char c;
	string str;
	while(i!=0)
	{
		c=i%10+'0';
		i/=10;
		str+=c;
	}
	for(k=0,j=str.length()-1;k<str.length()/2;--j,++k)
	{
		if(str[k]!=str[j]) return false;
	}
	return true;
}

int main()
{
	int T,abc;
	scanf("%d",&T);
	for(abc=1;abc<=T;++abc)
	{
		int result=0;
		long long A,B,a,b,i;
		scanf("%lld %lld",&A,&B);
		a = sqrt(A)+0.001;
		if(a*a<A) ++a;  
		b = sqrt(B)+0.001;
		for(;i<=b;++i)
		{
			if(isP(i)&&isP(i*i)) {++result;}
		}
		printf("Case #%d: %d\n",abc,result);
	}
	
	return 0;
}
