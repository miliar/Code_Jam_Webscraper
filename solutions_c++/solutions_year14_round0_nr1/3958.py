#include <iostream>

using namespace std;

int T;
int r1;
int r2;

int vys;
int poc;
int tab1[7][7];
int tab2[7][7];

int scanfinput1()
	{
	 for (int o=1;o<=4;o++)
		 	{
		 	 for (int p=1;p<=4;p++)
		 	 	{
		 	 	 scanf("%d",&tab1[o][p]);
		 	 	}
		 	}
	 return 0;
	}

int scanfinput2()
	{
	 for (int o=1;o<=4;o++)
		 	{
		 	 for (int p=1;p<=4;p++)
		 	 	{
		 	 	 scanf("%d",&tab2[o][p]);
		 	 	}
		 	}
	 return 0;
	}
	

int give_output(int a,int b,int t)
	{
	 printf("%s","Case #");
     printf("%d",t);
     printf("%s",": ");
	 if (b==0) 
	 	{
	 	 printf("%s","Volunteer cheated!");
	 	}
	 if (b>1)
	 	{
	 	 printf("%s","Bad magician!");
	 	}
	 if (b==1)
	 	{
	 	 printf("%d",a);
	 	}
	 printf("\n");
	 return 0;
	}

int main() {
	cin>>T;
	for (int i=1;i<=T;i++)
		{
		 vys=0;
		 poc=0; 
		 		 
		 scanf("%d",&r1);
		 scanfinput1();

		 scanf("%d",&r2);
		 scanfinput2();
		 for (int o=1;o<=4;o++)
		 	{
		 	 for (int k=1;k<=4;k++)
		 	 	 {
		 	 	  if (tab1[r1][o]==tab2[r2][k]) {vys=tab1[r1][o];poc++;}
		 	 	  //cout<<"nasla sa zhoda medzi "<<o<<"   "<<k<<endl;
		 	 	 }
		 	}
		 give_output(vys,poc,i);
		}
	return 0;
}
