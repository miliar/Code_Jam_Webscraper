#include<iostream>
using namespace std;

int main()
{int pos1,pos2,flag=0,test;
    int t,i,j,order1[5][5],order2[5][5],x=0;
    cin>>t;
    while(t--)
    {
		flag=0;
        cin>>pos1;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                cin>>(order1[i][j]);
        cin>>(pos2);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                cin>>(order2[i][j]);
        j=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(order1[pos1][i]==order2[pos2][j])
                {
                     flag++;
cout<<flag<<" ";
                     test=order1[pos1][i];
                }
            }
        }
        if(flag==0)
            cout<<"Case #"<<++x<<": Volunteer cheated!"<<endl;
        else if(flag==1)
            cout<<"Case #"<<++x<<": "<<test<<endl;
        else
            cout<<"Case #"<<++x<<": Bad magician!"<<endl;
    }
    return 0;
}
#include<iostream>
using namespace std;

int main()
{int pos1,pos2,flag=0,test;
    int t,i,j,order1[5][5],order2[5][5],x=0;
    cin>>t;
    while(t--)
    {
		flag=0;
        cin>>pos1;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                cin>>(order1[i][j]);
        cin>>(pos2);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                cin>>(order2[i][j]);
        j=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(order1[pos1][i]==order2[pos2][j])
                {
                     flag++;
cout<<flag<<" ";
                     test=order1[pos1][i];
                }
            }
        }
        if(flag==0)
            cout<<"Case #"<<++x<<": Volunteer cheated!"<<endl;
        else if(flag==1)
            cout<<"Case #"<<++x<<": "<<test<<endl;
        else
            cout<<"Case #"<<++x<<": Bad magician!"<<endl;
    }
    return 0;
}
#include<iostream>
using namespace std;

int main()
{int pos1,pos2,flag=0,test;
    int t,i,j,order1[5][5],order2[5][5],x=0;
    cin>>t;
    while(t--)
    {
		flag=0;
        cin>>pos1;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                cin>>(order1[i][j]);
        cin>>(pos2);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                cin>>(order2[i][j]);
        j=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(order1[pos1][i]==order2[pos2][j])
                {
                     flag++;
                     test=order1[pos1][i];
                }
            }
        }
        if(flag==0)
            cout<<"Case #"<<++x<<": Volunteer cheated!"<<endl;
        else if(flag==1)
            cout<<"Case #"<<++x<<": "<<test<<endl;
        else
            cout<<"Case #"<<++x<<": Bad magician!"<<endl;
    }
    return 0;
}
