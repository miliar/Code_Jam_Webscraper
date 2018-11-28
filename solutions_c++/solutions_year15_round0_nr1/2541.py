#include<iostream>
#include <stdio.h>
#include <fstream>
using namespace std;
int main()
{
    ifstream fg;
    ofstream fw;
    fg.open("Al0.in");
    fw.open("solution_l0");

    if(!fg.is_open() || !fw.is_open())
    {
        cout<<"Files are unable to open."<<endl;
        return 0;
    }
    int t;
    fg >> t;
    for(int i=0;i<t;i++)
    {
        int n;
        fg >> n;
        string s;
        fg >> s;
        //fw<< n <<" "<<s<<endl;
        int ans = 0;
        int sum = int(s[0]) - 48;
        for(int j=1;j<=n;j++)
        {
            if( sum < j )
            {
                //cout<<"a ";
                int t = (j - sum);
                ans = ans + t;
                sum = sum + t;
            }
            //cout<<ans<<" "<<sum<<"   ";
            sum = sum + int(s[j]) - 48;

        }
        //cout<<endl;
        fw<<"Case #"<<i+1<<": "<<ans<<endl;

    }

    return 0;
}
