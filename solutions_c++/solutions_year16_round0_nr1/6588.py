#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int t;
    int y;
    cin>>t;
    for (int i=1;i<=t;i++)
        {
            int cnt = 1;
            set<int> x;
            cin>>y;
            if (y==0)
                cout<<"Case #"<<i<<": INSOMNIA\n";
            else
            {
                while ((x.size()!=10 && cnt<100 ))
                {
                    int z=y*cnt++;
                    while(z!=0)
                    {
                        x.insert(z%10);
                        z/=10;
                        if (x.size()==10)
                        break;
                    }
                }
                cout<<"Case #"<<i<<": "<<y*(cnt-1)<<"\n";
            }
        }
    return 0;
}
