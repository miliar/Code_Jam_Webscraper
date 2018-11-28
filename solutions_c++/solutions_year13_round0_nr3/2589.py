#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

string i2s(int i){
  std::ostringstream result;
  result << i;
  return result.str();
}

bool isfair(long long num){
  string s=i2s(num);
  for(int i=0;i<s.length();i++){
    if(s.substr(i,1)!=s.substr(s.length()-i-1,1)){return false;}        
  }     
  return true;

}

int main(int argc, char *argv[])
{
    ifstream in("in.in");    
    ofstream out("out.out");    
    
    long long num;    
    in>>num;
    long long max=1000;
    bool b[max];
    b[0]=true;
    b[1]=true;
    
    for(long long i=0;i<=max;i++){
      if(sqrt(i)==floor(sqrt(i)) && isfair((int)sqrt(i)) && isfair(i)){
        b[i]=true;
      }else{
        b[i]=false;
      }         
    }
    
    for(long long k=0;k<num;k++){
      out<<"Case #"<<k+1<<": ";
      long long a,c;
      long long num=0;
      
      in>>a>>c;             
      for(long long i=a;i<=c;i++){
        if(b[i]){num++;}
      }
      out<<num<<endl;
 
    }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
