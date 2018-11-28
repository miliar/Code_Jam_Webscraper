#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define sl(n) scanf("%lld",&n)

int main()
{
    ifstream fin;
    ofstream fout("ans.txt");
    fin.open ("input.in");

    if(!fin.is_open())
    {
        fout<<"file error";
    }
    else
    {
        ll t;
        string s,s1;
        fin>>t;
        //fout<<t<<endl;
        for(int j=1;j<=t;j++)
        {
            //fout<<j<<endl;
            fin>>s;
            int l=s.length();
            int i=0;
            s1="";
            s1=s1+s[0];
            while(i<l)
            {
                if(s1[0]<=s[i+1])
                s1=s[i+1]+s1;
                else
                s1=s1+s[i+1];
                i++;
                //cout<<s1;
            }
            fout<<"Case #"<<j<<": ";
            for(i=0;i<l;i++)
            {
                fout<<s1[i];
            }
            fout<<endl;
        }
        fin.close();
        fout.close();
    }
}
