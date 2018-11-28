#include<iostream>
#include<cstdio>
#include<algorithm>


using namespace std;

double nao[1042],ken[1042];

int main(){
        int T,testCase = 1,N;
        double temp;
        cin>>T;
        while(testCase <= T){

                scanf("%d",&N);
                for(int i = 0; i < N; i++){
                        scanf("%lf",&nao[i]);
                }
                for(int i = 0; i < N; i++){
                        scanf("%lf",&ken[i]);
                }

                sort(nao,nao + N);
                sort(ken,ken + N);
                /*for(int i = 0; i < N; i++){
                        cout<<nao[i]<<" ";
                }
                cout<<"\n";
                for(int i = 0; i < N; i++){
                        cout<<ken[i]<<" ";
                }
                cout<<"\n";
                */
                int war = 0;
                int nHead = 0, nTail = N-1, kHead = 0, kTail = N-1;
                while(nHead <= nTail && kHead <= kTail){
                        if(nao[nHead] > ken[kHead]){
                                war++;
                                kHead++;
                        }
                        else{
                                nHead++;
                                kHead++;
                        }
                }

                int dWar = 0;
                nHead = 0, nTail = N-1, kHead = 0, kTail = N-1;
                while(nHead <= nTail && kHead <= kTail){
                        if(nao[nHead] < ken[kHead]){
                                kTail--;
                                nHead++;
                        }
                        else if(nao[nHead] > ken[kHead]){
                                dWar++;
                                nHead++;
                                kHead++;
                        }
                }

                printf("Case #%d: %d %d\n",testCase,dWar,war);

                testCase++;
        }
}
