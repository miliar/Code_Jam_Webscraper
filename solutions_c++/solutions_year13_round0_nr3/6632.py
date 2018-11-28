#include <iostream>
#include <fstream>
#include <math.h>
#include <sstream>
#include <vector>
#include <map>
using namespace std;
int cases;
int a,b;
int ans=0;
string str, str2;
bool checkPal(string str1)
{
    int j= (str1.length()) - 1;

    for(unsigned int i=0; i < (str1.length()) / 2; i++)
    {
        if(str1[i] != str1[j-i])
            return false;

    }
    return true;
}
int main()
{
    ifstream in("C-small-attempt0.in");
    ofstream out("output-smal.out");
    in >> cases;
    for(int k=0; k < cases; k++)
    {
        in >> a >> b;
        for(; a <= b; a++)
        {
            stringstream ss;
            ss << a;
            str=ss.str();

            stringstream aa;
            aa << sqrt(a);
            str2=aa.str();

            if(checkPal(str) && checkPal(str2) )
                ans++;
        }

       out <<"Case #" << k+1 << ": " << ans<<endl;
       ans=0;
    }
}
