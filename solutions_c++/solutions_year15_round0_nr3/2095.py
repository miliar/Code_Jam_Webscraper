#include<bits/stdc++.h>
using namespace std;
#define ll long long
int mat[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};   // 1=1 i=2 j=3 k=4
int eval( int a, int b )
{
    int sign=(a*b>0?1:-1);
    a=abs(a);
    b=abs(b);
    return sign*mat[a][b];
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("CHHoutput.txt","w",stdout);
    int t;  cin>>t;
    for( int tt=1; tt<=t; ++tt ) {
        ll l,x;     cin>>l>>x;
        string s,oris;   cin>>s;    oris=s;
        for( ; x>1; x-- ) s+=oris;
        bool formI=false,formK=false,IK=false;
        int v=1,uv=1,idxi,idxk;
        for( int i=0,j=s.length()-1; i<s.length() && j>=0 ; ++i,--j ) {
            v=eval(v,s[i]-'g');
            if(not formI && v==2 ) {
                formI=true;
                idxi=i;
            }

            uv=eval(s[j]-'g',uv);
            if( not formK && uv==4 ) {
                formK=true;
                idxk=j;
            }

            if( formI && formK && idxi<idxk) {
                IK=true;
            }
        }
        if( v==-1 && IK) {
            cout<<"Case #"<<tt<<": "<<"YES"<<endl;
            continue;
        } else {
            cout<<"Case #"<<tt<<": "<<"NO"<<endl;
            continue;
        }
    }
    return 0;
}
