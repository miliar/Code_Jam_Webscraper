#include<bits/stdc++.h>
using namespace std;
int main()
{

    freopen("D-small-attempt0.in","r",stdin);
    freopen("kk.out","w",stdout);
    int t,p=0;
    map<pair<int,pair<int,int> > ,string > mp;

    mp[{4,{2,2}}]="RICHARD";
    mp[{4,{2,3}}]="RICHARD";
    mp[{4,{2,4}}]="RICHARD";
    mp[{4,{3,3}}]="RICHARD";
    mp[{4,{3,4}}]="GABRIEL";
    mp[{4,{4,4}}]="GABRIEL";
    mp[{4,{1,1}}]="RICHARD";
    mp[{4,{1,2}}]="RICHARD";
    mp[{4,{1,3}}]="RICHARD";
    mp[{4,{1,4}}]="RICHARD";



    mp[{3,{1,1}}]="RICHARD";
    mp[{3,{1,2}}]="RICHARD";
    mp[{3,{2,2}}]="RICHARD";
    mp[{3,{2,3}}]="GABRIEL";
    mp[{3,{2,4}}]="RICHARD";
    mp[{3,{3,3}}]="GABRIEL";
    mp[{3,{3,4}}]="GABRIEL";
    mp[{3,{4,4}}]="RICHARD";
    mp[{3,{1,3}}]="RICHARD";
    mp[{3,{1,4}}]="RICHARD";




    mp[{2,{1,1}}]="RICHARD";
    mp[{2,{1,2}}]="GABRIEL";
    mp[{2,{1,3}}]="RICHARD";
    mp[{2,{1,4}}]="GABRIEL";
    mp[{2,{2,2}}]="GABRIEL";
    mp[{2,{2,3}}]="GABRIEL";
    mp[{2,{2,4}}]="GABRIEL";
    mp[{2,{3,3}}]="RICHARD";
    mp[{2,{3,4}}]="GABRIEL";
    mp[{2,{4,4}}]="GABRIEL";



    cin>>t;
    while(t--)
    {
        int x,y,z;
        cin>>x>>y>>z;
        printf("Case #%d: ",++p);
        if(x==1)
            cout<<"GABRIEL";
        else
        {

if(y>z)

    swap(y,z);
string s=mp[{x,{y,z}}];
cout<<s;
        }
        printf("\n");
    }
    return 0;
}
