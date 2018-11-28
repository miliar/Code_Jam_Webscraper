#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<cassert>
#include<sstream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

int main()
{
    int t,T,y,n,m,i,j,k,x;
    int a[5]={1,4,9,121,484};
    cin >>t;
    T=t;
    while(t--)
    {
        int count=0;
        cin >>x>>y;
        for(i=0;i<5;i++)
            if(a[i]<=y && a[i]>=x)count++;
        cout << "Case #"<<T-t<<": "<<count<<"\n";
    }
    return 0;
}

