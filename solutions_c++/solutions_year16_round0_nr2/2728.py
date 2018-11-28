#include <iostream>
#include <string>

using namespace std;

int ans(string curr)
{
    int tot=0;
    for(int x=0;x<curr.size()-1;x++)
        if(curr[x]!=curr[x+1])
            tot++;
    if(curr[curr.size()-1]=='-')
        tot++;
    return tot;
}

int main()
{
    int n;
    cin >> n;
    cin.ignore('\n', '\n');
    string curr;
    for(int x=0;x<n;x++){
        getline(cin,curr);
        cout << "Case #" << (x+1) << ": " << ans(curr) << endl;
    }
}
