#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(false);
    int t;
    cin>>t;
    int k=1;
    while(t--)
    {
        int n;
        cin>>n;
        int arr[200][200];
        int co[3000];
        int visited[3000];
        fill(co,co+3000,0);
        fill(visited,visited+3000,0);
        for(int i=0;i<2*n-1;i++)
        {
            for(int j=0;j<n;j++)
            {
                cin>>arr[i][j];
                co[arr[i][j]]+=1;
            }
        }
        vector<int >v;
        for(int i=0;i<2*n-1;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(co[arr[i][j]]%2!=0&&visited[arr[i][j]]==0)
                {
                   v.push_back(arr[i][j]);
                   visited[arr[i][j]]=1;
                }
            }
        }
        sort(v.begin(),v.end());
        cout<<"Case #"<<k<<":"<<" ";
        for(int i=0;i<n;i++)
        {
            cout<<v[i]<<" ";
        }
        cout<<"\n";
        k++;
    }
    return 0;
}
