#include <iostream>
#include <fstream>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

int main()
{
    int t;
    in>>t;
    for(int i=1; i<=t; ++i)
    {
        string ans;
        bool found=0;
        int n,r,p,s;
        in>>n>>r>>p>>s;
        string strarr[3]= {"P","R","S"};
        for(int l=0; l<3; ++l)
        {
            string str=strarr[l];
            for(int j=0; j<n; ++j)
            {
                string temp="";
                for(int k=0; k<str.size(); ++k)
                {
                    if(str[k]=='R')
                    {
                        if(n-j>1)temp+="SR";//RSPS
                        else temp+="RS";//PSRS
                    }
                    else if(str[k]=='P')
                    {
                        if(n-j>3)temp+="RP";//SRPR PSRSPRRS PS
                        else temp+="PR";//PRSR PRRSPSRS
                    }
                    else if(str[k]=='S')
                    {
                        if(n-j>2)temp+="SP";
                        else temp+="PS";
                    }
                }
                str=temp;
            }
            int rr=0,pp=0,ss=0;
            for(int j=0; j<str.size(); ++j)
            {
                if(str[j]=='R')
                {
                    ++rr;
                }
                else if(str[j]=='P')
                {
                    ++pp;
                }
                else if(str[j]=='S')
                {
                    ++ss;
                }
            }
            //cout<<rr<<" "<<pp<<" "<<ss<<endl;
            if(rr==r&&pp==p&&ss==s)
            {
                if(!found||(found&&ans>str))ans=str;
                found=1;
            }
        }
        if(found)
        {
            found=0;
            out<<"Case #"<<i<<": "<<ans<<endl;
        }
        else out<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}
