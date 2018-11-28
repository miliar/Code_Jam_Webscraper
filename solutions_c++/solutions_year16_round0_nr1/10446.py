#include <iostream.h>
#include <fstream.h>
#include <string.h>

int sum(int a[10])
{int c=1;
  for(int i=0;i<10;i++)
{  if(a[i]==0)
c=0;
}
  return(c);
}
long cal(long sheep)
{
long  t=0,n,i;
int ch[10],k=0;

for(i=0;i<10;i++)
ch[i]=0;
   i=sheep;
  while(k!=1&&t<=200)
 {

  t++;
i=sheep*t;
  while(i!=0)
  {n=i%10;
  i/=10;

   ch[n]=1;


	}
 k=sum(ch);

 }
if(sum(ch)==1)
return(t*sheep);
else
return(0);





}
void main () {

  long i;
  char *inname = "input.txt";
  ifstream infile(inname);
  if (!infile) {
 cout << "There was a problem opening file " << inname << " for reading." << endl;
 }
else{
  cout << "Opened " << inname << " for reading." << endl;
	     long x=0;

 while (infile >> i&&x!=100)
 { cout << "Value from file is " << i << endl;
	x++;
fstream td;
td.open("output.txt",ios::out|ios::app);
long y=cal(i);
if(y!=0)
td<<"\nCase #"<<x<<": "	<<y;
else
td<<"\nCase #"<<x<<": INSOMNIA";

td.close();

  }

  }

  }