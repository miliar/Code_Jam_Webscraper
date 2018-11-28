/* coder: Anh Tuan Nguyen */
#include <bits/stdc++.h>
using namespace std;

int a[300];
string s;
int cnt[10];

void giam(string x, int n)
{
    for(int i=0; i<x.length(); i++)
    {
        a[x[i]]-=n;
    }
}

int main()
{
#ifdef gsdt
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
#endif // gsdt

    int T;
    cin>>T;

    for(int q=1; q<=T; q++)
    {

        cin>>s;
        memset(a,0,sizeof(a));
        for(int i=0; i<s.length(); i++)
        {
            a[s[i]]++;
        }

        cnt[0]=a['Z'];
        giam("ZERO",cnt[0]);
        cnt[2]=a['W'];
        giam("TWO",cnt[2]);
        cnt[6]=a['X'];
        giam("SIX", cnt[6]);
        cnt[8]=a['G'];
        giam("EIGHT",cnt[8]);
        cnt[4]=a['U'];
        giam("FOUR",cnt[4]);
        cnt[3]=a['T'];
        giam("THREE",cnt[3]);
        cnt[1]=a['O'];
        giam("ONE",cnt[1]);
        cnt[7]=a['S'];
        giam("SEVEN",cnt[7]);
        cnt[5]=a['V'];
        giam("FIVE",cnt[5]);
        cnt[9]=a['I'];

        cout<<"Case #"<<q<<": ";
        for(int i=0; i<=9; i++)
        {
            for(int j=1; j<=cnt[i]; j++)
                cout<<i;

        }
        cout<<endl;
    }

    return 0;
}

