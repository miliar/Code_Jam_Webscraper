#include <iostream>
#include <stdio.h>

using namespace std;
int main()
{
    int a[105][10],b[105][10],cas=1,t,row,n,m,i,j;
    freopen ("A-small-attempt0.in","r",stdin);
    freopen ("output.txt","w",stdout);
    //fropen ("a.txt","w");
    //fopen ("output.txt","r");
    cin>>t;
    while(t--)
    {
        cin>>n;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>a[i][j];
            }
        }
        cin>>m;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>b[i][j];
            }
        }
        int cnt = 0;
        for(j=1;j<=4;j++)
        {
            for(i=1;i<=4;i++)
            {
                if(a[n][i]==b[m][j])
                {
                    row = a[n][i];
                    cnt++;
                }
            }
        }

        if(cnt==0)
        {
            cout<<"Case #"<<cas++<<": Volunteer cheated!"<<endl;


        }else if(cnt==1)
        {
            cout<<"Case #"<<cas++<<": "<<row<<endl;
        }
        else
        {
            cout<<"Case #"<<cas++<<": Bad magician!"<<endl;
        }
        //cout<<"cnt val"<<cnt<<"row="<<row<<endl;

    }

    //fclose(stdout);

    return 0;
}
