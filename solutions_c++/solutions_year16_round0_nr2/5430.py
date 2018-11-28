#include <bits/stdc++.h>
using namespace std;

int main() 
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin>>n;
    int q=0;
    for(int i=0;i<n;i++)
    {
        string s;
        cin>>s;
        int e=(int)s.size();
        int an=0;
        for(;;)
        {
            bool f=1;
            for(int j=0;j<e;j++)f&=(s[j]=='+');
            if(f)break;
            f=1;
            for(int j=0;j<e;j++)f&=(s[j]=='-');
            if(f){an++;break;}

            int p=e-1,g=0;
            for(int j=0;j<e;j++)
            {
                g+=(!j||s[j]!=s[j-1]);
                if(g==2){p=j-1;break;}
            }
            
            an++;
            for(int j=0;j<p-j;j++)swap(s[j],s[p-j]);
            for(int j=0;j<=p;j++)if(s[j]=='+')s[j]='-';else s[j]='+';
        }
        cout<<"Case #"<<++q<<": "<<an<<endl;
    }    
    return 0;
}
