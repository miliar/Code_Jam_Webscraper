#include <iostream>
#include <fstream>
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))

using namespace std;

bool alwaysPossible(int X, int R, int C) {
    if((R * C) % X != 0 || (X > R && X > C))
        return false;
    int min = MIN(R,C);
    int max = MAX(R,C);
    if(X <= 2)
        return true;
    else if(X == 3) {
        // Yay for case work!
        if(min == 1 && max == 3)
            return false;
        if(min == 2 && max == 3)
            return true;
        if(min == 3 && max == 3)
            return true;
        if(min == 3 && max == 4)
            return true;
        return false;
    }
    else if(X == 4) {
        if(min == 1 && max == 4)
            return false;
        if(min == 2 && max == 4)
            return false;
        if(min == 3 && max == 4)
            return true;
        if(min == 4 && max == 4)
            return true;
        return false;
    }
    else
        return false;
}

int main() {
    ifstream in("omino.in");
    ofstream out("omino.out");
    int T;
    in>>T;
    for(int k=0;k<T;k++) {
        int X,R,C;
        in>>X>>R>>C;
        out<<"Case #"<<(k+1)<<": ";
        out<<(alwaysPossible(X,R,C)?"GABRIEL":"RICHARD")<<"\n";
    }
    out.close();
    return 0;
}