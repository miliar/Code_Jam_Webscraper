#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>
#include <deque>

using namespace std;



std::vector<char>  flip(std::vector<char> v){
    std::vector<char> w;
    for(int i=0;i<v.size();i++){
        char x=v[v.size()-1-i];
        if (x=='+'){
            x='-';
        }
        else{
            x='+';
        }
        w.push_back(x);

    }


    return w;
}






int main(){


int T;
cin>>T;

for (int i=0;i<T;i++){
    int op=0;
    string s;
    cin>>s;
    vector<char> v;
    for (int k =0;k<s.size();k++){
        v.push_back(s[k]);
    }
    while (!v.empty()){
        char base = v.back();
        char top = v.front();
        if (base=='+' ){
            v.pop_back();
            //cout<<"out"<<endl;
        }
        else{
            if(top=='-'){
                v=flip(v);
                op+=1;
            }
            else{
                std::deque<char> w;
                while(v.back()!='+'){
                    w.push_front(v.back());
                    v.pop_back();
                }
                v=flip(v);
                op+=1;
                while(!w.empty()){
                    v.push_back(w.front());
                    w.pop_front();
                }
            }
        }


    }
cout<<"Case #"<<i+1<<": "<<op<<endl;
}

return 0;

}

