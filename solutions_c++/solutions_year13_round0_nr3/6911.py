#include <iostream.h>
#include <conio.h>
#include <fstream.h>
int palindrome(int);
void main ()
{clrscr();
ifstream input ("C-small-attempt4.in");
ofstream output ("output");
int z;
input>>z;
for (int i=1;i<=z;i++)
{int count=0,num1,num2,reverse,reverse1;
input>>num1>>num2;
for (int k=num1;k<=num2;k++)
{reverse=palindrome(k);
for (int j=1;j<=k;j++)
{if (k==(j*j)&&k==reverse)
{reverse1=palindrome(j);
if (j==reverse1)
{++count;}}}
}
output<<"Case #"<<i<<": "<<count<<endl;
}
input.close();
output.close();
getch();
}
int palindrome(int x)
{int n,digit,rev=0;
n=x;
do{
digit=n%10;
rev=(rev*10)+digit;
n/=10;
}while(n!=0);
return rev;
}

