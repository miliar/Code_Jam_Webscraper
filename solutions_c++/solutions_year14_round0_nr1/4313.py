#include <iostream>

using namespace std;

int main()
{
    int T,testcase=1;
    int first, value, second, matchcount;
    int i,j;
    cin >> T;
    do
    {
        int a[16]= { };
        matchcount=0;
        cin >> first;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            {
                cin >> value;
                if(first==i)
                {
                    a[value-1]++;
                }
            }

        cin >> second;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            {
                cin >> value;
                if(second==i)
                {
                    a[value-1]++;
                    if(a[value-1] == 2)
                        matchcount++;
                }
            }

        if(matchcount == 0)
            cout <<"Case #"<<testcase<<": Volunteer cheated!"<<endl;

        else if(matchcount > 1)
            cout <<"Case #"<<testcase<<": Bad magician!"<<endl;

        else if(matchcount == 1)
        {
            for(i=0;i<16;i++)
            {
                if(a[i] == 2)
                {

                    cout <<"Case #"<<testcase<<": "<<i+1<<endl;
                    break;
                }
            }
        }

        testcase++;
    }while(testcase<=T);

    return 0;
}
