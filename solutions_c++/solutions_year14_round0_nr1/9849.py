#include <iostream>

using namespace std;
int rowa[5][5];
int rowb[5][5];
int main()
{
    int num;
    int temp=0;
    cin >> num;
    while(num--)
    {
        int ansa;
        int ansb;
        int tempa[5]={0};
        int tempb[5]={0};
        cin>>ansa;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                cin>>rowa[i][j];
                if(i==ansa)
                    tempa[j]=rowa[i][j];
            }
        }
        cin>>ansb;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                cin>>rowb[i][j];
                if(i==ansb)
                    tempb[j]=rowb[i][j];
            }
        }
        int anspos;
        int count=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(tempa[i]==tempb[j])
                {
                    count++;
                    anspos=tempa[i];
                }
            }
        }
        if(count==1) cout<<"Case #"<<++temp<<": "<<anspos<<endl;
        else if(count==0) cout<<"Case #"<<++temp<<": Volunteer cheated!"<<endl;
        else cout<<"Case #"<<++temp<<": Bad magician!"<<endl;
    }
}
