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
char R[100]; 
int b = 0;

static int find_l(void)
{
    int i, j =0;
    
    for(i=0;i<100;i++)
    {
        if(R[i]==0)
            break;
        j++;
    }
    printf("length is %d\n", j);
    return j;
}

static int find_result(void)
{
    
    int l; 
    int p =0;
    int c = 0;
    int i;

    l=find_l();
    if(R[0] =='+')
        p =1;
    for(i=0;i<l;i++)
    {
        if((R[i]=='+')&&(p==1))
            continue;
        else if((R[i]=='-')&&(p==1))
        {
            p=0;
            c++;
        }
        else if((R[i]=='+')&&(p==0))
        {
            p=1;
            c++;
        }
        else if((R[i]=='-')&&(p==0))
        {
            continue;
        }
    }
    if(R[l-1]=='-')
        c++;
    return c;
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
  fstream outFile("output_B1.txt", fstream::out);

  inFile >> nCases;
  for0n(i,nCases) {
     for(j=0;j<100;j++)
     {
         R[j]=0;
     }
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
