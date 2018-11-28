#include <iostream>
#include <cctype>
int main(){
    std::cin.sync_with_stdio(false);
    long long int t,cnt,Case = 1;
    long long int standing;
    std::cin>>t;
    long long int smax,diff;
    char c;
    long long int *lst = NULL;
    while(t--){
        cnt = standing = 0;
        std::cin>>smax;
        lst = new int long long[smax+1];
        std::cin.get();
        for(int i=0;i<=smax;i++){
            std::cin.get(c);
            lst[i] = c - 48;
        }

        if(lst[0] == 0){
            standing++;
            cnt++;
        }
        else{
            standing+=lst[0];
        }
        for(int i=1;i<=smax;i++){
            diff = 0;
            if(lst[i] != 0){
                if(standing >= i){
                    standing += lst[i];
                }
                else{
                    diff = i - standing;
                    cnt += diff;
                    standing += diff;
                    standing += lst[i];
                }
            }
        }
        std::cout<<"Case #"<<Case++<<": "<<cnt<<'\n';
        delete[] lst;
    }
    return 0;
}
