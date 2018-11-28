#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
double ff[1000+1];
double gg[1000+1];
double fw[1000+1];
double gw[1000+1];
bool flag_fw[1000+1];
bool flag_gw[1000+1];
int n;

void init()
{
    for(int i=0;i<=1000;++i)
    {
        flag_fw[i]=flag_gw[i]=0;
    }
}
int find_ub(double aa[1000+1],bool flag[1000+1],double f)
{
    for(int i=0;i<n;++i)
    {
        if(f<=aa[i]&&flag[i]==0)return i;
    }
    return -1;
}
int war()
{
    init();
    int ans=0;
    for(int i=0;i<n;++i)
    {
        double s=fw[i];
        int pos=find_ub(gw,flag_gw,s);
        if(pos>=0)
        {
            flag_gw[pos]=1;
        }
        else
        {
            int small=find_ub(gw,flag_gw,0);
            ++ans;
            flag_gw[small]=1;
        }
    }
    return ans;
}
int dwar()
{
    init();
    int ans=0;
    int del=-1;
    for(int i=n-1;i>=0;--i)
    {
        //loop for gg
        double s=gg[i];
        int w=find_ub(fw,flag_fw,s);
        if(w==-1)
        {
            //har nishchat
            flag_gw[i]=1;
            flag_fw[++del]=1;
        }
        else {
            flag_gw[i]=1;
            ++ans;
            flag_fw[w]=1;
        }
    }
    return ans;
}
int main()
{
    ofstream gout("output.txt");
    int t;
    cin>>t;
    int cs=0;
    while(t--)
    {
        ++cs;
        cin>>n;
        for(int i=0;i<n;++i)cin>>ff[i],fw[i]=ff[i];
        for(int i=0;i<n;++i)cin>>gg[i],gw[i]=gg[i];
        sort(ff,ff+n);
        sort(gg,gg+n);
        sort(fw,fw+n);
        sort(gw,gw+n);
        gout<<"Case #"<<cs<<": "<<dwar()<<' '<<war()<<endl;
    }

}
