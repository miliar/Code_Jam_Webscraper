#include<bits/stdc++.h>
#define rep(i,a,b) for(int i=a;i<b;++i)
#define rev(i,a,b) for(int i=a;i>b;i--)
using namespace std;
typedef long long int ll;
int t,n,ans;
bool mark[10];
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("A-large.in");
    fout.open("submitlarge.txt");
    fin>>t;
    rep(i,1,t+1){
        fin>>n;
        if(!n) {
            fout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        ans=n;
        rep(j,0,10) mark[j]=0;
        while(1){
            int tem=ans;
            while(tem){
                mark[tem%10]=1;
                tem/=10;
            }
            int ch=0;
            rep(j,0,10) if(mark[j]) ch++;
            if(ch==10) break;
            ans+=n;
        }
        fout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
