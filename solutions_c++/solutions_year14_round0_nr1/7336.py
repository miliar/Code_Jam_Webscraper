#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("a.in","r",stdin);
    freopen("w.out","w",stdout);
    int t,a,n=1;
    int c=0;
    int num=-1;
    cin>>t;
    while(t--)
    {
        cin>>a;
        int *v = new int [4];
        set<int>x;
        for(int i=1; i<=4; i++)
        {
            for(int j=0; j<4; cin>>v[j++]);
            if(a==i)
                for(int j=0; j<4; x.insert(v[j++]));
        }
        cin>>a;
        for(int i=1; i<=4; i++)
        {
            for(int j=0; j<4; cin>>v[j++]);
            if(a==i)
            {
                c=0;
                for(int j=0; j<4; j++)
                {
                    if(x.find(v[j])!=x.end())
                        c++,num=v[j];
                }
            }
        }
        if(c==1)
            printf("Case #%d: %d\n",n++,num);
        else if(c>1)
            printf("Case #%d: Bad magician!\n",n++);
        else
            printf("Case #%d: Volunteer cheated!\n",n++);

    }
    return 0;
}
