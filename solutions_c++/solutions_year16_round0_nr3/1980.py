#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair < int , int > Point;

string DecToBin(LL x, int N)
{
    string ret("");
    while(x)
    {
        ret+=(char)'0'+(x%2);
        x/=2;
    }
    while((int)ret.size()<N)ret+='0';
    reverse(ret.begin(),ret.end());
    return ret;
}

int main()
{
//    freopen("numbers_large.txt","w+",stdout);
    cout<<"Case #1:\n";
    LL N = 32 , i , j ,k,l;
    vector < LL > Out;

    for(i=1;i<=28;++i)
        for(j=i+2;j<=28;++j)
            for(k=j+2;k<=28;++k)
                for(l=k+2;l<=28;++l)
                {
                    if(Out.size()!=500)
                        Out.push_back(((1LL<<31) |(1) | (1LL<<i) | (1LL<<(i+1)) | (1LL<<(j)) | (1LL<<(j+1)) |(1LL<<(k)) | (1LL<<(k+1)) | (1LL<<l) | (1LL<<(l+1))));
                    else
                        goto last;
                }
    last:
    sort(Out.begin(),Out.end());
    Out.erase(unique(Out.begin(),Out.end()),Out.end());
    assert(Out.size()==500);
    for(i=0;i<(int)Out.size();++i)
    {
        cout<<DecToBin(Out[i],N)<<" ";
        if(__builtin_popcount(Out[i])!=10)
            assert(0);
        assert(DecToBin(Out[i],N).size()==32);
        assert(DecToBin(Out[i],N)[0]=='1' && DecToBin(Out[i],N)[31]=='1');
        for(j=2;j<=10;++j)
            cout<<j+1<<" ";
        cout<<'\n';
    }
    cout<<endl;

    return 0;
}
