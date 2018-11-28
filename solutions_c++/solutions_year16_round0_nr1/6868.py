#include<bits/stdc++.h>
using namespace std;

bool cc;
long long frek[12],cnt;
void check(long long bil)
{
    long long i;
    while(bil>0)
    {
        if(frek[bil%10]==0)
        {
            cnt++;
        }
        frek[bil%10]++;
        bil=bil/10;
    }

}
int main()
{
    ifstream cin("concom.in");
    ofstream cout("concom.out");
    long long i,i2,cont=0,t;
    cin>>t;
    while(t--)
    {
        cout<<"Case #"<<++cont<<": ";
        cin>>i;
        if(i==0) {cout<<"INSOMNIA"<<endl; continue;}
        for(i2=0;i2<10;++i2)
        {
            frek[i2]=0;
        }
        cnt=0;
        i2=1;
        while(cnt!=10)
        {
            check(i*i2);
            //cout<<i*i2<<endl;
           // cout<<cnt<<endl;
            i2++;
        }
        cout<<(i*i2-i)<<endl;
    }


}
