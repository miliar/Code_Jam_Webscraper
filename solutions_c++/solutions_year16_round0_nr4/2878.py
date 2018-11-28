#include <string.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include <fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define for0n(i,n) for(i=0;i<n;i++)
#define for1n(i,n) for(i=1;i<=n;i++)
#define forn(i,j,n) for(i=j;i<n;i++)

const int inf = 2100000000;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;



int nCases;
long long K, C, S; 
long long R[100];
int b = 0;
static void find_d(long long i)
{
    int j, k;
    k = i;
    while(i>0)
    {
        j=i%10;
        b |= 1<<j;
        i=i/10;
    }
    //printf("number %d, b = 0x%x\n", k, b);
}

static int find_result(void)
{
    int rc = 0;
    long long i, j;
    long long c=0;
    int flag = 0;
    memset(R, 0, sizeof(R));
    if(S==K)
    {
       for(i=0;i<K;i++)
       {
           R[i] = i+1;
       }
       return 1;
    }
    if (C==1)
    {
        if(S<K)
            return -1;
    }
    c=1;
    if(K%2==0)
    {
         if(S<K/2)
             return -1;
         else
         {
             c=1;
             for(i=0;i<K/2;i++)
             {
                c=2*K*(i);
                R[i] = 2* (i + 1) + c;
             }
             if(S>K/2)
             {
                j = 1;
                for(i=K/2;i<S;i++)
                {
                   R[i] = j+2;
                   j++;
                }
             }
             return 1;
         }
    }
    else
    {
         if(S<K/2+1)
             return -1;
         else
         {
             c=1;
             for(i=0;i<K/2+1;i++)
             {
                c=2*K*(i);
                if(2*(i+1)>K)
                {
                    R[i] = c+K;
                }
                else
                    R[i] = 2*(i + 1) + c;
             }
             if(S>K/2+1)
             {
                j = 1;
                for(i=K/2+1;i<S;i++)
                {
                   R[i] = j+2;
                   j++;
                }
             }
             return 1;
         }
        
    }
 }

int main (int argc, char **argv)
{
  int i,j, rc;

  if (argc < 2) 
 {
    printf("Specify input file\n");
    return -1;
  }

  fstream inFile(argv[1], fstream::in);
  fstream outFile("output_D1.txt", fstream::out);

  inFile >> nCases;
  for0n(i,nCases) {
     b = 0;
     inFile >> K >> C >> S;
     outFile << "Case #"<< i+1 << ": " ;
     rc = find_result ();
     if(rc<0)
         outFile << "IMPOSSIBLE" << endl;
     else
     {
         for(j=0;j<S;j++)
         {
             outFile << R[j] << " ";
         }
         outFile << endl;
     }
  }
  outFile.close();
  return 0;
}
