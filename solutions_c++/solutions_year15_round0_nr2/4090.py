#include<bits/stdc++.h>
using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
int main()
{
    //READ("B-small-attempt2.in");
    //WRITE("B-small-attempt2.out");
    int t,d,maxx,minn,mins,n,newMax;cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>d;
        vector<int>v(d);
        vector<int>v2;
        mins=0;
        for(int j=0;j<d;j++)
            cin>>v[j];
        v2 = v;
        maxx = *max_element(v.begin(),v.end());
        minn = maxx;
        for(int j=0;;j++)
        {
            if(maxx == 1)
                break;
            n=find(v.begin(),v.end(),maxx)-v.begin();
            if(v[n]%2 == 0){
                v.push_back(maxx/2);
                v[n] = (maxx-(maxx/2));
            }
            else if(v[n]%3 == 0)
            {
                v.push_back(maxx/3);
                v[n] = (maxx-(maxx/3));
            }
            else
            {
                v.push_back(maxx/2);
                v[n] = (maxx-(maxx/2));
            }
            mins++;
            newMax = *max_element(v.begin(),v.end());
            minn = min(newMax+mins, minn);
            maxx = newMax;
        }

        mins = 0;
        maxx = *max_element(v2.begin(),v2.end());
        int minnn = maxx;
        for(int j=0;;j++)
        {
            if(maxx == 1)
                break;
            n=find(v2.begin(),v2.end(),maxx)-v2.begin();
            v2.push_back(maxx/2);
            v2[n] = (maxx-(maxx/2));
            mins++;
            newMax = *max_element(v2.begin(),v2.end());
            minnn = min(newMax+mins, minnn);
            maxx = newMax;
        }

        cout<<"Case #"<<i+1<<": "<<min(minn,minnn)<<endl;
    }
}
