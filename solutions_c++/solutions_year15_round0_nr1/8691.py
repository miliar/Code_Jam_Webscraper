#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int T,N;
    ifstream ifs("A-large.in");
    ifs >> T;
    ofstream ki("answer.txt");
    //cerr << T;
    for(int t=0;t<T;t++)
    {
        string nums;
        //cout << t <<endl;
        int S=0;
        int ret=0;
        ifs >> N;
        ifs >> nums;
        for(int i=0;i<=N;i++)
        {
            int n = (int) nums[i] - 48;
            //cout << n+1 <<" ";
            //cerr << n+1 << " ";

            if(S<i)
            {
                ret+=i-S;
                S=i;
            }
            S+=n;
        }
        ki <<"Case #" <<t+1 << ": "<<ret<<endl;
    }

    return 0;
}
