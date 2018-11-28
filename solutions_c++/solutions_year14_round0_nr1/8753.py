#include <iostream>

using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int a[4][4]={0},fre[100]={0},b[4][4]={0};
        int x,y;
        cin>>x;
        x--;
        for(int p=0;p<4;p++)
        {
            for(int q=0;q<4;q++)
            {
                cin>>a[p][q];
                if(p==x)
                {
                    fre[a[p][q]]++;
                }
            }
        }
        cin>>y;
        y--;
        for(int p=0;p<4;p++)
        {
            for(int q=0;q<4;q++)
            {
                cin>>b[p][q];
                if(p==y)
                {
                    fre[b[p][q]]++;
                }
            }
        }
        int cnt=0,res=0;
        for(int p=0;p<=100;p++)
        {


                if(fre[p]>1)
                {


                cnt++;
                res=p;
                }

        }
        if(cnt==1)
        {
            cout<<"Case #"<<i<<": "<<res<<endl;
        }
        else if(cnt>1)
        {
            cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;

        }
        else
        {
            cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
        }


    }






    return 0;
}
