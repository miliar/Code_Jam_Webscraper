#include<malloc.h>
#include<stdio.h>
#include<fstream>
using namespace std;
long int count;
int main()
{
 int test;
scanf("%d",&test);
ofstream myfile;
  myfile.open ("example.txt");
long int a,b,k;
long int e,f,g;
int i;
for(i=0;i<test;i++)
{
count =0;
scanf("%ld %ld %ld",&a,&b,&k);
for(e=0;e<a;e++)
{
for(f=0;f<b;f++)
{
if((e&f)<k)
count++;
}
}  
myfile<<"Case #"<<i+1<<": "<<count<<"\n";
}
myfile.close();
return 0;
}
