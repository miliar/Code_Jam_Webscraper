#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    int t;
    ifstream fin("aBigIn.in");
    ofstream fout("aBigOut.txt");
    //cin>>t;
    fin>>t;
    for (int j=0; j<t; j++)
    {
        int len;
        long long ans = 0, cur = 0;
        string word;
        //cin>>len>>word;
        fin>>len>>word;
        for (int i=1; i<=(len+1); i++)
        {
            if (cur < i-1)
            {
                    ans += (i-1-cur);
                    cur = i-1;
            }
            cur += (word[i-1] - '0');
        }
        //cout<<"Case #"<<j+1<<": "<<ans;
        fout<<"Case #"<<j+1<<": "<<ans;
        if (j!=(t-1))
           //cout<<endl;
           fout<<endl;
    }
    //system("pause");
    return 0;
}
