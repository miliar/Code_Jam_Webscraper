#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin>>t;

    for(int tests=1;tests<=t;tests++)
    {
        string input;
        int smax;

        cin>>smax>>input;

        int currentlyStanding=input[0]-'0';
        int added=0;

        for(int i=1;i<input.size();i++)
        {
            if(currentlyStanding<i)
            {
                added++;
                currentlyStanding++;
            }
            currentlyStanding+=input[i]-'0';
        }

        cout<<"Case #"<<tests<<": "<<added<<endl;
    }

    return 0;
}
