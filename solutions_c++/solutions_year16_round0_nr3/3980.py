#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;
const int LEN=14;
const int MAXDB=50;
const long long MEDDIG=34000000;

long long str_to_int(char str[] ,int base)
{
    char * en;
    return strtol (str,&en,base);
}

std::string binary(long int x)
{
    std::string s;
    do
    {
        s.push_back('0' + (x & 1));
    } while (x >>= 1);
    while (s.length()<LEN)
    {
        s.push_back('0');
    }
    std::reverse(s.begin(), s.end());
    return s;

}

long oszto(long long szam, vector<int>& primes)
{
    for (int i=0; i<primes.size() && primes[i]*primes[i]<=szam; i++)
    {
        if (szam%primes[i]==0)
        { return primes[i];}
    }

    return 0;
}

int main()
{

ofstream fki("ki.txt");
fki<<"Case #1: "<<endl;
vector<int> sieve;
vector<int> primes;
int M=MEDDIG;
for (int i = 1; i < M+ 1; ++i)
   sieve.push_back(i);   // you'll learn more efficient ways to handle this later
sieve[0]=0;
for (int i = 2; i < M + 1; ++i) {   // there are lots of brace styles, this is mine
   if (sieve[i-1] != 0) {
      primes.push_back(sieve[i-1]);
      for (int j = 2 * sieve[i-1]; j < M + 1; j += sieve[i-1]) {
          sieve[j-1] = 0;
      }
   }
}

cout<<"szita kesz"<<endl;



    int db=0;
    for (int i=0; i<16384 && db<MAXDB; i++)
    {
        std::string str = "1"+binary(i)+"1";
        char *cstr = &str[0u];
        bool jo=true;
        vector <long> Osztok;
        for (int j=2; j<=10 && jo; j++)
        {
            long long szamunk=str_to_int(cstr,j);
            long O=oszto(szamunk,primes);
            if (O!=0)
            {
                Osztok.push_back(O);
            }else{jo=false;}
        }
        if (jo)
        {
            fki<<cstr<<" ";

            for (int k=0; k<Osztok.size(); k++)
            {
                fki<<Osztok[k]<<" ";
            }
            fki<<endl;
            db++;
        }

    }
    cout<<db;
    fki.close();
    return 0;
}
