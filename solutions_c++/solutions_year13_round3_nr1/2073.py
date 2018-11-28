#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
char vowel[5]={'a','e','i','o','u'};
bool checksub(int n,bool sub[],int siz)
{
    int b=0;
    for(int a=0;a<siz;a++)
    {
        if (sub[a]==0) b++;
        else b=0;
        if (b>=n) return 1;
    }
    return 0;
}
int nvalue(int n,string s)//cons=0,vowel=1
{
    int sizes=s.size();
    bool si[sizes];
    for (int b=0;b<sizes;b++)
    {
        for (int c=0;c<5;c++)
        {
            if(s[b]==vowel[c])
            {
                si[b]=1;
                break;
            }
            else si[b]=0;
        }
        //cout<<si[b];
    }
    //cout<<endl;
    /*for (int d=0;d<sizes;d++)
    {
        if(si[d]==0)
        {

        }
    }*/
    int subl=n;
    int offset=0;
    int nv=0;

    while(subl<=sizes)
    {
        offset=0;
        while(offset<=sizes-subl)
        {
            bool sub[subl];
            for(int a=0;a<subl;a++)
            {
                sub[a]=si[offset+a];
                //cout<<sub[a];
            }
            //cout<<endl;
            if(checksub(n,sub,subl))
                nv++;
            //cout<<nv<<endl;
            offset++;
        }
        subl++;
    }
    return nv;
}
int main()
{
    int T;
    cin>>T;
    string s;
    int n;
    for (int t=1;t<=T;t++)
    {
        cin>>s;
        cin>>n;
        cout<<"Case #"<<t<<": "<<nvalue(n,s)<<endl;
    }
}
