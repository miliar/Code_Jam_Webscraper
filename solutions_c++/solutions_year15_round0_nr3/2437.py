#include<bits/stdc++.h>
using namespace std;
int hash[10002]={0};

int a[5][5]={
    {0,0,0,0,0},
{0,1,2,3,4},
{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}
};


int fun(string s)
{
    int ini=1;
    for(int i=0;i<s.size()-2;i++)
    {
        if(ini<0)
            {ini=a[-1*ini][s[i]-'g'];ini*=-1;}
        else
            ini=a[ini][s[i]-'g'];
        //cout<<a[ini][s[i]-'g']<<" ";
        if(ini==2)
        {
            int ini1=1;
            for(int j=i+1;j<s.size()-1;j++)
            {
                if(ini1<0)
                    {ini1=a[-1*ini1][s[j]-'g'];ini1*=-1;}
                else
                    ini1=a[ini1][s[j]-'g'];

                if(ini1==3&&hash[j]==0)
                {
                    int ini2=1;
                    for(int z=j+1;z<s.size();z++)
                    {
                        if(ini2<0)
                            {ini2=a[-1*ini2][s[z]-'g'];ini2*=-1;}
                        else
                            ini2=a[ini2][s[z]-'g'];

                    }
                    if(ini2==4)
                    {
                        return 1;
                    }
                    else    hash[j]=1;
                }
            }
        }
    }
    return 0;
}




int main()
{
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        memset(hash , 0 , sizeof hash);
        int x,l;
        cin>>x>>l;
        string as;
        cin>>as;
        string s="";
        for(int i=0;i<l;i++)
            s+=as;
        if(fun(s))  cout<<"Case #"<<j<<": YES"<<endl;
        else    cout<<"Case #"<<j<<": NO"<<endl;
    }
    return 0;
}
