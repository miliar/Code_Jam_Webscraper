#include <iostream>

using namespace std;

int T;
double C,F,X;
double strata0,prod0,vys0,strata1,prod1,vys1;

int put_output(double a,int b)
	{
	 printf("%s","Case #");
	 printf("%d",b);
	 printf("%s",": ");
	 printf("%.7f",a);
	 printf("\n");
	}

int main() {
	cin>>T;
	for (int i=1;i<=T;i++)
		{
		 cin>>C>>F>>X;//C-cena fabriky    F- zvysenie produkcie     X-final statement
		 prod0=2;
		 strata0=0;
		 vys0=X/prod0+strata0;;
		 
		 strata1=C/prod0;
		 prod1=prod0+F;
		 vys1=X/prod1+strata1;
		 
		 while (vys0>vys1)
		 	{
		 	 vys0=vys1;
		 	 prod0=prod1;
		 	 strata0=strata1;
		 	 
		 	 strata1=C/prod0+strata0;
		 	 prod1=prod0+F;
		 	 vys1=X/prod1+strata1;
		 	 //cout<<"stare:"<<vys0<<endl<<"nove:"<<vys1<<endl<<endl;
		 	}
		 put_output(vys0,i);
		}
	return 0;
}
