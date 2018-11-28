#include<bits/stdc++.h>
#define rep(i,a,b) for(int i=a;i<b;++i)
#define rev(i,a,b) for(int i=a;i>b;i--)
using namespace std;
typedef long long int ll;
int t,ans;
string s1,s2;
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("sub2ndlar.txt");
    fin>>t;
    rep(i,1,t+1){
        fin>>s1;
        ans=0;s2="";
        rep(j,0,s1.length()) s2.push_back('+');
        char c='-';int cur=s1.length()-1;
        while(s2!=s1){
          //  cout<<s2<<" "<<endl;
            int j=cur;
            while(s1[j]!=c) j--;
      //  cout<<j<<" "<<c<<endl;
            rev(k,j,-1) s2[k]=c;
            if(c=='+') c='-';
            else c='+';
            cur=j;
            ans++;
        }
        fout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
