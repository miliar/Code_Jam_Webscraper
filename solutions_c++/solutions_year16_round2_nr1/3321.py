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
#define Fox(i,n) for (i=0; i<n; i++)
#define Fox1(i,n) for (i=1; i<=n; i++)
#define FoxI(i,a,b) for (i=a; i<=b; i++)
#define FoxR(i,n) for (i=(n)-1; i>=0; i--)
#define FoxR1(i,n) for (i=n; i>0; i--)
#define FoxRI(i,a,b) for (i=b; i>=a; i--)
#define Foxen(i,s) for (i=s.begin(); i!=s.end(); i++)
#define Min(a,b) a=min(a,b)
#define Max(a,b) a=max(a,b)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))
#define pb push_back
#define mp make_pair
#define x first
#define y second


const int inf = 2100000000;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

const char* const number[] =
{
    "ZERO",
    "TWO",
    "SIX",
    "SEVEN",
    "EIGHT",
    "FIVE",
    "THREE",
    "FOUR",
    "NINE",
    "ONE",
};

int num_l[] = {4,3,3,5,5,4,5,4,4,3};

int num_r[] = {0, 2, 6, 7, 8,5, 3, 4, 9, 1};

int nCases;
#define MAX  2000 
char S[MAX];
char S1[MAX];
char A[MAX];
int tmp[5];
int R[MAX];
int H, L;
char *p;
int  pl;

static void sort(int *a, int start, int end)
{
    int swap;
    int i, c, d;

    for (c = start; c <= end; c++)
    {
        for (d = start ; d < end  + start -c ; d++)
        {
          if (a[d] > a[d+1]) /* For decreasing order use < */
          {
            swap       = a[d];
            a[d]   = a[d+1];
            a[d+1] = swap;
          }
        }
    }
}

static void remove(char *r, int len, int id)
{
    int i;
    FoxI(i, id, len-1)
    {
        r[i]=r[i+1];
    }
}


static int find_l(void)
{
    int j;
    for0n(j,MAX)
    {
        if(S[j]==0)
        {
            return j;
        }
    }
    return j;
}

static int find_one(int id)
{

    int i, j, flag;
    int LL = L;
    memcpy(S1, S, sizeof(S));

    for(j=0;j<num_l[id];j++)
    {
        flag = 0;
        for(i=0;i<LL;i++)
        {
            if(S1[i]==number[id][j])
            {
                flag = 1;
                break;
            }
        }
        if(flag == 0)
            return 0;
        remove(S1, LL, i);
        LL--;
    }
    memcpy(S, S1, sizeof(S));
    L = LL;
    R[H] = num_r[id];
    printf("+++++++++ R %d H %d L %d \n", R[H], H, L);
    H++;
    return 1;
}

static void find_all(int id)
{
    int i = 1;

    while (i==1)
    {
        i=find_one(id);
    }
    return;
}

static int find_r(int id)
{
    int i, j, flag;
    int LL = L;
    memcpy(S1, S, sizeof(S));
    printf("L = %d ======= %d\n", L, id);
    for(i=0;i<L;i++)
    {
        printf("%c", S[i]);
    }
    printf("==========\n");
    memset(tmp, 0, sizeof(tmp));

    for(j=0;j<10;j++)
    {
        find_all(j);
    }
    
}

static int find_result(void)
{
    int l, i;
    L = find_l();
    printf("L = %d\n", L);
    for(i=0;i<L;i++)
    {
        printf("%c", S[i]);
    }
    printf("\n");
    while(L>0)
    {
        for(i=0;i<10;i++)
        {
           if(L>0)
           {
               find_r(i);
           }
        }
    }
   sort(R, 0, H-1);
    return 0;
}

int main (int argc, char **argv)
{
  int i,j, rc;

  if (argc < 2) 
 {
    cout << "Specify input file" << endl;
    return -1;
  }

  fstream inFile(argv[1], fstream::in);
  fstream outFile("A_out.txt", fstream::out);

  inFile >> nCases;
  for0n(i,nCases) {
     memset(S, 0, sizeof(S));
     memset(A, 0, sizeof(A));
     memset(R, 0, sizeof(R));
     H = 0;
     inFile >> S;
     outFile << "Case #"<< i+1 << ": " ;
     find_result ();
    printf("@@@@@@@@@@@@@ R %d H %d L %d \n", R[H], H, L);
     for(j=0;j<H;j++)
     {
         outFile << R[j];
     }
     outFile << endl;

  }
  outFile.close();
  return 0;
}
