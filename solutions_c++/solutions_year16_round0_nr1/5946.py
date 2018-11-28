#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

string s;
vector <int> atual, n;
int alg[10];
int num[100010];

void soma(int x){
    int k=0;
    for(int i=0; i<atual.size(); i++){
        k=k+num[i]+atual[i];
        if(i==atual.size()-1 && k>=10){
            atual.push_back(0);}
        atual[i]=k%10;
        k=(k-k%10)/10;
    }
}

int main(){
    int t;

    scanf("%d ", &t);

    for(int i=1; i<=t; i++){
        for(int j=0; j<10; j++){
            alg[j]=0;
        }
        atual.clear();
        n.clear();

        cin >> s;

        if(s[0]!=48){
            int aux=0;

            for(int j=s.size()-1; j>=0; j--){
                n.push_back(s[j]-48);
                atual.push_back(s[j]-48);
            }

            for(int j=0; j<n.size(); j++){
                num[j]=n[j];
            }

            while(1){
                for(int l=0; l<atual.size(); l++){
                    alg[atual[l]]=1;
                }

                for(int l=0; l<10; l++){
                    if(alg[l]==1){
                        aux=1;}
                    else{
                        aux=0;
                        break;}
                }

                if(aux==1){
                    break;}

                soma(0);
            }

            printf("Case #%d: ", i);

            for(int j=atual.size()-1; j>=0; j--){
                printf("%d", atual[j]);
            }
            printf("\n");
        }
        else{
            printf("Case #%d: INSOMNIA\n", i);
        }

        for(int j=0; j<n.size(); j++){
            num[j]=0;
        }
    }

    return 0;
}
