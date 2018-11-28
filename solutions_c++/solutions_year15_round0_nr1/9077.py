#include <iostream>
#include <stdio.h>
using namespace std;

int main ()
{

freopen ("A-large.in","r",stdin);
freopen ("output.txt","w",stdout);

int TestCases;

scanf("%d", &TestCases);

for(int i=0;i<TestCases;i++){

int sMax=0, counter=0 , Friends=0;
char str[1009];
scanf("%d", &sMax);
scanf("%s", str);


for(int k=0;k<=sMax;k++)
  {

if(k==0)
{

    counter+= (str[0]-'0') ;
    continue;

}


if( k >counter  && (str[k]-'0')!=0)
{

    Friends+=(k - counter );
    counter+=( (str[k]-'0') + (k - counter) );

}
else
{

    counter+=(str[k]-'0');

}

  }


printf("%s" , "Case #");
printf("%d" , (i+1));
printf("%s" , ": ");
printf("%d" , Friends);
printf("%s", "\n");
}
return 0;
}
