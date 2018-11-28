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
    int N, X;
    cin >> N >> X;

    list<int> sizes;
    for(int i=0; i<N; i++)
    {
        int size;
        cin >> size;
        sizes.push_back(size);
    }

    sizes.sort();

    int numdisks=0;
    while(!sizes.empty())
    {
        numdisks++;
        int size = sizes.back();
        sizes.pop_back();

        if(sizes.empty() || size+*sizes.begin()>X)
        {
            continue;
        }

        for(list<int>::iterator it = sizes.begin(); it != sizes.end(); ++it)
        {
            list<int>::iterator next = it;
            ++next;
            if(next == sizes.end() || *next+size > X)
            {
                sizes.erase(it);
                break;
            }
        }
    }
    cout << " " << numdisks << endl;
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


