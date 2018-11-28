#include <iostream>

std::string S,LW;
int T;


void solve(){
    char c,largest;
    std::cin >> S;
    int length = S.size();
    largest = S[0];
    std::string LW(1,largest);
    for(int i=1;i<length;i++){
        c = S[i];
        if(c>=largest){//左に追加
            LW.insert(LW.begin(),c);
            largest = c;
        }else{//右に追加
            LW.push_back(c);            
        }
    }
    std::cout << LW << std::endl;
}

int main(){
    std::cin >> T;
    for(int i=1;i<=T;i++){
        std::cout << "Case #" << i << ": ";
        solve();
    }

}