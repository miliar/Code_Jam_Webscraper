using namespace std;
#include<iostream>
#include<conio.h>
int main()
{
    int r1,r2,i,j,k,n,c;
    int a[4][4],b[4][4];
    cin>>n;
    k=0;
    while(k<n)
    {
        cin>>r1;
        for(i=0;i<4;i++)
        {

            for(j=0;j<4;j++)
            {
                cin>>a[i][j];
            }

        }

        cin>>r2;
        for(i=0;i<4;i++)
        {

            for(j=0;j<4;j++)
            {
                cin>>b[i][j];
            }

        }

        c=0;
        int card;
        for(i=0;i<4;i++)
        {

            for(j=0;j<4;j++)
            {
                if(a[r1-1][i]==b[r2-1][j])
                {
                    c++;
                    card=a[r1-1][i];
                }
            }

        }
        k++;
        switch(c)
        {

            case 0:
                    cout<<"Case #"<<k<<": Volunteer cheated!\n";
                    break;
            case 1:
                    cout<<"Case #"<<k<<": "<<card<<"\n";
                    break;
            default:
                    cout<<"Case #"<<k<<": Bad magician!\n";


        }
}
return 0;
}
