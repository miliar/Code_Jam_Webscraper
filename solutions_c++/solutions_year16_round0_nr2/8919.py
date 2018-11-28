#include <bits/stdc++.h>

using namespace std;
//ifstream fin("A-small-attempt1.in");
//ofstream fout("out2.txt");

int main()
{
    int test;
    cin>>test;

    for(int k=1;k<=test;++k)
    {
        string s;
        cin>>s;
        int l = s.length();
        int n = 0;
        for(int i=1;i<l;++i)
            if(i<l && s[i]!=s[i-1])
                n++;
        if(s[l-1]=='-')
            n++;
        cout<<"Case #"<<k<<": "<<n<<endl;
    }
}
