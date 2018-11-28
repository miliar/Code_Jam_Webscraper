#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define X first
#define Y second
int main()
{

freopen("A-large (3).in","rt",stdin);
freopen("out.txt","wt",stdout);
    int t;
    cin>>t;
    for(int c=1; c<=t; c++)
    {
        pair<int,int> p[27];
        int n,pa;
        float total=0.0;
        cin>>n;
        for(int i=0; i<n; i++)
        {
            cin>>pa;
            total+=pa;
            p[i]=make_pair(pa,i);
        }
        cout<<"Case #"<<c<<":";
        while(total>0)
        {
            sort(p,p+n);
            if(n==2)
            {
                p[0].X--;
                p[1].X--;
                total-=2;
                cout<<" AB";
            }
            else
            {
                if(p[n-1].X>1)
                {
                        p[n-1].X-=1;
                        total-=1.0;
                        cout<<" "<<(char)(p[n-1].Y+'A');

                }
                else
                {

                 if(p[n-3].X>0){
                    p[n-1].X-=1;
                        total-=1.0;
                        cout<<" "<<(char)(p[n-1].Y+'A');
                 }else{
                  p[n-1].X-=1;
                  p[n-2].X-=1;
                        total-=2.0;
                        cout<<" "<<(char)(p[n-1].Y+'A')<<(char)(p[n-2].Y+'A');
                 }


                }
            }

        }
        cout<<endl;

    }



    return 0;
}
