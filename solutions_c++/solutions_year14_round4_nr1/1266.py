#include<iostream>
#include<vector>
#include<string>
#include<cstdio>
#include<set>
using namespace std;

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
          int T,TEST = 1;
       cin >> T;
       while(T--)
       {
                 int N,X,a;
                 multiset<int> S;
                 int ans = 0;
                 cin >> N >> X;
                 for(int i = 0 ; i < N; i++)
                 {
                         cin >> a;
                         S.insert(-a);        
                 }          
                 while(S.size())
                 {
                                ans++;
                                int a =  -(*S.begin());
                                S.erase(S.begin());
                                multiset<int>::iterator it = S.lower_bound(a - X);
                                if(it != S.end())
                                {
                                      int b = -(*it);
                                      if(a + b <= X)
                                           S.erase(it);      
                                }              
                 }
                 cout << "Case #"<<TEST++<<": " << ans << endl;
       }
}
