#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <stack>
#include <cstring>
#define LL long long
using namespace std;
string s1[105];
string s2[105];
int dp[105][105];
vector<char> s3[105];
int arr[105];
int cc=0;
int main()
{
   freopen("C:\\Users\\Balasubramanian\\Downloads\\A-small-attempt0.in", "r", stdin);
    freopen("C:\\Users\\Balasubramanian\\Desktop\\C++progs\\outputa1.out", "w", stdout);
    int t1;
    cin>>t1;
    while(t1--)
    {
        cc++;memset(dp,0,sizeof(dp));
        cout<<"Case #"<<cc<<": ";
    memset(arr,0,sizeof(arr));
    for(int i=0;i<105;++i)s3[i].clear();
    int n;
    cin>>n;
    for(int i=0;i<n;++i)
    {cin>>s1[i];s2[i]=s1[i];}
    //cout<<"1";
    for(int i=0;i<n;++i)
    {
       for(int j=0;j<s1[i].size();++j)
        {
            if(j==0)
            s3[i].push_back(s1[i][j]);
            else
            {
                if(s1[i][j-1]!=s1[i][j])
                s3[i].push_back(s1[i][j]);
            }
        }
    }
    
   
    int t=1;
    string s(s3[0].begin(),s3[0].end());
   
    for(int i=0;i<n;++i)
    {
        string h(s3[i].begin(),s3[i].end());
        //cout<<h<<endl;
        if(s!=h){t=0;break;}
    }
    if(t==0)
    {
        cout<<"Fegla Won";
    }
    else 
    {
        for(int i=0;i<n;++i)
        {
            
            int k=0;int count=0;
            for(int j=0;j<s1[i].size()&&k<s1[i].size();++j)
            {
                if(s[k]==s1[i][j])
                {
                    count++;
                }
                else
                {
                    k++;
                    j--;
                    dp[i][k-1]=count;
                    count=0;
                }
            }dp[i][k]=count;
        }
      /*  for(int i=0;i<n;++i)
        {for(int j=0;j<s.size();++j)
        cout<<dp[i][j]<<" ";cout<<endl;}*/
        for(int j=0;j<s.size();++j)
        {
            double sum=0;
            for(int i=0;i<n;++i)
        {
            sum+=dp[i][j];
            
        }
        double u=sum/(double)(n);
        if(u-floor(u)>=ceil(u)-u){
            u=ceil(u);}
            
        else u=floor(u);
        //cout<<u<<" ";
        int ans=0;
        for(int i=0;i<n;++i)
        ans+=abs(dp[i][j]-u);
        arr[j]=ans;
        }
        
        int anse=0;
        for(int i=0;i<s.size();++i)
        {
            anse+=arr[i];
        }
        cout<<anse;
        
        
    }
    cout<<endl;
    
    
    
    
    
    
    
    
    
    
    
    }
    
    
    return 0;
}
