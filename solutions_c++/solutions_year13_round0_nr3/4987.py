#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
using namespace std;

int main(){

int t, a, b;
int Casesno = 0;
int array[] = {1, 4, 9, 121, 484};
ifstream fi("C-small-attempt0.in");
ofstream fo("x.out");
fi>>t;
int c = 0;

    while(t--){
        c = 0;
        fi>>a>>b;        
        for(int i = a; i <= b; ++i){
            for(int j = 0; j < 5; ++j){
                if(i == array[j]) ++c;
            }
        }
        fo<<"Case #"<<++Casesno<<": "<<c<<endl;
    }

    return 0;
}
