#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
using namespace std;
void out(int t,int rg)
{
    string s;
    if(rg==0)s="RICHARD";
    else s="GABRIEL";
    printf("Case #%d: ",t);
    cout<<s<<endl;
}
int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        int X,R,C;
        cin>>X>>R>>C;
        if(X==1)out(t,1);
        else if(X==2){
            if(R*C%2!=0)out(t,0);
            else out(t,1);
        }
        else if(X==3){
            if(R==1||C==1)out(t,0);
            else if(R*C%3!=0) out(t,0);
            else out(t,1);
        }
        else if(X==4){
            if(R==1||C==1)out(t,0);
            else if(R*C<4)out(t,0);
            else if(R*C%4!=0) out(t,0);
            else if(R<3||C<3) out(t,0);
            else out(t,1);
        }
    }
}
