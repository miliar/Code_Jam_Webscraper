#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;
int plaindrome(int num);
int squareroot(int num);
int main()
{
ifstream fin("C-small-attempt0.in");
ofstream fout("file1.txt");
int T;
fin>>T;
for(int i=1;i<=T&&T<=100;i++)
{
int c=1;
int A,B;
fin>>A>>B;
int counter=0;
for(int j=A;j<=B&&A<=1000&&B<=1000;j++)
{
if(j==plaindrome(j))
{
	int root=squareroot(j);
	if(root)
	{
	if(root==plaindrome(root))
	{
	counter++;	
	}	
	}



}



}
fout<<"Case #"<<i<<": "<<counter<<endl;


}
fin.close();
fout.close();
}
int plaindrome(int num)
{
int num1=0;
for(int i=0;num>0;i++)
{
num1=num1*10+(num%10);
num=num/10;

}
return num1;

}
int squareroot(int num)
{
bool check=false;
int i;
for(i=1;i<=num/2+1;i++)
{
	check=false;
if(i*i==num)
{
check=true;
break;
}


}
if(check)
return i;
else return 0;

}



