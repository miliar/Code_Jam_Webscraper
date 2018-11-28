#include <iostream>
#include <cstdio>
#define loop(i,j,k) for (int i=j;i<=k;i++)

using namespace std;

int main(){
int t,smax,clapn,nfrnds,ntmp,nfrtmp;
cin >> t;
string s;
loop(countr,1,t){
    clapn=0;
    nfrnds=0;
    cin >> smax >> s;
    //cout << smax << s;
    loop(shyNess,0,smax)
           {
               //printf("B4 level : %d  standing : %d \n",shyNess,clapn);
               ntmp = s.at(shyNess)-'0';
               if (ntmp==0)
                    continue;
               if (shyNess<=clapn)
                    {clapn+=ntmp;
                    //printf("Enough ppl: PPl incr to %d\n ",clapn);
                    }
               else {
                    nfrtmp = shyNess-clapn;
                    nfrnds += nfrtmp;
                    clapn+= ntmp+nfrtmp;
                    //printf("Not enough ppl: %d friends added, PPl incr to %d\n ",nfrtmp,clapn);
               }
               //printf("After level : %d  standing : %d added : %d \n\n\n\n",shyNess,clapn,nfrnds);
           }
    cout << "Case #"<<countr<<": " << nfrnds << endl;//Case #1: 0
}

}
