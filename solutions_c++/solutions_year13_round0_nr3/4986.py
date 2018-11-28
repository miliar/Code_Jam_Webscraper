#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
using namespace std;

int main(){
int T, a, b;
int cases = 0;
int pal[] = {1,4,9,121,484};

ifstream fin("C-small-attempt0.in");
ofstream fout("1.out");

fin>>T;

int count = 0;
    while(T--){
        count = 0;
        fin>>a>>b;
        
        for(int i = a; i <= b; ++i){
            for(int j = 0; j < 5; ++j){
                if(i == pal[j]) ++count;
            }
        }
        fout<<"Case #"<<++cases<<": "<<count<<endl;
    }

    return 0;
}
