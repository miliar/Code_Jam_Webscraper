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
#define MAX  1001 
char S[MAX];
char A[MAX];
char tmp[MAX];
int b = 0;

static int find_l(void)
{
    int j;
    for(j=0;j<MAX;j++)
    {
        if(S[j]==0)
        {
            return j;
        }
    }
    return j;
}

static void input (int i)
{
    int j;
    memset(tmp, 0, sizeof(tmp));
    if(i==0)
    {
        A[i]=S[i];
        return;
    }
    if(S[i]<A[0])
    {
       A[i]=S[i];
       return;
    }
    tmp[0]= S[i]; 

    for(j=1;j<i+1;j++)
    {
        tmp[j]=A[j-1];
    }
    memcpy(A, tmp, i+1);
}

static int find_result(void)
{
    int l, i;
    l = find_l();
    for(i=0;i<l;i++)
    {
        input(i);
    }
    return 0;
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
  fstream outFile("output_A2.txt", fstream::out);

  inFile >> nCases;
  for0n(i,nCases) {
     memset(S, 0, sizeof(S));
     memset(A, 0, sizeof(A));
     inFile >> S;
     outFile << "Case #"<< i+1 << ": " ;
     find_result ();
         outFile << A << endl;

  }
  outFile.close();
  return 0;
}
