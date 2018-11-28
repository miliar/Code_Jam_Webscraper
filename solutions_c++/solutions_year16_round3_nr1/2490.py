#include<iostream>
#include<map>
#include<string>
#include<iterator>
#include<regex>
#include<vector>
#include<algorithm>

#define MAX(a,b) (a > b ? a : b)
#define MIN(a,b) (a < b ? a : b)

typedef __int128_t i128 ;
typedef __uint128_t u128 ;
typedef __int64_t i64 ;
typedef __uint64_t u64 ;
typedef __int32_t i32 ;
typedef __uint32_t u32 ;

#define DEBUG 0
#define PF printf
#define EPF(...) fprintf(stderr, __VA_ARGS__)
#define DPF if (DEBUG) PF
#define SF scanf
#define SFD(Int) scanf("%d",&Int);
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)

using namespace std;

int cmp(const void *a,const void *b) {return (*(int *)b-*(int *)a);}

int T,N,S;

int P[1000],cP[1000];

int imax(int *P) {
  int max=0;
  int imax=0;
  F0(i,N)
    if(P[i]>max) {
      max=P[i];
      imax=i;
    }
  return imax;

}

int i2max(int *P) {
  int cP[1000];
  F0(i,N) cP[i]=P[i];
  cP[imax(cP)]=0;
  return imax(cP);

}

int maj(int *P,int S) {
    int i=imax(P);
    F0(i,N)
      if (P[i]*2>S)
        return 1;

    return 0;
}


void solve(int S) {

 //if (maj(P,S))  EPF("maj");

  if (S==0)
    return;

  if (S%2==1) {
    int im=imax(P);
    P[im]--;
    PF("%c ",im+'A');
    solve(S-1);
    return;
  }

  if (S%2==0) {
    int im=imax(P);
    int i2=i2max(P);
    P[im]--;
    P[i2]--;

    PF("%c%c ",im+'A',i2+'A');

    solve(S-2);
    return;
  }

}

int main() {

  cin >> T;
  F0(t,T) {
    cin >> N;
  //  cout << N << endl;
    memset(P,0,1000*sizeof(int));
    S=0;
    F0(n,N)  {
      cin >> P[n];
      S+=P[n];
    }
  //  F0(n,N)   cout << P[n] << " " ;
  PF("Case #%d: ",t+1);
  solve(S);
  cout << endl;
   }



}
