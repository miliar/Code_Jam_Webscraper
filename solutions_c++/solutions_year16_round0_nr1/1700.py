#include <iostream>
#include <fstream>
using namespace std;

typedef long long ll;

bool used[10];

bool check(){
    for(int i = 0; i < 10; i++){
        if(!used[i]){
            return false;
        }
    }
    return true;
}

void update(ll x){
    int digit;
    while(x > 0){
        digit = x%10;
        if(!used[digit]){
            used[digit] = true;
        }
        x /= 10;
    }
}

void reset(){
    for(int i = 0; i < 10; i++){
        used[i] = false;
    }
}

int main(){
    ifstream fin("count.in");
    ofstream fout("count.out");
    int T;
    ll N, cur;
    bool finish = false;
    fin>>T;
    for(int t = 1; t <= T; t++){
        fin>>N;
        cur = 1;
        finish = false;
        reset();
        while(cur <= 1001 && !finish){
            update(cur*N);
            if(check()){
                finish = true;
            }
            cur++;
        }
        fout<<"Case #"<<t<<": ";
        if(!finish){
            fout<<"INSOMNIA\n";
        }else{
            fout<<(cur-1)*N<<"\n";
        }
    }
}

