#include <bits/stdc++.h>
#include <fstream>

using namespace std;
int tomato[32];
int potarto[9];
int well;
int testa(){
    long long nam=0, countah=0, lmeow=1;
    for(int i=2; i<11; i++){
            countah = 0;
                for(int j=2; j<=pow(i, (well)/2); j++){
                        nam=1;
                        lmeow = i%j;
                        for(int k=0; k<well-2; k++){
                            nam = (nam+lmeow*tomato[k])%j;
                            lmeow = (lmeow*i)%j;
                        }
                nam = (nam+lmeow)%j;
                    if(nam==0){
                            potarto[i-2] = j;
                        countah = 1;
                        break;
                    }
                }
            if(countah == 0){
                    if(tomato[0]==0 && tomato[1]==0 && tomato[2]==0 && tomato[3]==1){
        }
                return 0;
            }
    }
    return 1;
}
int main(){
    fstream potato;
    ofstream optato;
    string meh;
    optato.open("Answer.txt");
    potato.open("C-small-attempt0.in");
    int useless=0, num=0;
    potato >> useless;
    potato >> well;
    potato >> num;
    optato << "Case #1: \n";
    while(num>0){
        for(int i=0; i<well-2; i++){
            if(tomato[i]==0){
                tomato[i]=1;
                for(int k=0; k<i; k++){
                    tomato[k]=0;
                }
                break;
            }
        }
        if(testa()==1){
            optato << "1";
            for(int i=0; i<well-2; i++){
                optato << tomato[well-3-i];
            }
            optato << "1 ";
            for(int i=0; i<9; i++){
                optato << potarto[i] << " ";
            }
            optato << "\n";
            num--;
        }
    }
optato.close();
}
