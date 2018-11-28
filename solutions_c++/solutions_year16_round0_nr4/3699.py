#include<bits/stdc++.h>
#define ll   long long

#define md 1000000007

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
   #ifndef ONLINE_JUDGE
            freopen("input.txt","r",stdin);
            freopen("output.txt","w",stdout);    
    #endif
      int test;
      cin>>test;
     for(int tst=1;tst<=test;tst++){
     	cout<<"Case #"<<tst<<": ";
     	int k,c,s;
        cin>>k>>c>>s;
        for(int i=1;i<=s;i++)
            cout<<i<<" ";
        cout<<endl;
     	
     }
    return 0;  
}
