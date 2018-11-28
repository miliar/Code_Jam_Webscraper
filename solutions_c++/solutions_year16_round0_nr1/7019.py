#include <bits/stdc++.h>

using namespace std;
map<int, int> m;

void addToMap(long long int N){
    long long int pembagi = 1000000000;
    while(N<pembagi)pembagi/=10;
    while(N){
        if(pembagi<=N){
            long long int hsl = N/pembagi;
            m.insert(make_pair(hsl,0));
            N%=pembagi;
        }
        pembagi/=10;
        if(N<pembagi){
            m.insert(make_pair(0,0));
        }
    }

}

int main()
{
    long long int T,N;

    scanf("%lld",&T);

    for(long long int i=1;i<=T;i++){
        scanf("%lld",&N);
        if(N!=0){
            m.clear();
            long long int j=0,hasil;
            for( j=1;m.size()<10;j++){

                /*for(map<int, int>::iterator it = m.begin(); it!=m.end();it++){
                    printf("%d ",it->first);
                }
                printf("\n");*/
                hasil = j*N;
                addToMap(hasil);
            }
            printf("Case #%lld: %lld\n",i,hasil);
        }else{
                printf("Case #%lld: INSOMNIA\n",i);
        }

    }

    return 0;
}
