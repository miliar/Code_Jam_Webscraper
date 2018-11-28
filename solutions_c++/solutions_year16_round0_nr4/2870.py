#include <iostream>
using namespace std;

long long ipow(int k,int c)
{
    if(c==0)return 1;
    if(c==1)return k;
    long long s=ipow(k,c/2);
    if(c%2==0)return s*s;
    else return k*s*s;
}

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        tci++;
        cout<<"Case #"<<tci<<":";
        int k,c,s,i;
        cin>>k>>c>>s;
        long long le=ipow(k,c-1);
        long long l=1;
        for(i=0;i<s;i++){cout<<" "<<l;l+=le;}
        cout<<endl;
    }
    return 0;
}
