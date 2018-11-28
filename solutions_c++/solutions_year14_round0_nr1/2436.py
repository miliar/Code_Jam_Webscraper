#include<bits/stdtr1c++.h>
using namespace std;



int main()
{
    #ifndef ONLINE_JUDGE
        freopen("2.in","r",stdin);
        freopen("3.txt","w",stdout);
        
    #endif // ONLINE_JUDGE
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    
    int t,r;
    cin>>t;
    
    int ic=1;
    while(t--)
    {
        cin>>r;
        map<int,int> m;
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int a;
                cin>>a;
                if(i==r)
                    m[a]=1;
            }
        }
        
        string two="Bad magician!";
        string ch="Volunteer cheated!";
        int c=0,ret;
         cin>>r;
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int a;
                cin>>a;
                if(i==r)
                   {
                       if(m.count(a))
                       {
                           c++;
                           ret=a;
                       }
                   }
            }
        }
        
        cout<<"Case #"<<ic++<<": ";
        if(c==0)
            cout<<ch<<endl;
        else if(c==1)
            cout<<ret<<endl;
        else
            cout<<two<<endl;
        
    }
    
    return 0;
    
}
