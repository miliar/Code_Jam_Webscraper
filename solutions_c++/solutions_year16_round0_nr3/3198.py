#include <bits/stdc++.h>
using namespace std;
#define ll long long
bool p[100000001];
ll t,n,j,primes[6000005],k;
int main()
{
    memset(p,false,sizeof(p));
    for(ll i=2;i<=100000000;i++)
    {
        if(!p[i])
        {
            //cout<<i<<endl;
            j=2*i;
            primes[k++]=i;
            while(j<=100000000)
            {
                p[j]=true;
                j+=i;
            }
        }
    }
    ifstream inFile;
    ofstream outFile;
    inFile.open("input.txt");//("B-small-attempt0.in");
    outFile.open("output_file.txt");
    inFile>>t;
    outFile<<"Case #"<<t<<":"<<endl;
    int cnt=0;
    inFile>>n>>j;
    for(ll i=(1<<15);i<(1<<16);i++)
    {
    //    cout<<i<<endl;
        if( (i&1)==0 )
            continue;
        vector<ll>v;
        for(ll k=2;k<=10;k++)
        {
            ll chk=i,mul=1,ans=0;
            while(chk)
            {
                ans+= (mul* (chk&1));
                chk=chk>>1;
                mul*=k;
            }
            //ans+=mul;
            //cout<<ans<<endl;
            for(int j=0;primes[j]*primes[j]<=ans;j++)
            {
                if(ans%primes[j]==0)
                {
                    v.push_back(primes[j]);
                    break;
                }
            }
        }
        if(v.size()==9)
        {
            cnt++;
            if(cnt>500)
                break;
            ll digit=i;
            stack<int>st;
            stack<int>st2;
            while(digit)
            {
                st.push(digit&1);
                st2.push(digit&1);
                digit=digit>>1;
            }
            while(!st.empty())
            {
                outFile<<st.top();
                st.pop();
            }
            while(!st2.empty())
            {
                outFile<<st2.top();
                st2.pop();
            }
            outFile<<" ";
            for(int j=0;j<v.size();j++)
                outFile<<v[j]<<" ";
            outFile<<endl;
        }
    }
    return 0;
}
