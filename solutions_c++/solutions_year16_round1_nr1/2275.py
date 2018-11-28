#include<bits/stdc++.h>
using namespace std;
#define MAX 1000001
typedef long long ll;

int main()
{
    ifstream IF;
    IF.open("input.txt");
    ofstream OF;
    OF.open("output.txt");
    int t; IF >> t;
    for(int tt=1;tt<=t;tt++)
    {
        string s,p=""; IF >> s;
        char ss[3000];int i,j; i=1000;j=1001;
        ss[i]=s[0];i--;
        for(int ii=1;ii<s.size();ii++)
        {
            if(s[ii]>=ss[i+1])
            {
                ss[i] = s[ii];
                i--;
            }
            else
            {
                ss[j] = s[ii];
                j++;
            }
        }
        string ans="";
        for(int pp=i+1;pp<j;pp++)
            ans += ss[pp];
        OF << "Case #" << tt << ": " << ans << endl;
    }
    OF.close(); IF.close();
}


