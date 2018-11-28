#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream in("A-small-attempt0.in");
    cin.rdbuf(in.rdbuf());
    ofstream out("output.txt");
    cout.rdbuf(out.rdbuf());

    int T = 0;
    int ans1 = 0;
    int ans2 = 0;
    int arr1[5][5];
    int arr2[5][5];

    cin>>T;

    for(int t = 0;t<T;t++)
    {
        cin>>ans1;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>arr1[i][j];
            }
        }

        cin>>ans2;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>arr2[i][j];
            }
        }

        int matchNum = 0;
        int match = 0;
        for(int a = 1; a <=4;a++)
        {
            int cmp1 = arr1[ans1][a];
            for(int b = 1;b<=4;b++)
            {
                int cmp2 = arr2[ans2][b];
                if(cmp1 == cmp2)
                {
                    matchNum++;
                    match = cmp1;
                }
            }
        }

        if(matchNum == 0)
        {
            cout<<"Case #"<<t+1<<": "<<"Volunteer cheated!"<<endl;
        }
        else if(matchNum == 1)
        {
            cout<<"Case #"<<t+1<<": "<<match<<endl;
        }
        else if(matchNum > 1)
        {
            cout<<"Case #"<<t+1<<": "<<"Bad magician!"<<endl;
        }

    }// end of for T



    return 0;
}
