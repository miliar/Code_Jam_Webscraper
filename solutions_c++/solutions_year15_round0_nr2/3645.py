#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define SZ(a) ((int)a.size())
#define pb push_back

int arr[1010];

int main()
{
    freopen("B-large.in" , "r" , stdin);
    freopen("B-large.out" , "w+" , stdout);
    int tcase,cas=1;
    cin>>tcase;

    while(tcase--)
    {
        int n;
        cin>>n;
        int mxvalue = -1;
        for(int i = 0 ; i<n ; i++)
        {
            cin>>arr[i];
            if(mxvalue==-1 || mxvalue<arr[i]) mxvalue = arr[i];
        }

        int mx = -1;

        for(int i = 1 ; i<=mxvalue ; i++)
        {
            int tmp = 0;
            for(int j =0 ; j<n ; j++)
            {
                if(arr[j]<=i) continue;
                else
                {
                    tmp += (arr[j]/i);
                    if((arr[j]%i)==0) tmp--;
                }
            }
            if(mx==-1 || (i+tmp)<mx) mx= i+tmp;
        }

        cout<<"Case #"<<cas++<<": "<<mx<<endl;
    }

}
