#include<iostream>
using namespace std;
int main()
{int p1,p2,flag=0,test;
    int t,i,j,o1[5][5],o2[5][5],x=0;
    cin>>t;
    while(t--)
    {
		flag=0;
        cin>>p1;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                cin>>(o1[i][j]);
        cin>>(p2);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                cin>>(o2[i][j]);
        j=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(o1[p1][i]==o2[p2][j])
                {
                     flag++;
cout<<flag<<" ";
                     test=o1[p1][i];
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
