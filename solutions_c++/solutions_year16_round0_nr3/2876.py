#include<bits/stdc++.h>

using namespace std;
ifstream fin("C-small-attempt0.in");
ofstream fout("out5.txt");
long long power(long long a,long long b)
{
    if(b==1)
        return a;
    if(b==0)
        return 1;
    if(b%2==0)
    {
        long long x=power(a,b/2);
        return x*x;
    }
    else
        return a*power(a,b-1);
}
long long int convert(string a,int bas)
{
    long long ans=0;
    int ap=0;
    for(int i=a.length()-1;i>=0;i--)
    {
        ans+=(a[i]-'0')*power(bas,ap);
        ap++;
    }
    return ans;
}
bool prime(long long a)
{
    if(a==1|| a==0)
        return false;
    for(int i=2;i<=sqrt(a);i++)
    {
        if(a%i==0)
            return false;
    }
    return true;
}
int main()
{
    int t;
    cin>>t;
    for(int c=1;c<=t;c++)
    {
        int n,j1;
        cin>>n>>j1;
        int cou=0;
        cout<<"Case #"<<c<<":"<<"\n";
        for(int i=1;i<=(1<<n);i++)
        {
            string s1;
            int k=n-1;
            vector<int>v;
            if(((i&(1<<0))) && (i&(1<<k)))
            {
            for(int j=0;j<n;j++)
            {
                if(i&(1<<j))
                {
                    s1+="1";
                }
                else
                    s1+="0";
            }
            bool flag=false;
            int ind=0;
            for(int k=2;k<=10;k++)
            {

                long long int a=convert(s1,k);
                if(!prime(a))
                {
                    for(int l=2;l<=sqrt(a);l++)
                    {
                        if(a%l==0)
                        {
                            v.push_back(l);
                            break;
                        }
                    }
                }
                else
                {
                    flag=true;
                    break;
                }

            }
            if(flag==false)
            {
                cout<<s1<<" ";
                for(int i=0;i<v.size();i++)
                    cout<<v[i]<<" ";
                cout<<"\n";
                cou++;
            }
            if(cou==j1)
                break;
            }
        }
    }
}
