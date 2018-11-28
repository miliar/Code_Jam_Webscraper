#include <stdio.h>

#include <stdlib.h>

#include <cmath>

#include <iostream>

#include <string>
#include <sstream>

using namespace std;

typedef long long ll;

const int MOD=1000002013;

ll min(ll a, ll b){
	return (a<b)? a : b;
}

int modcorrect(ll nu){
    nu = nu % MOD;
    if(nu<0) nu+=MOD;
    return nu;
}

int fare(int en, int ex, int N){
    return ((ll)(((ll)(N+N-ex+en+1))*((ll)(ex-en))/2L))%MOD;
}


int main(){
	
    int T;
    cin >> T;

    int N, M;
    int o[1000], e[1000], p[1000];

    ll ideal, cheated, passengers[2000], pmin;
    int stops[2000], k, stopmin;
    //bool check;

    for(int i=1;i<=T;i++){

        cin >> N >> M;

        /*o = (int*)malloc(M*sizeof(int));
        e = (int*)malloc(M*sizeof(int));
        p = (int*)malloc(M*sizeof(int));*/

        for(int j=0;j<=M-1;j++) cin >> o[j] >> e[j] >> p[j];

        ideal=0;

        for(int j=0;j<=M-1;j++) ideal=(ideal+p[j]*fare(o[j],e[j],N))%MOD;

        cheated=0;

        stopmin=0;
        k=0;
        while(stopmin<=N){
            stopmin=N+1;
            for(int j=0;j<=M-1;j++){
                if(o[j]<stopmin) stopmin=o[j];
                else if(e[j]<stopmin) stopmin=e[j];
            }
            if(stopmin<=N){
                stops[k]=stopmin;
                passengers[k]=0;
                for(int j=0;j<=M-1;j++){
                    if(o[j]==stopmin){
                        passengers[k]+=p[j];
                        o[j]=N+1;
                    }
                    if(e[j]==stopmin){
                        passengers[k]-=p[j];
                        e[j]=N+1;
                    }
                }
                k++;
            }
        }

        for(int j=1; j<=k-1; j++) if(passengers[j]<0){
            int l=j-1;
            while(passengers[j]<0){
                if(passengers[l]>0){
                    pmin=min(passengers[l],-passengers[j]);
                    passengers[j]+=pmin;
                    passengers[l]-=pmin;
                    cheated=(cheated+pmin*fare(stops[l],stops[j],N))%MOD;
                }
                l--;
            }
        }

        cout << "Case #" << i << ": ";

        cout << modcorrect(ideal-cheated);

        cout << endl;
    }


	return 0;
}
