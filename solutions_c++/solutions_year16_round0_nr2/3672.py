#include <iostream>
#include <list>
#include <algorithm>
using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int n;
    cin >> n;
    for (int i=1;i<=n;i++)
    {
        string s;
        cin >> s;
        vector<char> c;
        int kol=0;
        for (int j=0;j<s.length();j++){c.push_back(s[j]);}
        vector<char>::iterator it=unique(c.begin(),c.end());
        c.resize(it-c.begin());
        if (c.size()>0&&s[s.length()-1]=='+'){c.pop_back();}
        kol+=c.size();
        cout << "Case #" << i << ": " << kol << endl;
    }
    return 0;
}
