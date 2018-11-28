#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector <int> pancakesPack;

int stackPancakes(string pancakes){

    int N=0;
    bool can=false;
    bool pass=false;

    for(unsigned int i=0;i<pancakes.length();i++){
        if(pancakes[i]=='+'){
            pancakesPack.push_back(1);
        }else{
            pancakesPack.push_back(0);
            can=true;
        }
    }

    if(can){

        while(!pass){

            int aux=0, aux2=0;
            bool block=false;

            for(unsigned int i=0;i<pancakesPack.size();i++){
                if(pancakesPack[0]==pancakesPack[i]&&!block){
                    aux++;
                }else{
                    block=true;
                }
            }
            for(int i=0;i<aux;i++){
                if(pancakesPack[i]==1){
                    pancakesPack[i]=0;
                }else{
                    pancakesPack[i]=1;
                }
            }
            for(unsigned int i=0;i<pancakesPack.size();i++){
                if(pancakesPack[i]==1){
                    aux2++;
                }
            }

            N++;

            if(static_cast<unsigned int>(aux2) == pancakesPack.size()){
                pass=true;
            }
        }

        return N;

    }else{
        return 0;
    }
}

int main(){

    int T;
    string pancakes;

    cin >> T;

    for(int i=0;i<T;i++){
        cin >> pancakes;
        pancakesPack.clear();
        cout << "Case #" << i+1 << ": " << stackPancakes(pancakes) << endl;
    }

    return 0;
}
