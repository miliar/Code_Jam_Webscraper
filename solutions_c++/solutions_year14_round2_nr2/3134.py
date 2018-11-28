#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("in1.in","r",stdin);
    freopen("out1.txt","w",stdout);
    unsigned int A, B, K, testcase, temp;

    long long int ccount = 0;
    cin >> testcase;

    for(unsigned int te = 1; te <= testcase; te++)
    {
        ccount = 0;
        cin >> A >> B >> K;

        for (unsigned int i = 0; i < A; i++)
        {
            for (unsigned int j = 0; j < B; j++)
            {
                temp = j;
                temp = temp & i;

                if (temp < K)
                {
                    ccount++;
                }
            }
        }


        cout <<"Case #"<<te<<": "<< ccount << endl;
    }

    return 0;
}
