#include <iostream>
#include <list>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <map>
#include <set>

using namespace std;

void testCase()
{
    int N;
    cin >> N;
    vector<int> A;
    for(int i=0; i<N; i++)
    {
        int tmp;
        cin >> tmp;
        A.push_back(tmp);
    }

    int count=0;

    while(!A.empty())
    {
        int minidx = -1;
        int min = numeric_limits<int>::max();
        for(int i=0; i<(int)A.size(); i++)
        {
            if(A[i] < min)
            {
                min = A[i];
                minidx = i;
            }
        }

        int numswaps = std::min(minidx, (int)A.size()-minidx-1);
        count += numswaps;
        A.erase(A.begin()+minidx);
    }
    cout << " " << count << endl;
}

int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        cout << "Case #" << i+1 << ":";
        testCase();
    }
}


