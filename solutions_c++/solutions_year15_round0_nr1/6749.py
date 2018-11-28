#include<bits/stdc++.h>

using namespace std;

int main()
{

     freopen("out.txt","w",stdout);

    int test,syness,num,need,tot;

    vector<int>v;

    string s;

    cin>>test;

    for(int t=1; t<=test; t++)
    {
        cin>>syness>>s;

        v.clear();

        need = tot= 0;

        for(int i=0; s[i]; i++)
        {
            num = s[i]-'0';

            for(int j=0; j<num; j++)
                v.push_back(i);
        }

        sort(v.begin(),v.end());

        int siz = v.size();

        for(int i=0; i<siz; i++)
        {
            if(tot<v[i])
            {
                need+=v[i]-tot;
                tot+=v[i]-tot+1;
            }

            else
                tot++;
        }

        printf("Case #%d: %d\n",t,need);
    }

    return 0;

}
