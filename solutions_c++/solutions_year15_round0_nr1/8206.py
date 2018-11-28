#include <iostream>
#include <string>

int main(void){
    int n;

    std::cin >> n;

    for(int i=0; i < n; i++){
        int s;
        std::string person;
        std::cin >> s;
        std::cin >> person;

        int standing = 0, ans = 0;
        for(int j=0; j < person.length(); j++){
            if(standing >= j){
                standing += person[j] - '0';
            }else{
                while(1){
                    standing++; ans++;
                    if(standing >= j){
                        standing += person[j] - '0';
                        break;
                    }else{
                        continue;
                    }
                }
            }
        }
        std::cout << "Case #" << i + 1 << ": " << ans << std::endl;
    }
    return 0;
}
