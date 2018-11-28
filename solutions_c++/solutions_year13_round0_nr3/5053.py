#include<iostream>
#include<fstream>
using namespace std;
long isSquare(long n)
{

long beg=0;
long end=n;
long mid;
long midsq;
bool issquare=false;
while(beg<=end)
{
	mid=(beg+end)/2;
	midsq=mid*mid;
	if(midsq==n)
	{
		issquare=true;
		break;
	}
	else if(midsq<n)
	beg=mid+1;
	else
	end=mid-1;
}
return ((issquare==true)?mid:-1);
}
bool isPalindrome(long n)
{
long reverse=0, rem,temp;
  temp=n;
  while(temp!=0)
  {
     rem=temp%10;
     reverse=reverse*10+rem;
     temp/=10;
  }  
  if(reverse==n)  
      return(true);
  else
      return(false);

}
int main()
{
int count;
long temp;
char ch[50];
int T;
long A,B;
ifstream iff;
ofstream off;
iff.open("C:\\Users\\him\\Desktop\\GOOGLE\\C-small-attempt0.in");
off.open("C:\\Users\\him\\Desktop\\GOOGLE\\output.txt");
iff.getline(ch,50);
T=atoi(ch);

for(int i=0;i<T;i++)
{
count=0;
iff.getline(ch,50,' ');
A=atoi(ch);
iff.getline(ch,50);
B=atoi(ch);
for(int j=A;j<=B;j++)
{
if((temp=isSquare(j))!=-1)
		if(isPalindrome(j) && isPalindrome(temp))
			count++;
}
off<<"Case #"<<i+1<<": "<<count<<"\n";
}
iff.close();
off.close();
system("pause");
}