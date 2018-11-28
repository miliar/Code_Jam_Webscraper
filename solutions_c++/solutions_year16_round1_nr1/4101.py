#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
using namespace std;

string s,f,temp,temp1;

int main()
{
    freopen("gcj_16_r1_a_1_in.txt","r",stdin);
    freopen("gcj_16_r1_a_1_new_out.txt","w",stdout);
    int t;
    cin>>t;
    for(int qq=1;qq<=t;qq++) {
        cout<<"Case #"<<qq<<": ";
        int i,j,n,m;
        cin>>s;
        n=s.length(); f="";
        for(i=0;i<n;i++) {
            temp=f+s[i];
            temp1=s[i]+f;
            if(temp>temp1) f=temp;
            else f=temp1;
        }
        cout<<f<<"\n";
    }
}
