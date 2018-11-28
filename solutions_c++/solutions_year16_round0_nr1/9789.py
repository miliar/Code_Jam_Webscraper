#include<iostream.h>
#include<conio.h>
#include<fstream.h>

void main()
{
  int nucases,num;
  int i,j,k,temp,flag=0,ind,sum=0;
  ifstream read;
  read.open("sheep.txt");
  ofstream write;
  write.open("sheepoutput.txt");
  read>>nucases;
  for(i=0;i<nucases;i++)
  { int a[10]={0,0,0,0,0,0,0,0,0,0};
    read>>num;
    if(num==0)
    {
    cout<<"Case #"<<(i+1)<<": INSOMNIA \n";
    write<<"Case #"<<(i+1)<<": INSOMNIA \n";
    continue;
    }
    temp=num;
    j=1; flag=0;
    while(flag!=1)
    {
     sum=0;
      num=temp*j;
      j++;
      for(k=num;k>0;k=k/10)
      {
        ind=k%10;
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
           cout<<"Case #"<<(i+1)<<": "<<num<<"\n";
           write<<"Case #"<<(i+1)<<": "<<num<<"\n";
           flag=1;
                    }}}   read.close();
    write.close();
    getch();}
