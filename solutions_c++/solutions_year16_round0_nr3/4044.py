#include <iostream>
#include<bits/stdc++.h>
using namespace std;
#define int long long

int n,m,cnt=0LL;
int power(int a,int b)
{
    int ans=1LL;
    for(int i=1;i<=b;i++)
        ans*=a;
    return ans;
}
void recurse(int i,string s)
{
    //cout<<i<<endl;
    if(i==n)
    {
        //cout<<"*"<<endl;
        vector<int> vt;
        set<int> s1;
        s+="1";
        int r,i,j,f,k;
        for(i=2;i<=10;i++)
        {
            r=0LL;
            k=0LL;
            for(j=s.size()-1;j>=0LL;j--)
            {
                if(s[j]=='1')
                r+=power(i,k);
                k++;
            }
            vt.push_back(r);
        }
        for(i=0;i<vt.size();i++)
        {
            f=0;
            for(j=2;j<=(int)sqrt(vt[i]);j++)
                if(vt[i]%j==0)
            {
                f=1;
                break;
            }
            if(f==0)
                return ;
        }

        if(cnt<m)
        {
            //cout<<vt[0]<<endl;
         cnt++;

         cout<<s<<" ";
        for(i=0;i<vt.size();i++)
        {
            //if(i==0)
              //  cout<<vt[0]<<endl;
            for(j=2;j<=(int)sqrt(vt[i]);j++)
                if(vt[i]%j==0 )
            {
                 if(s1.find(j) == s1.end())
                    {
                        cout<<j<<" ";
                        s1.insert(j);
                        break;

                    }
                    if(s1.find(vt[i]/j) == s1.end())
                        {
                        cout<<vt[i]/j<<" ";
                        s1.insert(vt[i]/j);
                        break;
                        }

            }
        }
        cout<<endl;
    }
    vt.clear();
    s1.clear();
    return ;

    }
    recurse(i+1,s+"0");
    recurse(i+1,s+"1");
}

main()
{
    freopen("input.txt","r",stdin);
    freopen("output7.txt","w",stdout);
    int t;
    cin>>t;
    cin>>n>>m;
    //cout<<n<<" "<<m<<endl;
    printf("Case #1: ");
    cout<<endl;
    recurse(2,"1");
    return 0;
}
