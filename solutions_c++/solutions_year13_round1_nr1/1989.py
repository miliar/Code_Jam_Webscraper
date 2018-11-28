#include<iostream.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream.h>
#include<math.h>
int t;
int split(char A[],int B[],char ch=' ')
{
for(int i=0;A[i]!='\0';i++);
int n=0,num=0;
for(int j=0;j<i;j++)
	if(A[j]==ch)
		{int o=1;
		B[num]=0;
			for(int p=j-1;p>=n;p--) {
				B[num]=B[num]+((A[p]-48)*o);
				o*=10;


						}
			num++;
		n=j+1;
		 }
	 else if(A[j+1]=='\0')
		{
		int o=1;
		B[num]=0;
			for(int p=j;p>=n;p--){
				B[num]=B[num]+((A[p]-48)*o);
				o*=10;
				}


		num++;
		n=j+1;
		}
return num;
}
void main()
	{
	ifstream infile("aGCI1A.txt");
	ofstream outfile("GCI1ANS.txt");
	char A[100];
	infile.getline(A,100);
	int T;
	T=atoi(A);
	for(t=0;t<T;t++)
		{
		 infile.getline(A,100);
		 char a[100];
		 int r,t;
		 int two[10];
		 split(A,two);
		 r=two[0];
		 t=two[1];
		  cout<<endl<<r<<endl<<t;
		  getch();

		 int x=t;

		 for(int k=r,e=0;x>=0;k+=2,e++)
			{
			 float paint = ((pow((k+1),2) - pow(k,2)));
			 x=x-paint;
			 }
		 int res=e-1;
		 cout<<res<<endl;
		 outfile<<"Case #"<<::t<<": "<<res<<endl;
		  }

		  }
