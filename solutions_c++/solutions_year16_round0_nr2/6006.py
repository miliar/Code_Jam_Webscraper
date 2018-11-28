#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

string s;

int main(){
    int t;


    char c;

    scanf("%d", &t);

    for(int i=1; i<=t; i++){
        cin >> s;

        int aux=0;
        int resp=0;

        while(1){
            int tam=0;

            for(int j=0; j<s.size(); j++){
                if(s[j]=='+'){
                    aux=1;}
                else{
                    aux=0;
                    break;}
            }
            if(aux==1){
                break;}
            resp++;

            c=s[0];
            for(int j=0; j<s.size(); j++){
                if(s[j]==c){
                    tam++;
                }
                else{
                    break;
                }
            }

            for(int j=0; j<tam; j++){
                if(c=='+' && s[j]=='+'){
                    s[j]='-';
                }else if(c=='-' && s[j]=='-'){
                    s[j]='+';
                }
            }

        }

        printf("Case #%d: %d\n", i, resp);
    }
}
