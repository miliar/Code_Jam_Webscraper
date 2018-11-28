#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    freopen("cj3.in", "r", stdin);
    freopen("cj3.txt", "w", stdout);
    int t=1, n, a[30], i, m, m1, m2, p1, p2, s, l;
    cin>>t;
    for(l=1; l<=t; l++)
    {
        cout<<"Case #"<<l<<": ";
        cin>>n;
        s=0;
        for(i=0; i<n; i++)
        {
            cin>>a[i];
            s+=a[i];
        }
        while(s>0)
        {
            if(s==3)
            {
                m1=m2=m=-1;
                for(i=0; i<n; i++)
                {
                    if(a[i] && m==-1)
                        m=i;
                    else if(a[i] && m1==-1)
                        m1=i;
                    else if(a[i])
                        m2=i;
                }
                cout<<(char)(m+'A')<<" "<<(char)(m1+'A')<<(char)(m2+'A');
                break;
            }
            m1=m2=-1;
            p1=p2=-1;
            for(i=0; i<n; i++)
            {
                if(m1<a[i])
                {
                    m1=a[i];
                    p1=i;
                }

            }
            for(i=0; i<n; i++)
            {
                if(m2<a[i] && i!=p1)
                {
                    m2=a[i];
                    p2=i;
                }
            }
            s-=2;
            a[p1]--;
            a[p2]--;
            cout<<(char)(p1+'A')<<(char)(p2+'A')<<" ";
        }
        cout<<endl;

    }
    return 0;
}
