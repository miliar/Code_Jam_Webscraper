#include <cstdlib>
#include <iostream>

using namespace std;

long long mas[10000];

int N=5;

int IsPal(long long x)
{long long y=0;
 if(x<10)return 1;
 while(x>y)
 {y=y*10+x%10;
  if(y==x)return 1;
  x/=10;
 }
 return x==y;
}

int RamFa(long long x)
{if(x<2)return x;
 int L=1,n=N,k; 
 if(mas[n]<x)return N;
 k=(L+n)/2;
 while(n-L>0)
 {if(x==mas[k])return k;
  if(x<mas[k])n=k-1; else L=k+1;
  k=(L+n)/2;
 }
 if(x>=mas[k])return k;
 else return k-1;
}

int main(int argc, char *argv[])
{long long x=1000000000L,i;
 int T,L,A,B;
 for(i=1;i<=3;i++)mas[i]=i*i;
 mas[4]=121;
 mas[5]=484;
 freopen("C-small-attempt0.in","r",stdin);
 freopen("C-small.out","w",stdout);
 cin>>T;
 for(L=1;L<=T;L++)
 {cin>>A>>B;
  cout<<"Case #"<<L<<": "<<RamFa(B)-RamFa(A-1)<<endl;
 }
//    system("PAUSE");
    return EXIT_SUCCESS;
}
