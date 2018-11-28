#include <iostream>
#include <cstdio>
#include <stdlib.h>

using namespace std;

#define iFor(i,n) for(int i=0;i<=n;i++)
#define iFor2(i,n,m) for(int i=n;i<=m;i++)
#define iForDec(i,n,m) for(int i=n;i>m;i--)

int N;
//string s;
#define SMALL
#define LARGE

int main(){
    freopen("a.txt","rt",stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
    cin>>N;
    int Smax = 0;
    string s;
    iFor(i,N-1){
        int fReq=0;
        int peop=0;
        int t=0;
         cin>>Smax;
         getchar();
         getline(cin,s);
         iFor(j,Smax){
             char h= s.at(j);
               char *a = &h;
               t=atoi(a);
               //cout<<t;
               if(t==0){

               }else{
                   if(j<=peop){
                        peop+=t;
                   }else{
                        fReq = fReq + (j-peop);
                        peop=j+t;
                   }
               }
         }
         printf("Case #%d: ", i+1);
         cout<<fReq<<"\n";
    }
    return 0;
}
