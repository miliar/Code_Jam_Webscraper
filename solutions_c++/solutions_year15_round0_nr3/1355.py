#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#include<set>
#define ll long long int
#define mk make_pair
#define pb push_back
using namespace std;


char val[4][4]={'1','i','j','k','i','1','k','j','j','k','1','i','k','j','i','1'};
char mp[122];
int sgn[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};
char s[11111];
char arr[10001][10001];
int arr1[10001][10001];

int main()
{
    int t,w=1;
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    mp[1]=0;
    mp['i'-'a']=1;
    mp['j'-'a']=2;
    mp['k'-'a']=3;
    cin>>t;
    while(t--)
    {
        int i,j,k,l,m,co=0;
        string p;
        cin>>l>>m;
        cin>>p;
        for(i=0;i<m;i++)
            for(j=0;j<l;j++)
                s[co++]=p[j];
        l=l*m;
        for(i=0;i<l;i++)
        {
            arr[i][i]=s[i];
            arr1[i][i]=1;
            for(j=i+1;j<l;j++)
            {
                int v1,v2;
                v2=mp[s[j]-'a'];
                if(arr[i][j-1]=='1')
                    v1=0;
                else
                    v1=mp[arr[i][j-1]-'a'];
                arr[i][j]=val[v1][v2];
                arr1[i][j]=arr1[i][j-1]*sgn[v1][v2];
            }
        }
        int flag=0;
        for(i=1;i<l-1;i++)
        {
            for(j=i;j<l-1;j++)
            {
                if(arr[0][i-1]=='i'&&arr[i][j]=='j'&&arr[j+1][l-1]=='k'&&arr1[0][i-1]==1&&arr1[i][j]==1&&arr1[j+1][l-1]==1)
                {
                    flag=1;
                    break;
                }
            }
            if(flag)    break;
        }
        if(flag)
            cout<<"Case #"<<w<<": "<<"YES\n";
        else
            cout<<"Case #"<<w<<": "<<"NO\n";
        w++;
    }
    return 0;
}

