#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

string toString(string s, int len)
{
    return string(len - s.size(), '0') + s;
}
bool isGood(int i, string s1)
{
    stringstream ss1;
    ss1<<i;
    string si = ss1.str();
    si = toString(si, s1.size());

    for(int i=0;i<si.size();i++)
    {
        if(si[i] != s1[i] && s1[i] != '?')
            return false;
    }
    return true;
    
}
vector<int> solve(string s1, string s2)
{
    int n = s1.size();
    int limit = pow(10, n);
    int cod = INT_MAX;
    int jam = INT_MAX; 
    int diff = INT_MAX;
    for(int i=0;i<limit;i++)
    {
        for(int j=0;j<limit;j++)
        {
            if(isGood(i, s1) && isGood(j, s2))
            {
                if(abs(i-j) < diff)
                {
                    diff = abs(i-j);
                    cod = i;
                    jam = j;
                }
                else if (abs(i-j)==diff && i < cod)
                {
                    cod = i;
                    jam = j;
                } else if (abs(i-j)==diff && i == cod && j < jam)
                {
                    jam = j;
                }
            }
        }
    }
    vector<int> v;
    v.push_back(cod);
    v.push_back(jam);
    return v;
}

int main()
{
    int T;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        string C, J;
        cin>>C>>J;
        vector<int> v = solve(C, J);
        int n = C.size();
        cout<<"Case #"<<t+1<<": ";
        cout<<setfill('0');
        cout<<setw(n)<<v[0]<<" "<<setw(n)<<v[1]<<endl;
    }
    return 0;
}
