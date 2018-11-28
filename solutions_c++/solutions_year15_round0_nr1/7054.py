#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream ifile;
    ifile.open("A-large.in");
    ofstream ofile;
    ofile.open("A-output.out");
    int t;
    ifile>>t;
    for (int i=1;i<=t;i++)
    {
        int n;
        string s;
        ifile>>n>>s;
        int res = 0;
        int sum = 0;
        int v[1100]={0};
        for (int j=0;j<=n;j++)
        {
            v[j] = int(s[j])-'0';
        }
        sum = v[0];
        for (int j=1;j<=n;j++)
        {
            if (sum<j)
                {
                    res += j - sum;
                    sum = j;
                }
            sum+=v[j];
        }
        ofile<<"Case #"<<i<<": "<<res<<endl;
    }
    return 0;
}
