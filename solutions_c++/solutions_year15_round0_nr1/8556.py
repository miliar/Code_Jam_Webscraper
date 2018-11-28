#include <iostream>
#include <iostream>
#include <fstream>
using namespace std;

int main()
{

// basic file operations




    ofstream cout;
    ifstream cin;
    cout.open ("example.txt");
    cin.open ("small.txt");

    int test,smax,counter,ans;
    string s;
    cin>>test;
    for(int t=1;t<=test;t++)
    {
        cin>>smax>>s;
        counter=0;
        ans=0;
        for(int i=0;i<=smax;i++)
        {
             if(i>counter)
             {
                    ans+=(i-counter);
                    counter=i;
             }
             counter+=(s[i]-'0');

        }

        cout<<"Case #"<<t<<": "<<ans <<endl;
    }
    cout.close();
    return 0;
}
