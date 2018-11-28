#include <iostream>
#include <cstdio>

using namespace std;

#define cont continue
int  a[210][210],n,m;

void f_read()
{
    cin>>n>>m;
    int i;
    for (i=0;i<n;++i)
        for (int j=0;j<m;++j)
            cin>>a[i][j];
}

bool f()
{
    int i,j,o;
    for (i=0;i<n;++i)
        for (j=0;j<m;++j)
        {
            bool ei=0,ej=0;
            for (o=0;o<m;++o)
                if (a[i][o]>a[i][j]) ei=1;
            for (o=0;o<n;++o)
                if (a[o][j]>a[i][j]) ej=1;
            if (ej&ei) return true;
        }
    return false;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for (int i=0;i<t;++i)
    {
        f_read();
        printf("Case #%d: ",i+1);
        if (!f()) cout<<"YES";
        else cout<<"NO";
        cout<<endl;
    }
}

