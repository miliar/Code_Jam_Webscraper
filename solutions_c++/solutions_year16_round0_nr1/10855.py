#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int T,i,j,count=0;
unsigned long int N, temp;
string s;

int main()
{
 fstream file;
 ofstream outfile;
 file.open("test.txt");
 outfile.open("output.txt");
 file>>T;
 for(j=0;j<T;j++)
 {
   file>>N;
   outfile<<"Case #"<<j+1<<": ";
   i=1;
   count=0;
   int status[10]={0,0,0,0,0,0,0,0,0,0};
   while(count<10)
   {
     if(N==0)
     {
       outfile<<"INSOMNIA"<<"\n";
       break;
       }
     temp=i*N;
     while(temp>0)
     {
       if(status[(temp%10)-1]==0)
       {
         status[(temp%10)-1]=1;
	 count++;
	 }
       temp=temp/10;
       }
       i++;
       }
       if(N!=0)
       {
         outfile<<(i-1)*N<<"\n";
	 }
	 }
	 file.close();
	 outfile.close();
	 return 0;
	 }
	 
