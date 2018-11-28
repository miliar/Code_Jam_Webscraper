#include<bits/stdc++.h>
using namespace std;
int main()
{
    ofstream fout;
    ifstream fin;
    fout.open("ABCDE.txt");
    fin.open("ABC.txt");
    ios::sync_with_stdio(false);
    int test;
    fin>>test;
    for(int i=1;i<=test;i++)
    {
        int length;
        fin>>length;
        string s;
        fin>>s;
        int ans=0;
        int count=s[0]-'0';
        for(int i=1;i<=length;i++)
        {
            if(s[i]-'0' == 0)
                ;
            else
            {
                if(count>=i)
                {
                    count+= (s[i]-'0');
                }
                else
                {
                    ans+=i-count;
                    count+=s[i]-'0'+ans;
                }
            }
        }
        fout<<"Case #"<<i<<": "<<ans<<"\n";
    }
}
