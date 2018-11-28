#include <iostream>

using namespace std;

int main()
{
    int T, testcase=1;

    cin>>T;
    do
    {
        int count=0, temp,A,B,K;
        cin>>A>>B>>K;
        for(int i=0;i<=A-1;i++)
        {
            for(int j=0;j<=B-1;j++)
            {
                temp = i & j;
                if(temp<=K-1)
                {
                    count++;
                }
            }
        }
        cout<<"Case #"<<testcase<<": "<<count<<endl;
        testcase++;
    }while(testcase<=T);

    return 0;
}
