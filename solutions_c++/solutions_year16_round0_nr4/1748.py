#include<bits/stdc++.h>
#define LONG_LONG_MAX	9223372036854775807LL
using namespace std;
int all_plus(int n, vector<int>p)
{
        int ptr = n-1;

        int ans=0;
        while(ptr>=0)
        {
            if(p[ptr]==0)
            {
                ans++;
                if(p[0]==1)
                {
                    int i = 0;
                    while(i<n && p[i]==1)p[i++]=0;
                    continue;
                }

                int st = 0, en = ptr;
                while(st<en)
                {
                    int tmp = p[st];p[st] = p[en];p[en]=tmp;
                    st++;en--;
                }
                for(int i=0;i<=ptr;i++)p[i] = 1-p[i];

            }
            ptr--;
        }
        return ans;
}
int all_minus(int n, vector<int>p)
{
        int ptr = n-1;
        int ans=0;
        while(ptr>=0)
        {
            if(p[ptr]==1)
            {
                ans++;
                if(p[0]==0)
                {
                    int i = 0;
                    while(i<n && p[i]==0)p[i++]=1;
                    continue;
                }

                int st = 0, en = ptr;
                while(st<en)
                {
                    int tmp = p[st];p[st] = p[en];p[en]=tmp;
                    st++;en--;
                }
                for(int i=0;i<=ptr;i++)p[i] = 1-p[i];

            }
            ptr--;
        }
        return ans+1;
}
int main()
{


      freopen("GoogleCodeJam2016.txt", "r", stdin);
      freopen("GoogleCodeJam2016_output.txt", "w", stdout);

    int t;
    cin>>t;

    for(int tc=1;tc<=t;tc++)
    {

        int k, c, s;
        cin>>k>>c>>s;
        cout<<"Case #"<<tc<<": ";
        for(int i=1;i<k;i++)
        {
            cout<<i<<" ";
        }
        cout<<k<<endl;

    }


}
