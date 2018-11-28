#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdlib.h>
#include<math.h>
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
int ispallindrome(int a)
{
char A[100];
itoa(a,A,10);
for(int i=0;A[i]!='\0';i++);
for(int j=0,k=i-1;(j<i/2)&&A[j]==A[k];j++,k--);
if(j==i/2)
	return 1;
else
	return 0;
}

void main()
{
ifstream infile("A0.txt");
ofstream outfile("ans3.txt");
char A[100];
infile.getline(A,100);
int T=atoi(A);
for(int i=1;i<=T;i++)
	{

	int num=0;
	infile.getline(A,100);
	int B[100];
	split(A,B);
	float lower=B[0];
	float upper=B[1];
	for(int j=lower;j<=upper;j++)
		if(ispallindrome(j))      {int l=sqrt(j);
			if(ispallindrome(l)&&(l*l==j))
				{
				num++;
				cout<<j<<" ";
				getch();
				}        }
       outfile<<"Case #"<<i<<": "<<num<<endl;
       }


}
