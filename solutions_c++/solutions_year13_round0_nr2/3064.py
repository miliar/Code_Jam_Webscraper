#include<iostream>
using namespace std;
int mat[150][150]={0};
int cp[150][150]={0};
int main()
{
    int t=0,cas=1;
    cin>>t;
    while(t--){
        int n,m;
        int maxiv[110]={0},maxjv[110]={0};
        cin>>n>>m;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>mat[i][j];
                if (mat[i][j]>maxiv[i]) maxiv[i]=mat[i][j];
                if(mat[i][j]>maxjv[j]) maxjv[j]=mat[i][j];
            }
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cp[i][j]=maxiv[i];
            }

        }
        for(int j=0;j<m;j++)
        {
            for(int i=0;i<n;i++)
            {
                if(cp[i][j]>maxjv[j])
                {
                    cp[i][j]=maxjv[j];
                }
            }
        }
        int flag=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(mat[i][j]!=cp[i][j])
                {
                    flag=1;
                    break;
                }
            }
            if(flag) break;
        }
        cout<<"Case #"<<cas++<<": ";
        if(flag) cout<<"NO\n";
        else cout<<"YES\n";
    }
    return 0;
}
