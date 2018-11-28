#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    FILE *fin = freopen("D-small-attempt1.in", "r", stdin);
	FILE *fout = freopen("B-large.out", "w", stdout);
    long long int ans,index=1;
    long long int t,K,C,S,x;
    cin>>t;
    while(t--)
    {
        cin>>K>>C>>S;
        ans=1;

        if(K==1){cout<<"Case "<<"#"<<index<<": "<<1<<"\n";index++;}
        else if(C==1){cout<<"Case "<<"#"<<index<<": ";for(int i=1;i<=K;i++){ cout<<i<<" ";}
        cout<<"\n";index++;}
        else
        {
          for(int i=0;i<C;i++)
          {
              ans=ans*K;
          }
          x=ans/K;
          cout<<"Case "<<"#"<<index<<": "<<2<<" ";
          for(int i=2;i<=S-1;i++)
          {
              cout<<x*i<<" ";
          }
          cout<<"\n";
          index++;
        }
    }
    return 0;
}
