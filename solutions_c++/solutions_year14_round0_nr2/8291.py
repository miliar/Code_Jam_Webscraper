#include<iostream>
#include <iomanip>
#include<fstream>
using namespace std;


int main()
{

int cases, j,flag;
 long double C, F, X,f1,sum,sum2,compare;

ifstream i;
ofstream out;
//i.open("q2input.txt");
i.open("B-large.in");
out.open("q2output.txt");

i>>cases;
for (j=1;j<=cases;j++){
 i>>C;
 i>>F;
 i>>X;
 
 sum=0;sum2=0;compare=0;
 f1=2;
 flag=0;
 
 while(flag==0){
               sum2=sum+(X/f1);
               sum=sum+(C/f1);
               f1=f1+F;
               if (compare==0) compare=sum2;
               else {
                    if (compare>sum2){compare=sum2;}
                    else if (compare<sum2) {flag++;}
                    } 
 }
 int st=1;
 if (compare<10) st=8;
 else if (compare<100) st=9;
 else if (compare<1000) st=10;
 else if (compare<10000) st=11;
 else if (compare<100000) st=12;
 out<<"Case #"<<j<<": "<<setprecision(st)<<compare<<endl;
 
}//for (j=1;j<=cases;j++)


   // system("pause"); // comment it afterwards
    return 0;
}
