#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}

using namespace std;
void solve(){
    int f=in()-1;
    int a[2][4][4];
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            a[0][i][j]=in();
        }
    }
    int j=in()-1;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            a[1][i][j]=in();
        }
    }
    vector<int>out,v,v1;
    for(int i=0;i<4;i++){
        v.push_back(a[0][f][i]);
        v1.push_back(a[1][j][i]);
    }
    sort(v.begin(),v.end());sort(v1.begin(),v1.end());
    set_intersection(v.begin(),v.end(),v1.begin(),v1.end(),insert_iterator<vector <int> > (out,out.begin() ));
    if(!out.size())cout<<"Volunteer cheated!";
    else if(out.size()>1)cout<<"Bad magician!";
    else cout<<out[0];
    cout<<endl;
}
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
     freopen("output.txt", "w", stdout);
    int cases=in();
    for(int tc=1;tc<=cases&&printf("Case %d: ",tc++);)solve();
    return 0;
}
