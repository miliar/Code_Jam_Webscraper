#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("omino.in");
    ofstream fout("omino.out");
    int cases,x,r,c;
    fin >> cases;
    for(int i=1;i<=cases;i++)
    {
        fin >> x >> r >> c;
        cout << x << " " << r << " " << c << " ";
        int ld=c>r?r:c;
        if(x>=7||
           x>ld*2||
           ((r*c)%x)!=0||
           (ld==2&&x>=4)||
           (ld==3&&x>=6))cout << "Case #" << i << ": " << "RICHARD\n";
        else cout << "Case #" << i << ": " << "GABRIEL\n";
    }
    return 0;
}
