
#include<iostream>
#include<stack>
#include <sstream>
using namespace std;

void input() {

    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

}


int main(void)
{
    input();
    int t;
    cin>>t;
    int j=1;
    while(j<=t)
    {
        int x,r,c;
        cin>>x>>r>>c;

        if((r*c)%x!=0)
        {
           cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;


        }
        else
        {
            if(x==4)
            {
                if(r+c>6)
                {
                    cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
                }
                 else
                 {
                    cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
                 }
            }
            else if(x==3)
           {
                if(r+c>4 && r+c<8)
                {
                    cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
                }
                 else
                 {
                    cout<<"Case #"<<j<<": "<<"RICHARD"<<endl;
                 }
           }
           else
           {
                 cout<<"Case #"<<j<<": "<<"GABRIEL"<<endl;
           }
        }

        j++;

    }

    return 0;
}
