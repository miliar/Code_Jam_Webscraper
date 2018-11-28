#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int q=t;
    while(t--)
    {
        int n;
        cin>>n;
        int a[6][6],x;
        int aux[20]={0};
        for(int i=1;i<=4;i++)
        {
            if(i==n)
            {
                for(int j=1;j<=4;j++)
                {
                    cin>>a[i][j];
                    aux[a[i][j]]++;
                }
            }
            else for(int j=1;j<=4;j++)cin>>x;

        }
        cin>>n;
        int count=0,y;
        for(int i=1;i<=4;i++)
        {
            if(i==n)
            {
                for(int j=1;j<=4;j++)
                {
                    cin>>a[i][j];
                    if(aux[a[i][j]]>0)
                    {
                        y=a[i][j];
                        count++;
                    }
                }
            }
            else for(int j=1;j<=4;j++)cin>>x;

        }
        if(count==1)
        {
            cout<<"Case #"<<q-t<<": "<<y<<"\n";

        }
        else if(count==0)
        {
            cout<<"Case #"<<q-t<<": "<<"Volunteer cheated!\n";
        }
        else
        cout<<"Case #"<<q-t<<": "<<"Bad magician!\n";

    }
   // cout << "Hello world!" << endl;
    return 0;
}
