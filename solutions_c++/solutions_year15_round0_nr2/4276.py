#include <bits/stdc++.h>

using namespace std;

int main(int argc,char* argv[])
{
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    vector<vector<int>> d;
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        vector<int> app;
        int len;
        cin>>len;
        for(int j=0;j<len;j++)
        {
            int ap;
            cin>>ap;
            app.push_back(ap);
        }
        d.push_back(app);
    }

    for(int i=0;i<n;i++)
    {
        int minute_min=0;
        vector<int> poss;
        int m = (*max_element(d[i].begin(),d[i].end()));
        poss.push_back(m);
            for(int k=1;k<=m;k++)
            {
                minute_min=0;
                for(int j=0;j<d[i].size();j++)
                {
                    if(d[i][j]>k)
                    {
                        if(d[i][j]%k!=0)
                            minute_min++;
                        minute_min+=(d[i][j]/k)-1;
                    }
                }
                poss.push_back(minute_min+k);
            }

        minute_min=(*min_element(poss.begin(),poss.end()));
        cout<<"Case #"<<i+1<<": "<<minute_min<<endl;
    }
    return 0;
}
