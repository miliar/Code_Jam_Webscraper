#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<math.h>
using namespace std;
int find(int,int);
int check_pal(string);
int square_check(int);
main()
{
ifstream fin("fs.in");
ofstream fout("fs1.txt");
 int t,i,a,b,res;
 fin>>t;
 for(i=0;i<t;i++)
  {
    fin >> a>>b;
     res=find(a,b);
     fout<<"Case #"<<i+1<<": "<<res<<endl;

  }


}

int find(int a,int b)
{
    int i,c,count=0;
    int z=0;
 for(i=a;i<=b;i++)

 {
    z=square_check(i);
    if(z==1)
   {

    c=0;

   string Result;

    ostringstream convert;

    convert << i;      // insert the textual representation of 'Number' in the characters in the stream

    Result = convert.str();

    c=check_pal(Result);
    if(c==0)
     count++;
   }

 }
 return count;
}

int check_pal(string a)
{

    int c=0,len;
    len=a.length();
    for(int j=0;j<len/2;j++)
       {
           if(a[j]==a[len-1-j])
           {

           }
           else
           {
               c=1;
               break;
           }
       }
    return c;
}

int square_check(int n)
 {
     int x,z;
  double res = sqrt(n);
  bool isSquare = fmod(res,1)== 0;
  if(isSquare==true)
   {
       string Result;

    ostringstream convert;

    convert << res;      // insert the textual representation of 'Number' in the characters in the stream

    Result = convert.str();
       x=check_pal(Result);
       if(x==1)
       isSquare=false;

   }
  if(isSquare==true)
  z=1;
  else
  z=0;

return z;

 }
