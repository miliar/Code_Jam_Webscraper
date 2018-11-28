#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int tt=1;tt <=t ;tt++)
    {
        int smax;
        string s;
        cin >> smax >> s;
        long int extra = 0;
        long int arr[10001] ;
        arr[0] = s[0]-'0';
        for(int i=1;i<=smax;i++)
        {
            if(s[i]-'0' > 0)
            {
                if(i <= arr[i-1])
                {
                    arr[i] = arr[i-1] + s[i]-'0';
                }
                else
                {
                    extra += i - arr[i-1];
                    arr[i] = i + s[i]-'0';
                }
            }
            else
            {
                arr[i] = arr[i-1];
            }
            ///cout << arr[i] << endl;
               }
        cout << "Case #"<<tt<<": "<<extra<<endl;
    }
    return 0;
}
