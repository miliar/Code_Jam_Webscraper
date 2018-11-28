#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int tests;
    cin>>tests;
    for(int i=1; i<=tests; i++)
    {
        int s;
        cin>>s;
        int counter = 0;
        int min_number=0;
        int val;
        string input;
        cin>>input;
        for(int i=0; i<=s; i++)
        {
            if(i > 0)
            {
                counter+=val;
                min_number+=max(0, i-counter-min_number);
            }
            val = input[i]-'0';
        }
        cout<<"Case #"<<i<<": "<<min_number<<endl;
    }
    return 0;
}
