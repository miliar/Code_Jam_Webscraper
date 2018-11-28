#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    long long a,b,c,d,e,f,g,h=0,t,n,m;
    string s,s1;
    vector<string> v;
    vector<string>::iterator i;

    cin>>t;
    while(t>0)
    {
        cin>>n>>m;
        long long mat[n][m];

        for(b=0; b<n; b++)
        {
            for(c=0; c<m; c++)
            {
                cin>>mat[b][c];
            }
        }

        for(b=0; b<n; b++)
        {
            for(c=0; c<m; c++)
            {
                d=0; e=0; h=0;
                if(n>m)
                {
                for(f=0; f<n; f++)
                {
                    if(f<m){if(mat[b][c]<mat[b][f]){d++;}}
                    if(mat[b][c]<mat[f][c]){e++;}
                    if(d>0 && e>0){h++; break;}
                }
                if(h>0){break;}
                }
                else
                {
                for(f=0; f<m; f++)
                {
                    if(mat[b][c]<mat[b][f]){d++;}
                    if(f<n){if(mat[b][c]<mat[f][c]){e++;}}

                    if(d>0 && e>0){h++; break;}
                }
                if(h>0){break;}
                }

            }
            if(h>0){break;}
        }
        if(h>0){v.push_back("NO");}
        else{v.push_back("YES");}

        t--;
    }

    for(b=1, i=v.begin(); i!=v.end(); i++, b++)
    {
        cout<<"Case #"<<b<<": "<<*i<<endl;
    }

    return 0;
}
