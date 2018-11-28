#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("D-large.in");
    ofstream fout("outputLarge.txt");
    int T, x, r, c, flag;
    fin >> T;
    for(int i = 0; i < T; i++){
        flag = 0;
        fin >> x;
        fin >> r;
        fin >> c;
        if( ((r*c)%x)||((x>r)&&(x>c))||(x>6)||( ((x<7)&&(x>2))&&((r<=((int)(x/2)))||(c<=((int)(x/2)))) )||((((r==5)&&(c==3))||((r==3)&&(c==5)))&&(x==5)) ) flag = 1;
        fout <<"Case #"<<i+1<<": "<<(flag?"RICHARD\n":"GABRIEL\n");
    }
    return 0;
}
