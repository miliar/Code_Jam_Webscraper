#include<iostream>
#include<fstream>
#include<string>
#define DEBUG 0
using namespace std;

#if DEBUG
ifstream fin("test.in");
ofstream fout("test.out");
#else
ifstream fin("A-large.in");
ofstream fout("A-large.out");
#endif

int main(){
    int numOfTests = 0;
    int h = 0;
    string line = "";
    fin >> numOfTests;
    for(int i=0; i<numOfTests; i++){
        int res = 0;
        int p = 0;
        fin >> h >> line;
        if(h != 0){
           p += (line[0] - '0'); 
           for(int j=1; j<=h; j++){
               if(j > p){
                   res += (j - p);
                   p += (j - p);
               }
               p += (line[j] - '0');
               if(p > h){
                   break;
               }
           }
        }
        cout << "Case #" << (i+1) << ": " << res << endl;
        fout << "Case #" << (i+1) << ": " << res << endl;
    }
    fin.close();
    return 0;
}
