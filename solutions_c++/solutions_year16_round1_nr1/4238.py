#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T, t, temp1, temp2, i;
    string s, result;

    cin>>T;


    for(t=0; t<T; t++)
    {

        cin >> s;


        for (i=0; i<s.length(); i++)
            {if(s[i]>=result.front() || result.empty())
                result = s[i]+result;
            else
                result = result + s[i];}

            cout<<"Case #" << t+1 << ": " << result << endl;
            result.clear();
            s.clear();
    }




}
