#include <iostream>
#include <string>
#include <cstdio>
using namespace std;
  //  0   1   2   3  4   5   6   7
   // i,  j , k,  1, -1, -i, -j, -k
int mul[8][8]={
{4,2,6,0,5,3,7,1},
{7,4,0,1,6,2,3,5},
{1,5,4,2,7,6,0,3},
{0,1,2,3,4,5,6,7},
{5,6,7,4,3,0,1,2},
{3,7,1,5,0,4,2,6},
{2,3,5,6,1,7,4,0},
{6,0,3,7,2,1,5,4},
};

int main()
{
  //  freopen("C-small-attempt0.in","r",stdin);
 //   freopen("C-small-attempt0.out","w",stdout);
    int T,i,cas,l,x;
    string str;
    string str_long;
    cin>>T;
    for(cas=1;cas<=T;cas++) {
        cin>>l>>x;
        cin>>str;
        str_long="";
        for(i=0;i<x;i++) {
            str_long=str_long+str;
        }
        int first=3;
        for(i=0;i<str_long.length();i++) {
            first=mul[first][str_long[i]-'i'];
            if(first==0) break;
        }
        if(first!=0) {
            cout<<"Case #"<<cas<<": NO"<<endl;
            continue;
        }


        int second=3;
        for(i=i+1;i<str_long.length();i++) {
            second=mul[second][str_long[i]-'i'];
            if(second==1) break;
        }
        if(second!=1) {
            cout<<"Case #"<<cas<<": NO"<<endl;
            continue;
        }

        int third=3;
        for(i=i+1;i<str_long.length();i++) {
            third=mul[third][str_long[i]-'i'];
        }
        if(third==2) cout<<"Case #"<<cas<<": YES"<<endl;
        else cout<<"Case #"<<cas<<": NO"<<endl;
    }
    return 0;
}
