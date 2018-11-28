#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <limits>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807
#define INF 2000000000
#define PI acos(-1.0)
#define EPS 1e-9
#define LL long long
#define mod 1000000007
#define pb push_back
#define mp make_pair

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    cin >> t;
    int tt=t;
    while(t--)
    {
        int n;
        scanf("%d",&n);
        string edit[105],input[105];
        for(int i=0;i<n;i++)
        {
            cin >> input[i];
            edit[i]+=input[i][0];
            for(int j=1;j<(int)input[i].size();j++)
            {
                if(input[i][j] != input[i][j-1])
                {
                    edit[i]+=input[i][j];
                }
            }
        }
        bool equa = true;
        for(int i=1;i<n;i++)
        {
            if(edit[i] != edit[i-1])
            {
                equa = false;
                break;
            }
        }
        printf("Case #%d: ",tt-t);
        if(equa)
        {
            int counter=0,arr[n];
            memset(arr,0,sizeof(arr));
            for(int i=0;i<input[0].size();i++)
            {
                int temp=1,arrr[n];
                memset(arrr,0,sizeof(arrr));
                for(int j=1;j<n;j++)
                {
                    while(input[j][arr[j]]==input[0][i] && arr[j] < input[j].size())
                    {
                        arr[j]++;
                        arrr[j]++;
                    }
                }
                while(input[0][i] == input[0][i+1] && i < input[0].size())
                {
                    i++;
                    temp++;
                }
                arrr[0] = temp;
                int mini=INF_MAX;
                for(int j=0;j<n;j++)
                {
                    int tempo=0;
                    for(int k=0;k<n;k++)
                    {
                        tempo+=abs(arrr[k] - arrr[j]);
                    }
                    mini=min(mini,tempo);
                }
                counter+=mini;
            }
            printf("%d\n",counter);
        }
        else printf("Fegla Won\n");
    }
    return 0;
}
