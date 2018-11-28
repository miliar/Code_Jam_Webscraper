#include<iostream>
#include<vector>
#include<cstdlib>
#include<fstream>
#include<map>
using namespace std;
bool chk(char c)//true if c is consonant
{
    return c!='a' && c!='e' && c!='i' && c!='o' && c!='u'; 
}
int main(int argc, char *argv[]) {
    int tcs;
    cin>>tcs;
    for(int tc=1;tc<=tcs;tc++)
    {
        cout<<"Case #"<<tc<<": ";
        int n;
        string name;
        cin>>name;
        cin>>n;
        int len = name.size();
        int dp[len][len];
        int ans=0;
        for(int i=0;i<len;i++)//start
        {
            //cout<<"start at"<<i<<endl;
            for(int j=0;j<len-i;j++)//length
            {
                int end = i+j;
                //cout<<"chk at"<<end<<endl;
                if(j==0)
                {
                    if(chk(name[i]))dp[i][j] = 1;
                    else dp[i][j] = 0;
                }
                else
                {
                    if(chk(name[end]))dp[i][j] = dp[i][j-1]+1;
                    else dp[i][j] = 0;
                }
                if(dp[i][j]==n)
                {
                    //cout<<"yes"<<endl;
                    ans+=len-i-j;
                    break;
                }
                    
            }
            //cout<<endl;
        }
        /*
        for(int i=0;i<len;i++)
        {
            for(int j=0;j<len;j++)
            {
                cout<<dp[i][j]<<" ";
            }
            cout<<endl;
        }*/
        cout<<ans;
        cout<<endl;
    }
}