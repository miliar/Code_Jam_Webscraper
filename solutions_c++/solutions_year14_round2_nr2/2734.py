#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main()
{
    int cases;
    int a, b, k;
    int total=0;
    bool check = false;
    cin >> cases;

    for(int i =0; i<cases; ++i)
    {
        total = 0;
        cin >> a >> b >> k;
        
        for(int j =0; j<a ; ++j)
        {
            for(int w=0; w<b; ++w)
            {
                int temp;
                temp  = j&w;
                if(temp < k)
                    total++;
            }
        }
        
        cout << "Case #" << i+1 << ": " << total << endl;
    }
}