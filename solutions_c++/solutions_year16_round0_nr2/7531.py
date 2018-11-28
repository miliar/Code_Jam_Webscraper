#include <vector>
#include <algorithm>
#include<string>
#include <iostream>

using namespace std;

int main()
{
    int numCase;
    cin >> numCase;
    int i, j, n;
    long long ans;
    char r;
    string str;
    for (i = 0; i < numCase; i++)
    {    ans=0;

        cin>>str;
        r=str[0];
        for(j=1;j<str.size();j++){
           if(r!=str[j]){
               r=str[j];
               ans++;
           }

        }
        if(r=='-')
            ans++;


        cout << "Case #" << (i+1) << ": " << ans << endl;
    }
    return 0;
}
