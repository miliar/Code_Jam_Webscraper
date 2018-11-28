#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

string arr[1000];
int c[1000] = {};

int main()
{
    ifstream in("bs.in");
    ofstream out("bout.txt");

    int t,n;
    in>>t;
    for(int x=1;x<=t;++x)
    {
        in>>n;
        for(int i=0;i<n;++i)
            {
                in>>arr[i];
                c[i] = i;
            }
        long long ans=0;
        {
            int visited['z'+1] = {};
            char prev = 0;
            int i,j;
            for(i=0;i<n;++i)
            {
                for(j=0;arr[c[i]][j];++j)
                {
                    if(!visited[arr[c[i]][j]])
                    {
                        visited[arr[c[i]][j]] = 1;
                        prev = arr[c[i]][j];
                    }
                    else if(prev!=arr[c[i]][j])
                    {
                        break;
                    }
                }
                if(arr[i][j])
                    break;
            }
            if(i>=n)
                ans = (ans+1)%1000000007;
        }
        while(next_permutation(c,c+n))
        {
            int visited['z'+1] = {};
            char prev = 0;
            int i,j;
            for(i=0;i<n;++i)
            {
                for(j=0;arr[c[i]][j];++j)
                {
                    if(!visited[arr[c[i]][j]])
                    {
                        visited[arr[c[i]][j]] = 1;
                        prev = arr[c[i]][j];
                    }
                    else if(prev!=arr[c[i]][j])
                    {
                        break;
                    }
                }
                if(arr[c[i]][j])
                    break;
            }
            if(i>=n)
                ans = (ans+1)%1000000007;
        }
        out<<"Case #"<<x<<": "<<ans<<'\n';
    }
    in.close();
    out.close();
    return 0;
}

