#include <iostream>
#include <fstream>
#include <ostream>

using namespace std;

int run(int i, string t)
{
    int needed=0;
    int sum=0;
    int l=t.length();
    for(int j=0;j<l;++j)
    {

        sum+=t[j] - '0';
    //    std::cout << sum << " - ";
        if ((sum+needed)<j+1) needed=needed+1;
    }
    return needed;
}

int main()
{
    fstream f("input.txt");
    ofstream o("output.txt");
    int s;
    int m;
    f >> s;
    for(int i=0;i<s;++i)
    {
        string t;
        f>>m;
        f>>t;
     //   cout << m << "  " << t << endl;
        o << "Case #" << (i+1) << ": " << run(i,t) << endl;
    }
    o.close();
    f.close();
    return 0;
}
