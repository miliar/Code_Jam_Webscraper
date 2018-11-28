#include <iostream>
#include <deque>
#include <string>

using namespace std;

bool verif(deque<char> po){
    bool s ;
    unsigned int l(0) ;
    for(unsigned int i(0); i < po.size();i++){
        if(po[i]=='+')
            l++;
    }
    if(l==po.size())
        s = true ;
    else s = false ;
    return s ;
}

int main()
{
    long int T ;
    cin >> T ;
    long int o(1);
    while(o <= T){
    string pp ;
    deque<char> po ;
    cin >> pp ;
   long int t(0) ;
    while(pp[t]!='\0'){
        po.push_back(pp[t]);
        t++ ;
    }
    long int y(0);
    //verification

    if(verif(po)==false){
    while(verif(po)==false){
        if(po.front()=='-'){
            while(po.front()=='-'){
                po.pop_front();
                po.push_back('+');
            }
            y++ ;
        }
        else {
            while(po.front()=='+'){
                po.pop_front();
                po.push_back('+');
            }
            y++ ;
        }
    }
    cout << "Case #" << o  << ": " << y << endl ;
    }
    else{
        cout << "Case #" << o << ": 0" << endl ;
    }
    o++ ;
    }
    return 0;
}
