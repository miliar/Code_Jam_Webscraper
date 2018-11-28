#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream f1("A-small-attempt0");
    ofstream f2("large.out");

    int T;
    int length;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        string s,y;
        cin>>s;
        length=s.size();
        y=s[0];
        for(int j=1;j<length;j++)
        {
            if(s[j]>=y[0])
            {
                y=s[j]+y;
            }
            else
            {
                y=y+s[j];
            }
        }
        f2<<"Case #"<<i+1<<": "<<y<<endl;

    }
    return 0;
}
