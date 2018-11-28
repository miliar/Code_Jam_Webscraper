#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
//#include <>

using namespace std;


int main(int argc, char *argv[])
{
    ifstream myfile ("INPUT.txt");
    ofstream myfile1;
    myfile1.open ("OUTPUT.txt");
    int t;
    long long r,x,a,sum=0,i=0;
    myfile>>t;

    for(int j=1;j<=t;j++)
    {myfile>>r>>x;
    
    a=((r+1)*(r+1))-(r*r);
    sum=sum+a;
     
     
    i++;
    myfile1<<"Case #"<<j<<": ";
    while(sum<=x){
                 r=r+2;
    a=((r+1)*(r+1))-(r*r);
    sum=sum+a;
    i++;
    }
      
    i--;
    myfile1<<i<<endl;
    i=0;
    sum=0;
    }





    myfile1.close();
    myfile.close();
    system("PAUSE");
    return 0;
}
