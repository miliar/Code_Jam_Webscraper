#include<iostream.h>
#include<fstream.h>
#include<conio.h>

void main()
{
	clrscr();
	fstream fin,fout;
	fin.open("InputA.txt",ios::in);
	fout.open("outputA.txt",ios::out);
	long int N,i,j,k=0,temp,d,flag;
	fin>>N;
	fin>>N;
	while(!fin.eof())
	{
	int A[10]={0};
	for(i=1;i<=100;i++)
	{
	      temp=N;
	      temp*=i;
	      cout<<"temp*=i"<<temp;
	      while(temp!=0)
	      {
	      d=temp%10;
	      A[d]=1;
	      temp/=10;
	      }
	      flag=0;
	      for(j=0;j<10;j++)
	      {
		if(A[j]==1)
			flag++;
	      }
	      if(flag==10)
		break;
	}
	if(flag!=10)
		fout<<"Case #"<<++k<<": INSOMNIA\n";
	else
		fout<<"Case #"<<++k<<": "<<N*i<<endl;
	fin>>N;
	}
	fin.close();
	fout.close();
}