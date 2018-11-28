#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,x,r,c;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        cin>>x>>r>>c;
        if((r*c)%x!=0 || ((x>r)&&(x>c)))
        {
            cout<<"Case #"<<j<<": RICHARD"<<endl;
        }
        else
        {
            if(x==1)
            {
                cout<<"Case #"<<j<<": GABRIEL"<<endl;
            }
            if(x==2)
            {
                if(r>=2 || c>=2)
                {
                    cout<<"Case #"<<j<<": GABRIEL"<<endl;
                }
                else
                {
                    cout<<"Case #"<<j<<": RICHARD"<<endl;
                }

            }
            else if(x==3)
            {
                if(r>=2 && c>=2)
                {
                    cout<<"Case #"<<j<<": GABRIEL"<<endl;
                }
                else
                {
                    cout<<"Case #"<<j<<": RICHARD"<<endl;
                }
            }
            else if(x==4)
            {
                if(r>2 && c>2)
                {
                    cout<<"Case #"<<j<<": GABRIEL"<<endl;
                }
                else
                {
                    cout<<"Case #"<<j<<": RICHARD"<<endl;
                }
            }
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
