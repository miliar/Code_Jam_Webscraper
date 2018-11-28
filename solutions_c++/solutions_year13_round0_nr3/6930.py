#include <iostream>
#include <algorithm>
#include <sstream>
#include <string.h>
#include <math.h>
#include <fstream>
using namespace std;
long int sqr;
bool raiz(long int n)
{

    sqr=sqrt(n);
    if(sqr*sqr==n)return true;
    else return false;
}
string convertInt(long int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}



bool palindromo(long int n)
{
    string S;
    char str[20];
    char str2[20];

    S=convertInt(n);

    strcpy(str, S.c_str());


    strcpy(str2,str);


    reverse(str,str+strlen(str));

    if(strcmp(str,str2)==0){return true;}
    else {return false;}

}

int main()
{
    long int T, A,B,i,j,cont;
    ofstream fout ("test.out");
    ifstream fin ("C-small-attempt0.in");
    fin>>T;
    j=0;
    while(T--)
    {
        j++;
        cont=0;
        fin>>A>>B;
        for(i=A;i<=B;i++)
        {
            if(palindromo(i)&&raiz(i)&&palindromo(sqr)){cont++;}
        }
        fout<<"Case #"<<j<<": "<<cont<<endl;
    }


}
