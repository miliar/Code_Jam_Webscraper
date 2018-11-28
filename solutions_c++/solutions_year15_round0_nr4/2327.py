#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    int x,r,c,t;
    char ch;
    ifstream infile("D-small-attempt3.in");
    ofstream outfile("output.in");
    while(infile){
    infile>>t;
    infile.get(ch);

    for(int i=1;i<=t;i++)
    {
        infile>>x>>r>>c;
        if(c>r)
            swap(r,c);      //r is largest now
        if((x==1 && r==1 && c==1) || (x==2 && r==2 && c==1))
            outfile<<"Case #"<<i<<": "<<"GABRIEL"<<endl;

        else if((x>=r+c-1)  || (((c*r)%x)!=0)|| (x==4 && r==4 && c==2))
            outfile<<"Case #"<<i<<": "<<"RICHARD"<<endl;
        else
            outfile<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
    }
    outfile.close();}
    return 0;
}
