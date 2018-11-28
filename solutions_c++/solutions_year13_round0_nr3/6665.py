#include <iostream>
#include <math.h>
using namespace std;
bool palindrome(long long int A)
{
	long long int j,i,auxA=A,aux=0,dig,num=A;
	for(i=0;num!=0;i++)
	{
		num=num/10;
	}
	for(j=i-1;j>=0;j--)
	{
		dig=auxA%10;
		auxA=auxA/10;	
		aux=aux+(dig*pow(10,j));
	}
	if(A==aux)
	{
		return (true);
	}else{
		return (false);
	}
}
int main ()
{
	bool palin,ppalin;
	int T,cont,A,B;
	long long int i,C,a,b,j;
	cin>>T;
	for(i=1;i<T+1;i++)
	{
		cin>>a>>b;
		A=sqrt(a); B=sqrt(b); cont=0;
		for(j=A;j<=B;j++)
		{
			palin=palindrome(j);
			if(palin==true)
			{
				C=j*j;
				ppalin=palindrome(C);
				if((ppalin==true)&&(C<=b)&&(C>=a))
				{cont=cont+1;}
			}
		}
		cout<<"Case #"<<i<<": "<<cont<<endl;
	}
	return 0;
}

