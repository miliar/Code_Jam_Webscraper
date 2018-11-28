# include <iostream>
# include <conio.h>
# include <fstream>
using namespace std;
int solve();
ifstream fr("input.txt");
ofstream fw("output.txt");
int main()
{   int rep;
    fr>>rep;
    for (int i=0;i<rep;i++)
        fw<<"Case #"<<i+1<<": "<<solve()<<endl;
}
int solve()
{   //cout <<"test case";
    //getch();
    int r,t;
    fr>>r;
    fr>>t;
    int x=2,count=0;
    do
    {   //c_area+=(pie*(x*r)*(x*r))-(pie*(r-1)*(r-1));
        t-=((r+1)*(r+1))-(r*r);
        count++;
        r+=2;
        //cout <<c_area<<" "<<area<<endl;
        //getch();
    }
    while(t>=0);
    return count-1;
}


