#include<bits/stdc++.h>
#define mp make_pair
using namespace std;
int main()
{
    int t,n,l,i,j,k,f,x;
    bool neg;
    char ch;
    string s,e;
    ifstream IF;
    ofstream OF;
    IF.open("input.txt");
    OF.open("output.txt");
    IF>>t;
    pair<pair<char,char>,char> p[17];
    pair<char,char> v;
    p[0]=mp(mp('1','i'),'i');
    p[1]=mp(mp('i','1'),'i');
    p[2]=mp(mp('1','j'),'j');
    p[3]=mp(mp('j','1'),'j');
    p[4]=mp(mp('1','k'),'k');
    p[5]=mp(mp('k','1'),'k');
    p[6]=mp(mp('i','i'),'1');
    p[7]=mp(mp('j','j'),'1');
    p[8]=mp(mp('k','k'),'1');
    p[9]=mp(mp('k','i'),'j');
    p[10]=mp(mp('i','k'),'j');
    p[11]=mp(mp('j','i'),'k');
    p[12]=mp(mp('i','j'),'k');
    p[13]=mp(mp('j','k'),'i');
    p[14]=mp(mp('k','j'),'i');
    p[15]=mp(mp('1','1'),'1');
    for(j=1;j<=t;j++)
    {
        f=0;
        IF>>l>>x;
        IF>>s;
        e=s;
        for(i=1;i<x;i++)
        {
            s+=e;
        }
        ch='1';n=s.length();neg=0;
        //cout<<s<<endl;
        for(i=0;i<n;i++)
        {
            v=mp(ch,s[i]);
            for(k=0;k<16;k++)
            {
                if(p[k].first==v)
                {
                    ch=p[k].second;
                    if(v==mp('i','i')||v==mp('j','j')||v==mp('k','k')||v==mp('j','i')||v==mp('k','j')||v==mp('i','k'))
                        neg=(neg==0)?1:0;
                    break;
                }
            }
            if(ch=='i'&&neg==0)
                break;
        }
        if(i<n)
        {
            ch='1';neg=0;x=i;
            for(i=x+1;i<n;i++)
            {
                v=mp(ch,s[i]);
                for(k=0;k<16;k++)
                {
                    if(p[k].first==v)
                    {
                        ch=p[k].second;
                        if(v==mp('i','i')||v==mp('j','j')||v==mp('k','k')||v==mp('j','i')||v==mp('k','j')||v==mp('i','k'))
                            neg=(neg==0)?1:0;
                        break;
                    }
                }
                if(ch=='j'&&neg==0)
                    break;
            }
            if(i<n)
            {
                ch='1';neg=0;x=i;
                for(i=x+1;i<n;i++)
                {
                    v=mp(ch,s[i]);
                    for(k=0;k<16;k++)
                    {
                        if(p[k].first==v)
                        {
                            ch=p[k].second;
                            if(v==mp('i','i')||v==mp('j','j')||v==mp('k','k')||v==mp('j','i')||v==mp('k','j')||v==mp('i','k'))
                                neg=(neg==0)?1:0;
                            break;
                        }
                    }
                }
                if(ch=='k'&&neg==0)
                {
                    OF<<"Case #"<<j<<": YES"<<endl;
                    f=1;
                }
            }
        }
        //cout<<"Case #"<<p<<": "<<x<<endl;
        if(f==0)
            OF<<"Case #"<<j<<": NO"<<endl;
    }
    IF.close();
    OF.close();
    return 0;
}

