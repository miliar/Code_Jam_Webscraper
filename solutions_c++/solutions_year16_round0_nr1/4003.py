#include<fstream>
#include<iostream>

using namespace std;


void solver(int a, bool have[], int &total)
{ int temp; 
  while(a>0)
    { temp=a%10;
      if(!have[temp]) { have[temp]=true; total++;}
      a/=10;
    } 
}


int main()
{ int a,i,j,n,total;
  bool have[10];
  ofstream output;
  output.open("output1.txt");
  
  ifstream input;
  input.open("A-large.in");
  input>>n;
  for(j=1;j<=n;j++)
  { input>>a;
    if(a==0)   output<<"Case #"<<j<<": "<<"INSOMNIA"<<endl; 
  	for(i=0;i<10;i++) have[i]=false;
   
   total=0;
  for(i=1;i<100;i++)
   { solver(a*i,have,total);
     if(total==10) { output<<"Case #"<<j<<": "<<a*i<<endl; break;}
   }
 }
 input.close();
 output.close();
   return 0;
}
