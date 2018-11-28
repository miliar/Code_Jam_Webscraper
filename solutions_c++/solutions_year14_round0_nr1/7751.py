#include<iostream>
using namespace std;
int main()
{
    int t,a1,a2,m1[4][4],m2[4][4],ans,c,d,n=0;
    cin>>t;
    while(t--)
    {
        ans=-1;
        cin>>a1;
        for(c=0;c<4;c++)
            for(d=0;d<4;d++)
                cin>>m1[c][d];
        cin>>a2;
        a1--;a2--;
        for(c=0;c<4;c++)
            for(d=0;d<4;d++)
                cin>>m2[c][d];
        for(c=0;c<4;c++)
            for(d=0;d<4;d++)
                if(m1[a1][c]==m2[a2][d])
                {
                    if(ans==-1)
                        ans=m1[a1][c];
                    else
                        ans=0;
                }
        if(ans==-1)
            cout<<"Case #"<<++n<<": Volunteer cheated!"<<endl;
        else if(ans==0)
            cout<<"Case #"<<++n<<": Bad magician!"<<endl;
        else
            cout<<"Case #"<<++n<<": "<<ans<<endl;
    }
    return 0;
}
