#include <fstream>
#include <iostream>

using namespace std;

string findWinner(int x, int r, int c) {
    if (x == 1) return "GABRIEL";
    if (x == 2) {
        if (r%2 == 0 || c%2 == 0) return "GABRIEL";
        else return "RICHARD";
    }
    if (x == 3) {
        if ((r * c)%3 != 0 || (r ==3 && c==1) || (c==3 && r==1)) return "RICHARD";
        else return "GABRIEL";

    }
    if (x == 4) {
        if ((r!=4 && c!=4) || r==1 || c==1 || r==2 || c==2) return "RICHARD";
        else return "GABRIEL";

    }
}

int main()
{
    ifstream f("C:/Users/Rebecca/Downloads/D-small-attempt0.in");
    ofstream out;
    out.open("C:/Users/Rebecca/Downloads/result5.txt");

    int tests;
    f >> tests;
    for (int i = 0; i < tests; i++) {
        int x, r, c;
        f >> x >> r >> c;
        string winner = findWinner(x,r,c);
        out << "Case #" << i+1 << ": " << winner << endl;
    }
    out.close();
    return 0;
}

