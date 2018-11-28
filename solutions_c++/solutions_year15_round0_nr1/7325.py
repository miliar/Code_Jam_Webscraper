#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream ifile;
    ifile.open("A-large.in");
    ofstream ofile;
    ofile.open("A-output.out");
    int t=0;
    ifile>>t;
    for (int i = 1;i <= t;i ++)
    {
        int n;
        string s;
        ifile>>n >> s;
        int res = 0;
        int sumcount = 0;
        int v[1100]={0};
        for (int j=0;j<=n;j++)
        {
            v[j] = int(s[j])-'0';
        }
        sumcount = v[0];
        for (int j=1;j<=n;j++)
        {
            if (sumcount<j)
			{
				res += j - sumcount;
				sumcount = j;
			}
            sumcout+=v[j];
        }
        ofile<<"Case #"<<i<<": "<<res<<endl;
    }
    return 0;
}
