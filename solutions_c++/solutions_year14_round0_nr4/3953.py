#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int FIND_UPPER_BOUND(int n,double aBa[1000+1],bool flaAg[1000+1],double fA)
{
    for(int i=0;i<n;++i)
    {
        if(fA<=aBa[i]&&flaAg[i]==0)return i;
    }
    return -1;
}
int WAR(int n,double naomi[1000+1],double ken[1000+1],bool naomi_flag[1000+1],bool ken_flag[1000+1])
{
    for(int i=0;i<=1000;++i)
    {
        naomi_flag[i]=ken_flag[i]=0;
    }
    int ans=0;
    for(int i=0;i<n;++i)
    {
        double s=naomi[i];
        int pos=FIND_UPPER_BOUND(n,ken,ken_flag,s);
        if(pos>=0)
        {
            ken_flag[pos]=1;
        }
        else
        {
            int small=FIND_UPPER_BOUND(n,ken,ken_flag,0);
            ++ans;
            ken_flag[small]=1;
        }
    }
    return ans;
}
int DECEITFUL_WAR(int n,double naomi[1000+1],double ken[1000+1],bool naomi_flag[1000+1],bool ken_flag[1000+1])
{
    for(int i=0;i<=1000;++i)
    {
        naomi_flag[i]=ken_flag[i]=0;
    }
    int ans=0;
    int del=-1;
    for(int i=n-1;i>=0;--i)
    {
        //loop for ken
        double s=ken[i];
        int w=FIND_UPPER_BOUND(n,naomi,naomi_flag,s);
        if(w==-1)
        {
            //har nishchat
            ken_flag[i]=1;
            naomi_flag[++del]=1;
        }
        else {
            ken_flag[i]=1;
            ++ans;
            naomi_flag[w]=1;
        }
    }
    return ans;
}
int main()
{
    double naomi[1000+1];
double ken[1000+1];
bool naomi_flag[1000+1];
bool ken_flag[1000+1];

    ofstream gout("output.txt");
    ifstream gput("inp.txt");
    int test;
    int n;
    gput>>test;
    int cse=0;
    while(test--)
    {
        ++cse;
        gput>>n;
        for(int i=0;i<n;++i)gput>>naomi[i];
        for(int i=0;i<n;++i)gput>>ken[i];
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        gout<<"Case #"<<cse<<": "<<DECEITFUL_WAR(n,naomi,ken,naomi_flag,ken_flag)<<' '<<WAR(n,naomi,ken,naomi_flag,ken_flag)<<endl;
    }
    cout<<"all test case completed succesfully";
}
