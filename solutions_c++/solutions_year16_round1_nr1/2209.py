#include<cstring>
#include<iostream>
#include<cstdio>
using namespace std;


int main()
{
     freopen("ainput1_12.in","r",stdin);
    freopen("cjout1.txt","w",stdout);

    int t;
    cin>>t;
    for(int tt=1;tt<=t;++tt)
    {
        string in,result;
        char currmax;
        cin>>in;
        currmax=in[0];
        result+=in[0];
        for(int i=1;i<in.length();++i)
        {
            //cout<<in[i]<<" "<<currmax<<endl;
            if(in[i]>=currmax)
            {
                result=in[i]+result;
                currmax=in[i];
            }
            else
                result+=in[i];
        }
        cout<<"Case #"<<tt<<": "<<result<<endl;
    }
}
