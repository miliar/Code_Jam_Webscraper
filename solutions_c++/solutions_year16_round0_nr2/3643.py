#include <bits/stdc++.h>
#define INF 1000000000
#define mod 1000000007
#define vi vector<int>
#define vit vector<int>::iterator
#define ll long long
#define ii pair<int, int>
#define vii vector<ii>
#define pb push_back
#define mp make_pair
using namespace std;

char str[105];
static int arr[105];

int main()
{
    int T;
    scanf("%d", &T);
    for(int ctr=1; ctr<=T; ctr++)
    {
        int n, i, res = 0;
        cin>>str;
        for(n=0; str[n]!='\0'; n++)
            arr[n] = (str[n]=='+') ? 1 : -1;
        int change = 0, sign = 1;
        for(i=0; i<n; i++)
        {
            if(arr[i]!=sign)
            {
                change++;
                sign = arr[i];
            }
        }
        if(arr[0]==-1)
        {
            if(change%2==0)
                change--;
            res = change;
        }
        else
        {
            if(change%2==1)
                change++;
            res = change;
        }
        cout<<"Case #"<<ctr<<": "<<res<<endl;
    }
    return 0;
}
