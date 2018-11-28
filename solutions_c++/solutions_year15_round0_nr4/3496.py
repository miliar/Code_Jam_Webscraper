#include<iostream>
#include<fstream>
using namespace std;
ifstream in("aa.in");
ofstream out("output.txt");
int n,r,c;
void ooo(int i,int ans)
{
    if(ans)
    {
        out<<"Case #"<<i+1<<": GABRIEL"<<'\n';
        cout<<"Case #"<<i+1<<": GABRIEL"<<'\n';
    }
    else
    {
        out<<"Case #"<<i+1<<": RICHARD"<<'\n';
        cout<<"Case #"<<i+1<<": RICHARD"<<'\n';
    }

}
int main()
{

    int func();
    int i,t;
    in>>t;
    int ans[102];
    for(i=0; i<t; i++)
        ans[i]=func();
    for(i=0; i<t; i++)
        ooo(i,ans[i]);
    return 0;
}
bool comp(int cn,int cr,int cc)
{
    if(cn==n&&((cr==r&&cc==c)||cc==r&&cr==c))
        return true;
    else
        return false;
}

int func()
{
    in>>n>>r>>c;
    if (comp(1,1,1))
        return 1;
    else if(comp(2,1,1))
        return 0;
    else if(comp(3,1,1))
        return 0;
    else if(comp(4,1,1))
        return 0;
    else if(comp(1,1,2))
        return 1;
    else if(comp(2,1,2))
        return 1;
    else if(comp(3,1,2))
        return 0;
    else if(comp(4,1,2))
        return 0;
    else if(comp(1,1,3))
        return 1;
    else if(comp(2,1,3))
        return 0;
    else if(comp(3,1,3))
        return 0;
    else if(comp(4,1,3))
        return 0;
    else if(comp(1,1,4))
        return 1;
    else if(comp(2,1,4))
        return 1;
    else if(comp(3,1,4))
        return 0;
    else if(comp(4,1,4))
        return 0;
    else if(comp(1,2,2))
        return 1;
    else if(comp(2,2,2))
        return 1;
    else if(comp(3,2,2))
        return 0;
    else if(comp(4,2,2))
        return 0;
    else if(comp(1,2,3))
        return 1;
    else if(comp(2,2,3))
        return 1;
    else if(comp(3,2,3))
        return 1;
    else if(comp(4,2,3))
        return 0;
    else if(comp(1,2,4))
        return 1;
    else if(comp(2,2,4))
        return 1;
    else if(comp(3,2,4))
        return 0;
    else if(comp(4,2,4))
        return 0;
    else if(comp(1,3,3))
        return 1;
    else if(comp(2,3,3))
        return 0;
    else if(comp(3,3,3))
        return 1;
    else if(comp(4,3,3))
        return 0;
    else if(comp(1,3,4))
        return 1;
    else if(comp(2,3,4))
        return 1;
    else if(comp(3,3,4))
        return 1;
    else if(comp(4,3,4))
        return 1;
    else if(comp(1,4,4))
        return 1;
    else if(comp(2,4,4))
        return 1;
    else if(comp(3,4,4))
        return 0;
    else if(comp(4,4,4))
        return 1;
}
