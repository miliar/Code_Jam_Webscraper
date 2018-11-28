#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int i, j, k, tCase=1, nCase, n, m;
    int arr[101][101], rMax[101], cMax[101], Given[101][101];
    cin >> nCase;
    while(nCase--)
    {
        cin >> n >> m;
        for(i=0; i<n; i++)
            for(j=0; j<m; j++)
                cin >> arr[i][j], Given[i][j]=100;

        memset(rMax, 0, sizeof(rMax));
        memset(cMax, 0, sizeof(cMax));

        for(i=0; i<n; i++)
            for(j=0; j<m; j++)
                rMax[i] = max(rMax[i], arr[i][j]);

        for(i=0; i<m; i++)
            for(j=0; j<n; j++)
                cMax[i] = max(cMax[i], arr[j][i]);

        for(i=0; i<n; i++)
            for(j=0; j<m; j++)
                if(arr[i][j]==rMax[i]) Given[i][j]=rMax[i];

        for(i=0; i<m; i++)
            for(j=0; j<n; j++)
                if(arr[j][i]==cMax[i]) Given[j][i]=cMax[i];


        int flag=0;

        for(i=0; i<n; i++)
            for(j=0; j<m; j++)
                if(arr[i][j]!=Given[i][j])
                {
                    flag=1;
                    break;
                }

        if(flag==0) cout << "Case #" << tCase++ << ": YES" <<endl;
        else cout << "Case #" << tCase++ << ": NO" <<endl;

    }
    return 0;
}


