#include<iostream>
#include<algorithm>
using namespace std;
int main() {
    freopen( "B-small-attempt0.in", "r", stdin );
    freopen( "B-small-attempt0.out", "w", stdout );
    int T,N,k=1,i,j,war,decWar;
    double nao[10],ken[10];
    cin>>T;
    while(T--) {
               cin>>N;
               for(i=0;i<N;i++)        cin>>nao[i];
               for(i=0;i<N;i++)        cin>>ken[i];
               sort(ken,ken+N);
               sort(nao,nao+N);
               for(i=0,j=0;i<N;j++)
                                while(i<N && ken[i++]<nao[j]);
               if(ken[N-1]<nao[j-1])        j--;
               war=N-j;
               for(i=0,j=0;i<N;j++)
                                  while(i<N && nao[i++]<ken[j]);
               if(nao[N-1]<ken[j-1])        j--;
               decWar=j;
               cout<<"Case #"<<k++<<": "<<decWar<<" "<<war<<endl;
    }
    
    return 0;
}
