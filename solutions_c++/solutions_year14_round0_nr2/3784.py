#include<iostream>


using namespace std;

long double timer(long double C,long double F,long double X)
{
//	long double x2=X/2.0;
	//long double c2=C/2.0;
	//long double f1=F;
	long double result1=0.0,result2=0.0;
	long double result3=0.0,result4=0.0;
	int c=1;
		if(X/2.0<X/(2+F)+C/(2))
			{
				return X/2;
			}
		while(true)
		{
		result1 += C/(2+(c-1)*F);
		result2 =C/(2+(c*F));
		result3 = result1+ X/(2+(c)*F);
		result4 = result2+ X/(2+(c+1)*F) + result1;
		c++;
	//	cout<<result3 <<" AND "<<result4<<endl;
		
		if(result3<result4)
			return result3;
		//system("pause");
		}	

	}


void main()
{

	int T=0;
	long double C=0.0,F=0.0,X=0.0;

	long double y=0;
	cin>>T;

	for(int i=1;i<=T;i++)
	{
		y=0;
		cin>>C>>F>>X;
		y=timer(C,F,X);
	

		cout<<"Case #"<<i<<": ";
			printf("%.7f\n",y);

	}
	
}