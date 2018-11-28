#include <iostream>
#include <cstdio>
using namespace std;

bool isChosen[10];

bool checkTen()
{
    int i,count=0;
    for(i=0;i<5;i++)
    {
        if(isChosen[i*2] && isChosen[i*2+1])
            count+=2;
    }
    if(count == 10)
        return true;
}

int main()
{
    long int userIn[100],test,temp;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int inputCount;
    int i;
    cin>>inputCount;

    for(i=0;i<inputCount;i++)
    {
        cin>>userIn[i];
    }

    for(i=0;i<inputCount;i++)
    {
        for(int x=0;x<10;x++)
        {
            isChosen[x]=false;
        }
        if(i!=0)
            cout<<"\n";
        test = userIn[i];
        if(test == 0){
            cout<<"Case #"<<i+1<<": INSOMNIA";
            continue;
        }
        for(int j=1;;j++)
        {
            test = userIn[i]*j;
            int saveTest = test;
            while(test!=0)
            {
                temp = test%10;
                test/=10;
                isChosen[temp] = true;
            }
            if(checkTen())
            {
                cout<<"Case #"<<i+1<<": "<<saveTest;
                break;
            }
        }
    }
    return 0;
}
