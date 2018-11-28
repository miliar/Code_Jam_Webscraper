#include <string>
#include <iostream>
#include <cstdio>
using namespace std;

string gera_nova(string s, int tam, int n){
    string nova;
    for(int i = n ; i >= 0 ; i--){
        if(s[i] == '+')
            nova.push_back('-');
        else
            nova.push_back('+');
    }
    for(int i = n+1 ; i < tam ; i++){
        nova.push_back(s[i]);
    }
    return nova;
}

int main(){
    int t, cases=1, ops;
    string s;

    scanf("%d", &t);

    while(t--){
        cin >> s;
        ops = 0;
        while(s.size() > 0){
            for(int i = s.size()-1 ; i >= 0 ; i--){
                if(s[i] == '+'){
                    s.pop_back();
                }
                else{
                    break;
                }
            }

            if(s.size() > 0){
                if(s[0] == '+'){
                    for(int i = 0 ; i < s.size() ; i++){
                        if(s[i] == '+' && s[i+1] != '+'){
                            if(s != gera_nova(s, s.size(), i))
                                ops++;
                            s = gera_nova(s, s.size(), i);
                            break;
                        }
                    }
                }
                else{
                    if(s != gera_nova(s, s.size(), s.size()-1))
                        ops++;
                    s = gera_nova(s, s.size(), s.size()-1);
                }
            }


        }
        printf("Case #%d: %d\n", cases++, ops);

    }
    return 0;
}
