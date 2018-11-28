#include<iostream.h>
#include<conio.h>
#include<fstream.h>

void main()
{
  int nucases,number;
  int i,j,k,temp,flag=0,ind,sum=0;
  ifstream read;
  read.open("sheep.txt");
  ofstream write;
  write.open("sheepoutput.txt");
  read>>nucases;
  for(i=0;i<nucases;i++)
  { int a[10]={0,0,0,0,0,0,0,0,0,0};
    read>>number;
    if(number==0)
    {
    cout<<"Case #"<<(i+1)<<": INSOMNIA \n";
    write<<"Case #"<<(i+1)<<": INSOMNIA \n";
    continue;
    }
    temp=number;
    j=1; flag=0;
    while(flag!=1)
    {
     sum=0;
      number=temp*j;
      j++;
      for(k=number;k>0;k=k/10)
      {
        ind=k%10;                                
        for(int l=0;l<10;l++)
        {
        if(ind==l)
        a[l]=1;
        }
      }
        for(int m=0;m<10;m++)
         sum=sum+a[m];
          if(sum==10)
          {
           cout<<"Case #"<<(i+1)<<": "<<number<<"\n";
           write<<"Case #"<<(i+1)<<": "<<number<<"\n";
           flag=1;
                    }}}   read.close();
    write.close();
    getch();}
