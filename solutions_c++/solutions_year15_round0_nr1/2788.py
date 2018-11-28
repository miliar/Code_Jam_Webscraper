#include <iostream>
#include <queue>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <set>
#include <sstream>
using namespace std;





int main()
{
    ios_base::sync_with_stdio(false);
    ifstream in("input.txt");
    ofstream out("output.txt");
    #define cin in
    #define cout out
    int nb_cas;
    cin>>nb_cas;
    for(int cas=1;cas<=nb_cas;cas++)
    {
        cout<<"Case #"<<cas<<": ";
        int Smax;
        cin>>Smax;
        string s;
        cin>>s;
        int act = 0;
        int res = 0;
        for(int c=0;c<s.size();c++)
        {
            if(s[c]=='0') continue;
            if(act >= c)
            {
                act+=s[c]-'0';
            }
            else
            {
                res+=c-act;
                act=c;
                act+=s[c]-'0';
            }
        }
        cout<<res<<endl;
    }
}
