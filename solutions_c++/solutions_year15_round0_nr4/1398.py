#include <iostream>
using namespace std;

int main()
{
    int t,k=1;
    cin>>t;
    while(t--)
    {
        int x,r,c,v=0;
        cin>>x>>r>>c;
        if(r*c%x==0)
        {
            if(x==4)
            {
                if(c>=3 && r>=3)
                v=1;
            }
            else
            if(x==3)
            {
                if(c>=2 && r>=2)
                v=1;
            }
            else
            v=1;
         
        }
        cout<<"Case #"<<k++<<": ";
        if(v==1)
        cout<<"GABRIEL"<<endl;
        else
        cout<<"RICHARD"<<endl;
    }
    return 0;
}
