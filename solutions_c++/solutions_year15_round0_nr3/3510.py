#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0); cin.tie
using namespace std;

int T;
int N, M;
string a;

string original;

void copia() {
    original.clear();
    for(int i = 1; i<=M; i++) {
        for(int j = 0; j < a.size(); j++)
            original.push_back(a[j]);
    }
}

int busca(int pos, char car) {
    char aux = 1;
    int negativo = 0;
    while((aux!=car||negativo)&&pos+1<original.size()){
        pos++;
        if(aux==1){
            aux=original[pos];
        } else {
            if(aux==original[pos]){
                aux = 1;
                negativo^= 1;
            } else {
                if(aux=='i'){
                    if(original[pos]=='j')
                        aux='k';
                    if(original[pos] == 'k') {
                        negativo^=1;
                        aux = 'j';
                    }
                } else {
                    if(aux=='j') {
                        if(original[pos]=='i'){
                            negativo^=1;
                            aux = 'k';
                        }
                        if(original[pos]=='k')
                            aux='i';
                    }  else {
                        if(original[pos]=='i')
                            aux='j';
                        if(original[pos]=='j'){
                            negativo^=1;
                            aux = 'i';
                        }
                    }
                }
            }
        }
    }

    if(aux==car&&!negativo)
        return pos;

    return original.size();
}

bool cmp(int pos) {
    char aux=1;
    int negativo=0;
    while(pos+1<original.size()) {
        pos++;
        if(aux==1) {
            aux=original[pos];
        } else {
            if(aux==original[pos]) {
                aux=1;
                negativo^=1;
            } else {
                if(aux=='i') {
                    if(original[pos]=='j')
                        aux='k';
                    if(original[pos]=='k') {
                        negativo^=1;
                        aux='j';
                    }
                } else {
                    if(aux=='j'){
                        if(original[pos]=='i'){
                            negativo^=1;
                            aux='k';
                        }
                        if(original[pos]=='k')
                            aux='i';
                    }  else {
                        if(original[pos]=='i')
                            aux='j';
                        if(original[pos]=='j') {
                            negativo^=1;
                            aux='i';
                        }
                    }
                }
            }
        }
    }
    if(aux==1&&!negativo)
        return true;
    return false;
}

bool puede() {
    int pos;
    pos=busca(-1, 'i');
    pos=busca(pos, 'j');
    pos=busca(pos, 'k');
    if(pos>=original.size())
        return false;
    return cmp(pos);
}

int main(){
    optimizar_io(0);
    cin>>T;
    for(int cases=1;cases<=T;cases++) {
        cin>>N>>M;
        cin>>a;
        copia();
        cout<<"Case #"<<cases<<": ";
        if(puede())
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
    return 0;
}
