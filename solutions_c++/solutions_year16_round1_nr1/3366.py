#include <iostream>
using namespace std;

int main()
{
    int t=1,T;
    cin>>T;

    while(t <= T)
    {
        string input;
        cin>>input;

        int n=input.size();

        string output;
        output=input[0];
        for(int i=1;i<n;++i)
        {
            if(input[i] >= output[0])
                output=input[i]+output;

            else output=output+input[i];
        }

        cout<<"Case #"<<t<<": "<<output<<'\n';

        ++t;
    }

    return 0;
}
