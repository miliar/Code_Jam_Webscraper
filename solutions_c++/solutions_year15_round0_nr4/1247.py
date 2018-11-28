#include <iostream>
#include <fstream>
using namespace std;
bool isPossible(int x, int r, int c){
    int totalSquares=r*c;
    if(totalSquares%x != 0){
        return false;
    }
    if(c>r){
        int t=c;
        c = r;
        r = t;
    }
    if(x>r){
        return false;
    }
    if(x>=2*c+1){
        return false;
    }
    if(x==1){
        return true;
    }
    if(x<=c+1){
        return true;
    }
    //if tricky appears in the text file I go through and correct them if I see a way to fix it, hard to hardcode the answer
    cout << "TRICKY " << x << " : " << r << " : " << c << endl;
    return true;
}
int main(int argc, char* argv[])
{
    fstream input;
    input.open(argv[1]);
    int total;
    input >> total;
    for(int i=0; i<total; i++){
        int x;
        int r;
        int c;
        input >> x;
        input >> r;
        input >> c;
        cout << "Case #" << i+1<< ": " << ((isPossible(x,c,r))? "GABRIEL" : "RICHARD") << endl;
    }
    return 0;
}
