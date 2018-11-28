
#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

bool isPolindrome (int num)
{
    int n = num;
 int rev = 0;
 int dig =0;
 while (num > 0)
 {
      dig = num % 10;
      rev = rev * 10 + dig;
      num = num / 10;
 }
 
 if (n == rev )
     return true;
 return false;
}

bool isSquare(int num)
{
    double d_sqrt = sqrt( num );
int i_sqrt = d_sqrt;
if ( d_sqrt == i_sqrt )
    return true;
return false;
}


int main(int argc, char** argv) {
   
    ifstream ifs ("Input.ini");
    ofstream ofs("Output.ini");
    int T, A, B;
    int counter=0;
    ifs >> T;
    
    for (int i=1; i<= T; i++)
    {
        ifs >> A >> B;
        
        for (int j=A; j<= B; j++)
        {
            if (isPolindrome(j) && isSquare(j) && isPolindrome(sqrt(j)))
                counter ++;
        }
        
        ofs << "Case #"<<i<<": "<<counter<<endl;
        
        counter =0;
    }
    

    
    
    return 0;
}

