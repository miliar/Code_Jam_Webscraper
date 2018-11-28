#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int x,r,c;
    for(int i=0;i<n;i++)
    {
        cin>>x>>r>>c;
        bool s=true;
        if(x>=7)
            s=false;
        else if(x>r&&x>c)
            s=false;
        else if((r*c)%x!=0)
            s=false;
        else if((x+1)/2>min(r,c))
            s=false;
        else if(x==1||x==2||x==3)
            s=true;
        else if(x==4)
            s=min(r,c)>2;
        else if(x==5)
            s!=(min(r,c)==3&&max(r,c)==5);
        else if(x==6)
            s=min(r,c)>3;

        if(s==true)
            cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
        else
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
    }
    return 0;
}
