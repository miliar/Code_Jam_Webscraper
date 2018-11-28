#include<stdio.h>
#include<fstream>
#include<iostream>
using namespace std;
int main()
{
    int t;
    int smax=0;
    char st[1002];
    int m,people,count1;

 ifstream infile;
   infile.open("C:\\Users\\Public\\A-small-attempt1.in");
  infile >> t;
  ofstream outfile;
outfile.open("C:\\Users\\Public\\abc.in", ios::out | ios::trunc );

    for(int k=1;k<=t;k++)
    {
   infile >> smax;
        infile >> st;
     count1=0;
     people=0;
     for(int i=0;i<smax+1;i++)
     {
     m=st[i]-48;
     if(i==0)
        people=people+m;
     else
        if(people>=i)
          people=people+m;
         else if (m>0)
           {
            count1+=i-people;
           people=people+count1+m;
           }
     }
     printf("%d",count1);
outfile <<"Case #"<<k<<": "<<count1<< endl;
}
return 0;
}
