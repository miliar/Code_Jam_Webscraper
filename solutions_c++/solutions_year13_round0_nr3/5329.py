#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

int count;

int chk_palindrome(int j)
{int num,b;
double c=0,sum=0,a;
b=j;
while(b!=0){b=b/10;c++;}
c--;
num=j;
    while(num!=0)
    {a=num%10;
    sum=sum+(a*(pow(10,c)));
    num=num/10;
    c--;
    }
if(sum==j) return 1;
return 0;
}


int main(int argc, char *argv[])
{
    int t,result,d,c=0;
    double a,b,inp1,inp2,fractpart;
    ifstream myfile ("CJ3.txt");
    ofstream myfile1;
    myfile1.open ("CJ3-OUTPUT.txt");
    if (myfile.is_open())
    myfile>>t;
    for(int i=1;i<=t;i++)
    {myfile1<<"Case #"<<i<<": ";
            myfile>>a>>b;
            
            fractpart = modf (sqrt(a) , &inp1);
            fractpart = modf (sqrt(b) , &inp2);
            if(inp1*inp1!=a) inp1++;
            
            for(int j=(int)inp1;j<=(int)inp2;j++)
            {
                    result=chk_palindrome(j);
                    d=j*j;
                    result=result+chk_palindrome(d);
                    if(result==2)  c++;
            }
            myfile1<<c<<endl;
            c=0;
    }
     
     
    myfile1.close();
    
    myfile.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}
