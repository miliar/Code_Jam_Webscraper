#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large (1).in" , "r" , stdin);
    freopen("myout.txt" , "w" , stdout);
    int T;
    int eqto;
    string str1;
    string str2;
    string cha;
    scanf("%d" , &T);
    for(int i = 1; i <= T; i++){
        cin >> str1;
        str2.clear();
        cha.clear();
        cha.insert(0 , 1 , str1.at(0));
        str2.insert(0 , cha);
        eqto = 1;
        for(int c = 1; c < str1.length(); c ++){
            cha.clear();
            cha.insert(0 , 1 , str1.at(c));
            if(cha.at(0) > str2.at(0)){
                str2.insert(0 , cha);
                eqto = 1;
            }
            else if(cha.at(0) < str2.at(0)){
                str2.append(cha);
            }
            else{
                if(str2.length() == eqto){
                    str2.append(cha);
                    eqto ++;
                }
                else{
                    if(cha.at(0) > str2.at(eqto)){
                        str2.insert(0 , cha);
                        eqto ++;
                    }
                    else{
                        str2.append(cha);
                    }
                }
            }
        }
        cout << "Case #" << i << ": " << str2 << "\n";
    }
    return 0;
}
