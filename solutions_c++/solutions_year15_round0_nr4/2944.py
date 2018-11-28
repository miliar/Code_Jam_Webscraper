#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int t;
    ifstream file1("f1.txt");
    ofstream file2("f2.txt");
    file1>>t;
    for(int y=1;y<=t;y++)
    {
        int x,r,c;
        file1>>x>>r>>c;
        int n=r*c;
        if(x==4)
        {

            if(r*c==8 || r*c==4 || n%x!=0)
                file2<<"Case #"<<y<<": "<<"RICHARD"<<"\n";
            else
                file2<<"Case #"<<y<<": "<<"GABRIEL"<<"\n";

        }
        else if(x==3)
        {

            if(r*c==3 || n%x!=0)
                file2<<"Case #"<<y<<": "<<"RICHARD"<<"\n";
            else
                file2<<"Case #"<<y<<": "<<"GABRIEL"<<"\n";

        }
        else
        {


        if(n%x!=0 )
            file2<<"Case #"<<y<<": "<<"RICHARD"<<"\n";
        else
            file2<<"Case #"<<y<<": "<<"GABRIEL"<<"\n";
        }
    }
    return 0;
}
