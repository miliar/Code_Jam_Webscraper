#include <bits/stdc++.h>
using namespace std;


int main()
{    ofstream fout;
        fout.open("ans.txt");
    long long int t,p ;
    cin>>t;
    for(p=1;p<=t;p++)
    {

        long long int n ,i;
        cin>>n;
        string s ;
        cin>>s;
        long long int sum =0;
        long long int cou=0;
        for(i=0;i<s.length();i++)
        {
            int yu =  int(s[i])-'0';
            if(sum<i)
                {cou++;sum++;}
            sum+=yu;

        }

        fout<<"Case #"<<p<<": "<<cou<<"\n";

    }

}
