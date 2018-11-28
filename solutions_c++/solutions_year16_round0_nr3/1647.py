#include<bits/stdc++.h>
using namespace std;
string s;
//int sol[]={5,2,5,2,5,2,5,2,5};
int sol[]={3,2,5,2,5,2,3,2,11};
int n,j;
void solve()
{
 //   if(cnt==j || a>n-2 ||b>n-2 || c>n-2 || d>n-2 || a>=b || c>=d)
   //     return;
    // print sol
    int cnt=0;
    for (int a = 2; a <= n-2; a=a+2)
    {
        if(cnt==j)
            break;
        for (int b = a+2; b <= n-2; b=b+2)
        {
            if(cnt==j)
                break;
             for (int e = b+2; e <= n-2; e=e+2)
            {
                if(cnt==j)
                    break;
                for (int f = e+2; f <= n-2; f=f+2)
                {
                    if(cnt==j)
                        break;
             
                    for (int c = 1; c <=n-2 ; c=c+2)
                    {
                        if(cnt==j)
                            break;
                        for (int d = c+2; d <= n-2; d=d+2)
                        {
                            if(cnt==j)
                                break;
                            for (int g = d+2; g <=n-2 ; g=g+2)
                            {
                                if(cnt==j)
                                    break;
                                for (int h = g+2; h <= n-2; h=h+2)
                                {
                                    if(cnt==j)
                                        break;
                                    //cout<<a<<" "<<b<<" "<<e<<" "<<f<<" "<<c<<" "<<d<<" "<<g<<" "<<h<<endl;
                                    
                                    int i,j;
                                    for(i=0;i<n;i++)
                                    {
                                        if(i==0 || i==n-1)
                                            cout<<"1";   
                                        else if(i==a||i==b||i==c||i==d ||i==e||i==f||i==g||i==h)
                                            cout<<"1";
                                        else
                                            cout<<"0";
                                    }
                                    for(i=0;i<9;i++)
                                    {
                                        cout<<" "<<sol[i];
                                    }
                                    cout<<endl;
                                    cnt++;
                                    
                                }
                            }
                        }
                    }   
                }
            }
        }
    }
}
int main()
{
    int t,it;
    cin>>t;
    for(it=1;it<=t;it++)
    {
        cin>>n>>j;
        cout<<"Case #"<<it<<":\n";

        solve();
    //    cout<<endl;
    }
    return 0;
}
