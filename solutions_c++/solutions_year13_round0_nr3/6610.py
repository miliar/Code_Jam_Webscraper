#include<iostream.h>
#include<fstream.h>
#include<math.h>
ifstream fin("a.txt");
ofstream fout("ans.txt");
int check(int num)
{
	int n=num,rev=0,dig;
	while(num>0)
	{
		dig=num%10;
		rev=rev*10+dig;
		num=num/10;
	}
	if(n==rev)
		return 1;
	else
		return 0;
}

void main()
{
 int a,b,c,temp=0,k=1,sp,sr,a1,a2,count;
 fin>>a;
 while(k<=a)
 {
  fin>>b;
  a1=b;
  fin>>b;
  a2=b;
  count=0;
  for(int i=a1;i<=a2;i++)
  {
	temp=0;
	temp=sqrt(i);
	if(i==(temp*temp))
	{
		sp=check(i);
		if(sp==1)
		{
			sr=check(temp);
			if(sr==1)
				count++;
		}
	}
  }
  fout<<"Case #"<<k<<": "<<count<<"\n";
  k++;
}}

