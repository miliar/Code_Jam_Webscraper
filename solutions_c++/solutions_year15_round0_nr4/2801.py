#include <bits/stdc++.h>
#define rep(I, N) for (int I = 0; I < (N); ++I)
using namespace std;
int main()
{

    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
int t;
cin>>t;
for(int z=1;z<=t;z++)
{
    int x,r,c;
    cin>>x>>r>>c;
    int air=r*c;
    if(x==1) {cout<<"Case #"<<z<<": "<<"GABRIEL"<<endl;continue;}
    if(x==2) {if(air%x!=0) {cout<<"Case #"<<z<<": "<<"RICHARD"<<endl;continue;} else {cout<<"Case #"<<z<<": "<<"GABRIEL"<<endl;continue;}}
    if(x==3) {if(air%x!=0||r==1||c==1) {cout<<"Case #"<<z<<": "<<"RICHARD"<<endl;continue;} else {cout<<"Case #"<<z<<": "<<"GABRIEL"<<endl;continue;}}
    if(x==4) {if(air==12||air==16) {cout<<"Case #"<<z<<": "<<"GABRIEL"<<endl;continue;}else {cout<<"Case #"<<z<<": "<<"RICHARD"<<endl;continue;}}



    cout<<"Case #"<<z<<": "<<"GABRIEL"<<endl;


}
return 0;
}
