#include <bits/stdc++.h>
using namespace std;
int T,N,arr[1001];
char a;
int counter,test,peop;
int x,r,c;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>T;
    test=T;
    while(T--)
    {
cin>>x>>r>>c;
if(x==1)
    cout<<"CASE #"<<test-T<<": GABRIEL"<<"\n";
if(x==2)
{
    if((r==1 && c==1) ||(c==1 && r==1)||(r==1 && c==3)||(r==3 && c==1) || (r==3 && c==3))
        cout<<"CASE #"<<test-T<<": RICHARD"<<"\n";
    else
        cout<<"CASE #"<<test-T<<": GABRIEL"<<"\n";
}
if(x==3)
{
    if((c==2 && r==3) ||(c==3 && r==2) || (c==4 && r==3)||(c==3 && r==4)||(c==3 && r==3))
        cout<<"CASE #"<<test-T<<": GABRIEL"<<"\n";
    else
        cout<<"CASE #"<<test-T<<": RICHARD"<<"\n";
}
    if(x==4)
    {
        if((c==4 && r==4)||(c==4 && r==3) || (r==4 && c==3))
        cout<<"CASE #"<<test-T<<": GABRIEL"<<"\n";
        else
        cout<<"CASE #"<<test-T<<": RICHARD"<<"\n";
    }


}
    return 0;
}
