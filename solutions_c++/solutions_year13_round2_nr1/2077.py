#include <iostream>
#include <list>
#include <map>
#include <algorithm>
#include <string>
using namespace std;

int A;
int N;
int motes[1000];


int calc(int beg, int end, int &sum)
{
    int count = 0;
    int temp = beg;

    while(temp <= end)
    {
        temp += temp - 1;
        count++;
    }

    sum = temp;
    return count;
}


int main()
{

    int test_case;
    cin>>test_case;

    for(int i =0; i < test_case; ++i)
    {
        cin>>A>>N;
        for(int r = 0; r < N; ++r)
            cin>>motes[r];
    
        sort(motes, motes + N);
        int temp_size = A;
        int count = 0;

        for(int t = 0; t < N; ++t)
            {
                //int diff = motes[i] - temp_size; 
                if(temp_size == 1)
                {
                    count = N;
                    break;
                }

                int sum;
                int diff = calc(temp_size, motes[t], sum);
                if(diff >= N - t)
                {    
                    count += N - t;
                    break;
                }

                temp_size = sum + motes[t];
                count += diff;
            }

        cout<<"Case #"<<i+1<<": "<<count<<endl;
    }

    return 0;
}



