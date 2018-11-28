#include <iostream>
#include <string>
#include <fstream>
#include "math.h"

using namespace std;

string tostring(int n,string str)// you call it tostring(n,"");
{
       if(n ==0)return str;
       else
       {
           str = (char)((n%10)+48)+str;
           n /= 10;
           return tostring(n, str);
       }
}

bool pole(string str)
{
     if(str.length()<=1)return true;
     if(str[0] == str[str.length()-1]){
               str.erase(str.length()-1,1);
               str.erase(0,1);
               return pole(str);
     }
     else return false;
}

bool pol(int n)
{
     string str = tostring(n,"");
     return pole(str);
}





int main()
{
    
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small-attempt0.out");
    
    int T;
    long long A,B;
    int counter;
    fin >> T;
    
    for(int j=0;j<T;j++)
    {
            counter =0;
            fin >> A >> B;
            
            for(int i=A;i<=B;i++)
            {
                    int x = sqrt(i);
                    if( x != sqrt(i)) continue;
                    if(pol(i) && pol(x) ){counter++;}
            }
            fout << "Case #" << j+1 << ": " << counter <<  endl;
    }
    return 0;
}
