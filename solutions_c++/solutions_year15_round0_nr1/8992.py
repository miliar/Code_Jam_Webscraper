#include<iostream>
using namespace std;

int main()
{
    int n,t;
    char c;
    char sl[1000];
    cin>>t;
    int j=0;
    while(j<t)
    {
        cin>>n;
        int i=0;
        int sm=n;
        n++;
        //cin>>c;
        while(n--)
        {
            cin>>c;

            sl[i]=c-48;

            i++;
        }
        //cin>>c;
        int t=0;
        int cn=0;
        for(int i=0;i<=sm;i++)
        {
            if(t<i)
            {
                cn=cn+i-t;
                t=t+i-t;
            }
           t=t+sl[i];
        }
        cout<<"Case #"<<j+1<<": "<<cn<<endl;
        j++;
    }

    return 0;
}

