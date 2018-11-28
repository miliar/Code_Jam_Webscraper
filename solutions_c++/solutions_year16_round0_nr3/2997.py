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
 
int N, J;
long long  N1[9], F[9];
char B[16];

static int isLastOne(unsigned int v)
{
    if((v&1) ==0)
        return 0;
    return 1;
}

static long long isGood(long long v)
{
    long long i, j, k;
    for(i=2;i<12;i++)
    {
        if(v%i ==0)
            return i;
    }
    return 0;
}

static long long find_result(unsigned int i)
{
    int j, d, k, l;
    long long t;
    memset(B, 0, sizeof(B));
    memset(N1, 0, sizeof(N1));
    memset(F, 0, sizeof(F));

    d=0;
    if(isLastOne(i) != 1)
        return -1;
    for(j=0;j<N;j++)
    {
        if(isLastOne(i))
        {
            B[N-j-1]='1';
            for(k=0;k<9;k++)
            {
                t = 1;
                for(l=0;l<d;l++)
                {
                    t=t*(k+2);
                }
                N1[k] += t;
            }
        }
        else
            B[N-j-1]='0';
        d++;
        i = i >> 1;
    }
    for(j=0;j<9;j++)
    {
  //      printf("N [%d] = %d,  %s\n", j, N1[j],  B);
        F[j] = isGood(N1[j]);
  //      printf(" ---- F = %d\n", F[j]);
        if(F[j]==0)
           return -1;
    }
    return 1;
}


int main (int argc, char **argv)
{
  int i,j, k, rc;
  unsigned int max;
  unsigned int start, end;

  if (argc < 2) 
 {
    printf("Specify input file\n");
    return -1;
  }

  fstream inFile(argv[1], fstream::in);
  fstream outFile("output_C1.txt", fstream::out);

  inFile >> nCases;
  inFile >> N >> J;
  printf("N %d J %d\n", N, J);

     j=0;
     if(N==32)
     {
         start = 0x80000001;
         end = 0xffffffff;
     }
     else
     {
         start = 0x8001;
         end = 0xffff;
     }

           outFile << "Case #1: " <<endl ;
     for(i=start;i<end;i++)
//     for(i=0x21;i<0x3f;i++)
     {
        if(j==J)
        {
            outFile.close();
            return 0;
        }
        rc = find_result(i);
        if(rc==1)
        {
           outFile << B;
           for(k=0;k<9;k++)
           {
              outFile << " " << F[k];
           }
           outFile << endl;
           j++;
        }
     }
  outFile.close();
  return 0;
}
