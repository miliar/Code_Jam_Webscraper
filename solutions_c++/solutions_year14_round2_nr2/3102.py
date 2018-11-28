//in the name of GOD
#include<fstream.h>
#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
void main()
{
int cases,done=0;
long long number;
long long i,j,k,a,b,n,and;
ifstream ifile("2rba.in",ios::in);
ofstream ofile("2rba.out",ios::out);
ifile>>cases;

while(done<cases)
 {
 ifile>>a;
 ifile>>b;
 ifile>>n;
 number=0;
 for(i=0;i<a;i++)
 {
 for(j=0;j<b;j++)
 {
 and=i&j;
 if(and<n)
 {
 number++;
 }
 }
 }
 done=done+1;
 ofile<<"Case #"<<done<<": "<<number<<"\n";
 }

}