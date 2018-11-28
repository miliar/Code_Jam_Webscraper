#include <fstream>
using namespace std;
int a[100][100], m, n, t, p[101], s;
int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int k, i, j, x, q, w;
    bool ok;
    cin>>t;
    for(k=0; k<t; ++k)
    {
        cin>>n>>m;
        for(i=0; i<n; ++i)
        {
            for(j=0; j<m; ++j)
            {
                cin>>a[i][j];
                p[a[i][j]]++;
                s+=a[i][j];
            }
        }
        while(s!=0)
        {
            while(p[x]==0) x++;
            for(i=0; i<n; ++i)
            {
                for(j=0; j<m; ++j)
                {
                    if(a[i][j]==x && p[x]!=0)
                    {
                        for(q=0; q<n; ++q)
                        {
                            if(a[q][j]!=x && a[q][j]!=0)
                            {
                                break;
                            }
                        }
                        if(q==n)
                        {
                            for(q=0; q<n; ++q)
                            {
                                if(a[q][j]!=0)
                                {
                                    s=s-x;
                                    p[x]--;
                                }
                                a[q][j]=0;
                            }
                        }
                        for(w=0; w<m; ++w)
                        {
                            if(a[i][w]!=x && a[i][w]!=0)
                            {
                                break;
                            }
                        }
                        if(w==m)
                        {
                            for(w=0; w<m; ++w)
                            {
                                if(a[i][w]!=0)
                                {
                                    s=s-x;
                                    p[x]--;
                                }
                                a[i][w]=0;
                            }
                        }
                        if(w<m && q<n)
                        {
                            cout<<"Case #"<<k+1<<": NO\n";
                            goto A;
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<k+1<<": YES\n";
A:      for(i=0; i<n; ++i)
        {
            for(j=0; j<m; ++j)
            {
                a[i][j]=0;
            }
        }
        for(i=0; i<101; ++i) p[i]=0;
        s=0;
        x=0;
    }
    return 0;
}
