#include <cstdio>
#include <cstdlib>>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char ** argv){

    int T;
    cin>>T;

    for(int i = 0 ; i < T ; ++i){
        int level;
        cin>>level;

        string audience;
        cin>>audience;

        int clapped  = audience[0] - '0';
        int needed = 0;

        for(int j = 1; j <= level; ++j){
            if(clapped < j){
               needed += j - clapped;
               clapped += j - clapped;
            }
            clapped += audience[j] - '0';
        }

        cout<<"Case #"<<i+1<<": "<<needed<<endl;
    }

    return 0;
}
