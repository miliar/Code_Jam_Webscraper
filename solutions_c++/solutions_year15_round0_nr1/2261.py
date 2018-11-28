#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("out.txt");
    int tc,msl,sum=0,cnt=0;
    string s;
    in>>tc;
    for(int cas=1;cas<=tc;cas++)
    {
        cnt=0;
        sum=0;
        in>>msl;
        in>>s;
        sum = sum + s[0]-48;
        for(int i=1;i<s.size();i++)
        {
            if(i<=sum)
                sum=sum+s[i]-48;
            else
            {
                cnt=cnt+(i-sum);
                sum=sum+s[i]-48+(i-sum);
            }
        }
        out<<"Case #"<<cas<<": "<<cnt<<endl;
    }
    return 0;
}
