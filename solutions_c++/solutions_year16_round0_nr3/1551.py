#include<bits/stdc++.h>
#define LONG_LONG_MAX	9223372036854775807LL
using namespace std;
vector<int>primes;
int p[1000006];
vector<int> f(long long str)
{
    vector<int>ans;

    for(int b=2;b<=10;b++)
    {
        int flag = 0;
        for(int i=0;i<primes.size() && primes[i]<str;i++)
        {
            long long val=0, tmp = 1;

            for(int j=0;(1LL<<j)<str;j++)
            {
                if(str&(1LL<<j))
                {
                    val = (val + tmp)%primes[i];
                }
                tmp = (tmp*b)%primes[i];
            }

            if(val==0)
            {
                flag=1;
                ans.push_back(primes[i]);break;
            }
        }
        if(flag==0)
        {
            ans.clear();
            return ans;
        }
    }
    return ans;

}
int check(long long val, vector<int>&v)
{
    for(int b=2;b<=10;b++)
    {

        long long mod  = v[b-2], tmp = 1, x = 0;
        while(val)
        {
            if(val%2==1)x = (x + tmp)%mod;
            tmp = (tmp*b)%mod;
            val/=2;
        }
        if(x!=0)
        {
            return 0;
        }
    }
    return 1;
}
int main()
{
    p[0]=1;p[1]=1;
    for(int i=2;i<1000006;i++)
    {
        if(p[i]==0)
        {
            primes.push_back(i);
            for(int j=2;(long long)(j*i)<1000006;j++)
            {
                p[i*j] = 1;
            }
        }

    }


    freopen("GoogleCodeJam2016.txt", "r", stdin);
    freopen("GoogleCodeJam2016_output.txt", "w", stdout);

    int t;
    cin>>t;
    //t = 1000000;
    for(int tc=1;tc<=t;tc++)
    {
        cout<<"Case #"<<tc<<":"<<endl;

        int n, j;
        cin>>n>>j;

        long long val = (1LL<<(n-1)) + 1;
        int cnt = 0;
        for(int i=0;i<(1LL<<(n-1)) && cnt<j;i++)
        {
            long long tmp = val + i*2;
            vector<int> ans = f(tmp);
            if(ans.size()>0)
            {
                cnt++;
                long long x = tmp;
                string str = "";
                while(tmp)
                {
                    if(tmp%2==1)
                    {
                        str = "1"+str;
                    }
                    else
                    {
                        str = "0" + str;
                    }
                    tmp = tmp/2;
                }
                tmp = x;

                cout<<str;
                for(int b=2;b<=10;b++)
                {
                    cout<<" "<<ans[b-2];
                }
                cout<<endl;
/*
                for(int b = 2 ; b<=10 ; b++)
                {
                    long long val = 0, x = 1;
                    for(int i = str.size()-1;i>=0;i--)
                    {
                        if(str[i]=='1')
                        {
                            val = (val + x);
                        }
                        x = (x*b);
                    }
                    cout<<"base "<<b<<" "<<val<<" ";
                    cout<<ans[b-2]<<" "<<val%ans[b-2]<<endl;
                }


                if(check(tmp, ans)==0)
                {

                    cout<<"Wrong"<<endl;
                }
                cout<<"_________________________________________________________________________"<<endl;
                */
            }
        }


        //cout<<"Case #"<<tc<<": "<<"GOT IT!!"<<endl;
        //cout<<cnt<<endl;

    }


}
