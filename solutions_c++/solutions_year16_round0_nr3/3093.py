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

static int d[15];
char str[50];

int main()
{
    int T;
    scanf("%d", &T);
    for(int i=2; i<=10; i++)
    {
        if(i%2)
            d[i] = 2;
        else
            d[i] = 3;
    }
    d[6] = 7;

    for(int ctr=1; ctr<=T; ctr++)
    {
        int N, J;
        cin>>N>>J;
        cout<<"Case #"<<ctr<<": "<<endl;
        int cnt = 0;
        for(int i=1;cnt<J && i<=N-5; i++)
        {
            for(int j=i+2;cnt<J && j<=N-3; j++)
            {
                cnt++;
                memset(str, '0', N*sizeof(char));
                str[N] = '\0';
                str[0] = str[N-1] = '1';
                str[i] = str[i+1] = '1';
                str[j] = str[j+1] = '1';

                cout<<str;
                for(int k=2; k<=10; k++)
                    cout<<" "<<d[k];
                cout<<endl;
            }
        }
    }
    return 0;
}
