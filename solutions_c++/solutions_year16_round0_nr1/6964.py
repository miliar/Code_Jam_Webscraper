#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{ int n,r ;
ifstream inp ;
ofstream outp ;
inp.open("input.txt");
outp.open("output.txt");

inp>>n ;

bool pi[10] ;
string res ;

for (int i=1 ;i<=n ;i++){
bool p =false;

  for (int j=0 ;j<=10 ;j++){pi[j]=false; }

inp>>r ;
if (r==0) {res="INSOMNIA";}
else {
        int w=1,v=0 ;
        while(!p) {
                     v=w*r;
                     w++;
                     stringstream ss;
                     ss << v;
                     string strr = ss.str();
                     int l =strr.length(); 
                          for (int k=0 ;k<l ;k++){   int z =  strr[k] - '0';   pi[z]= true; }

                          if ( pi[0]&&pi[1]&&pi[2]&&pi[3]&&pi[4]&&pi[5]&&pi[6]&&pi[7]&&pi[8]&&pi[9]){res=strr; p=true;

                          }
                    }


}
      outp<< "Case#"<<i<<":"<<res<<endl;

}


    return 0;
}