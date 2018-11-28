#include<iostream>
#include<cmath>
using namespace std;


bool check_p(long double num1,long double num2,int dig)
{
	if(dig<0)return 0;
	bool ch;
	if( dig != 1 )
	{

		long double pom1,pom2,pom3;
		dig--;
		pom1 = num1 - floor( num1 / 10 ) * 10;
		pom2 = pow(10.0,dig);
		pom3 = floor( num2 / pom2 );
		if( pom1 == pom3 )
		{
			num1 = floor( num1 / 10 );
			pom2 = floor( num2 / pom2 ) * pom2; 
			num2 -= pom2;
			ch = check_p(num1,num2,dig);
		}
		if( pom1 != pom3 ) return 0;

	}

	if( dig == 1 )
	{
		if( num1 == num2 ) return 1;
		if( num1!=num2 ) return 0;
	}

	return ch;
}

bool palindrone(long double num)
{
	long double i,x=num,y=0;
	i = pow(10.0,100);
	int digits = 101;
	int h,z;
	while( x / i  <= 1 ){ digits--; i /= 10.0; }
	if( digits == 1 || num == 1) return 1;
	h = digits /  2 ;
	i = pow(10.0,h);
	x = floor( num / i );
	y = floor(num - x*i);
	
	if( digits % 2 ) 
	{
		x = floor( x / 10);
	}

	
	return check_p(x,y,h);
}

bool fns(long double x)
{
	if(palindrone(sqrt(x)) && palindrone(x)) return 1;
	else return 0;

}







int main()
{
	FILE *in,*out;
	in=fopen("C-small-attempt0.in","r");
	out=fopen("Cs.out","w");
	int T,count=0,s=0;
	int a,b;
	long double A,B,dif=1,dfpom=0;
	fscanf(in,"%d",&T);
	for(int i=0;i<T;i++)
	{
		fscanf(in,"%d %d",&a,&b);
		A=a;B=b;
		for( long double i=A; i<=B; i+=dif ) 
		{
			if(floor( sqrt(i))==sqrt(i) )
			{
				s++;
				if(fns(i))count++;
				if( s==1 ) dfpom=i;
				if( dfpom!=0 && s==2 )dif=i-dfpom;
				if( s>=2 )dif+=2;
			}
		}
		fprintf(out,"Case #%d: %d\n",i+1,count);
		count=0;
		s=0;
		dif=1;
	
	
	}

	

	system("PAUSE");
	fclose(in);
	fclose(out);
	return 0;
}