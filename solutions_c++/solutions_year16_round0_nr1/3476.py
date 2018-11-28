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
long long R; 
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
    int n = 1;
    if(R ==0)
       return -1;
    
    while (b!= 0x3ff)
    {
        find_d(n*R);
        rc = n*R;
        n++;
    }
    return rc;
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
  fstream outFile("output_A1.txt", fstream::out);

  inFile >> nCases;
  for0n(i,nCases) {
     b = 0;
     inFile >> R;
     outFile << "Case #"<< i+1 << ": " ;
     rc = find_result ();
     if(rc<0)
         outFile << "INSOMNIA" << endl;
     else
         outFile << rc << endl;

  }
  outFile.close();
  return 0;
}
