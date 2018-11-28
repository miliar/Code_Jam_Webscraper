#include<iostream>
#include <fstream>
using namespace std;  
main(int argc, char * argv[]) {
  int T,input[100],i,l;
   int result[10],j=0,X,y;
  std::fstream myfile("A-large.in", std::ios_base::in);
  ofstream myfile1,fs;
  fs.open ("output.txt", std::fstream::in | std::fstream::out | std::fstream::app);
  myfile >> T;
  for ( i = 1; i <= T; ++i) {
  myfile >> input[i];
  std::cout<<input[i];
  }
   std::cout<<"\n";
    for ( i = 1; i <= T; ++i){
   for(l=0;l<=9;l++)
   result[l]=0;
    j=0;
    if(input[i]==0)
    {
    fs<<"Case #"<<i<<":"<<" INSOMNIA\n"; 
	std::cout<<"Case #"<<i<<":"<<" INSOMNIA\n";
	continue;
    }
    while(1==1)
    {
    X=j*input[i];
    j++;
    y=X;
    while(y>0)
    {
    result[y%10]=1;
    y=y/10;
    }
    int flag=1,k;
    for(k=0;k<10;k++)
    {
    if(result[k]==0)
    {flag=0;
    break;
    }}
    if(flag==1)
    break;
    }
  	fs<<"Case #"<<i<<": "<<X <<"\n";
    std::cout<<"Case #"<<i<<": "<<X<<"\n";
    }
}
