#include <iostream>
#include <stdio.h>
using namespace std;
int t,c,s,k;
int main()
{
    ios::sync_with_stdio(0);
    freopen("input.txt","r+",stdin);
    freopen("output.txt","w+",stdout);
    cin >> t;
    for (int ca=1;ca<=t;ca++)
    {
        cin >> k >> c >> s;
        cout << "Case #"<<ca<<": ";
        if (s==k)
        {
            for (int i=0;i<k-1;i++)
                cout << i+1<<" ";
            cout << k<< endl;
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
