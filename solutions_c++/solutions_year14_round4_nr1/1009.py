#include<iostream>
#include<string.h>
using namespace std;

int a[100000],vis[100000];
int main()
{
    freopen ("output.txt","w",stdout);
    freopen ("o.txt","r",stdin);
    int t, o = 0;  
    cin >> t;
     while ( t-- )
     {
           int n,m;
           cin >> n>>m;
           memset(vis,0,sizeof vis );
           for ( int i = 0; i < n; i++ )
           cin >> a[i];
           sort(a,a+n);
           int ans = 0;
           int i = n-1,j = n - 2;
           for (; i >= 0; i-- )
           { 
                if (!vis[i] )
                {
                            vis[i] = 1;
                            for ( j = i-1; j >= 0; j-- )
                            {
                                if (vis[j] == 0 && a[i] + a[j] <= m )
                                {
                                     vis[i] = vis[j] = 1;
                                     break;
                                } 
                            }
                            ans++;
                }
           }
           cout << "Case" << " #"<< ++o<<": "<< ans << endl;
      }                                    
  //string s;
 // cin >> s;
  //cout << "pogo"<<endl;
//    cout << "Hello World"<<endl;
}
