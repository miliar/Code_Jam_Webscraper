#include<iostream.h>
#include<math.h>
#include<fstream.h>
#include<string.h>
//using namespace std;
int palindrome(int );
int square(int i)
{
 return i*i;
}              
int main()
{
int i,j,k,m,n,p,t;
int c,num;
c=0;
char file[50];
cout<<"enter the input file name with extension: ";
cin>>file; 

ifstream infile;
infile.open(file);
ofstream ofile;
ofile.open("output.txt");
if(!infile)
{
 cout<<"error in opening the file";
 return 0;
}
infile>>t;


while(c!=t)
{
 k=-1;

infile>>m;

 infile>>n;
num=m;

       for(i=sqrt(m);i<=sqrt(n);i++)
       {
        for(j=num;j<square(i+1)&&j<=n;j++)
         {
          if(square(i)==j && palindrome(j)&&palindrome(sqrt(j)))
           k++;  
           
         }
         num=square(i+1);  
        }
 ofile<<"Case #"<<c+1<<": "<<k+1<<endl;
c++;
}

return 0;
}



int palindrome(int i)
{
int temp=i;
 int reverse=0;
   while( temp != 0 )
   {
      reverse = reverse * 10 + temp%10;
      temp=temp/10;
   }
 
   if ( i == reverse )
      return 1;
      
 else
   return 0;
}
