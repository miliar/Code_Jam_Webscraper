#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("op.txt", "w", stdout);

    int T,t;
    int i,j,k;
    int r;
    int n[16],no,res;

    cin>>t;
    T=t;
    while(t--)
    {
        for (i=0;i<16;i++)
            n[i]=0;

        res=0;

        cin>>r;
        for (i=0;i<16;i++)
        {
            cin>>no;
            if (i/4+1==r)
                n[no-1]++;
        }

        cin>>r;
        for (i=0;i<16;i++)
        {
            cin>>no;
            if (i/4+1==r)
                n[no-1]++;
        }
        for (i=0;i<16;i++)
            if (n[i]>1) {res++;no=i+1;}

        if (res==0) cout<<"Case #"<<T-t<<": Volunteer cheated!\n";
        else if (res>1) cout<<"Case #"<<T-t<<": Bad magician!\n";
        else cout<<"Case #"<<T-t<<": "<<no<<endl;
    }
    return 0;
}
