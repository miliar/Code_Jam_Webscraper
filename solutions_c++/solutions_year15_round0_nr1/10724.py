#include <bits/stdtr1c++.h>
using namespace std;

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n;
    string s;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        cin >> n >> s;
        int c=0,p=0;
        for(int j=0;j<s.size();j++)
        {
            if(p<j &&s[j]>'0')
                c+=(j-p),p+=c;
               // cout << c << "  " << p << "\n";
            p+=s[j]-'0';
        }
        cout << "Case #" << i+1 << ": " << c << "\n" ;
    }
    return 0;
}
