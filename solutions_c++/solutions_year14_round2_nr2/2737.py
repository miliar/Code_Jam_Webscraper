#include<iostream>
#include<fstream>
using namespace std;


int main()
{

int cases,j,k,a,b,m,n,catalinacount;
double dd;
ifstream i;
ofstream out;
//i.open("q2input.txt");
i.open("B-small-attempt0.in");
out.open("q2output.txt");


i>>cases;
for (j=1;j<=cases;j++){
   i>>a;
   i>>b;
   i>>k;
   catalinacount=0;
   for (m=0;m<a;m++){
       for (n=0;n<b;n++){
          if (((m&n)<k)&&((m&n)>=0)) {catalinacount++;}
       }
   }
    
   out<<"Case #"<<j<<": "<<catalinacount<<endl;
}//for (j=0;j<cases;j++)


    //system("pause"); // comment it afterwards
    return 0;
}
