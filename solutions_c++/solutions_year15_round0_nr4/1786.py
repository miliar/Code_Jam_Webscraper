#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream inin;
    inin.open("C:\\WYX\\Program\\D-small-attempt0.in",ios::in);
    ofstream outout;
    outout.open("C:\\WYX\\Program\\ominous_out.out",ios::out);
    int num;
    inin >> num;
    for (int numm=0;numm<num;numm++)
    {
        int x,r,c;
        inin >> x >> r >> c;
      //  int flag = 0;
        if (x==1) outout << "Case #" << numm+1 << ": GABRIEL" << endl;
        else if (r*c%x!=0) outout << "Case #" << numm+1 << ": RICHARD" << endl;
        else if (r<x && c<x) outout << "Case #" << numm+1 << ": RICHARD" << endl;
        else if (x==2) outout << "Case #" << numm+1 << ": GABRIEL" << endl;
        else if (r<((x+1)/2) || c<((x+1)/2)) outout << "Case #" << numm+1 << ": RICHARD" << endl;
        else if (x==4 && r==2 && c==4) outout << "Case #" << numm+1 << ": RICHARD" << endl;
        else if (x==4 && r==4 && c==2) outout << "Case #" << numm+1 << ": RICHARD" << endl;
        else outout << "Case #" << numm+1 << ": GABRIEL" << endl;
    }
}
