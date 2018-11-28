#include<iomanip>
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
using namespace std;
int main()
{
	freopen( "D-small-attempt0.in", "r", stdin );
	freopen( "D-small-attempt0.out", "w", stdout );
    int t,no;
    cin>>t;
    for(no = 0;no < t;no++)
    {
        float a[10],b[10];
        int i,n,j = 0,w = 0,dw = 0,flag = 0;
        cin>>n;
        for(i = 0;i < n;i++)
            cin>>a[i];
        for(i = 0;i < n;i++)
            cin>>b[i];
        sort(a , a + n);
        sort(b , b + n);
        for(i = 0;i < n && j < n ;i++)
        {
            while(j < n)
            {
                if(a[i] < b[j++])
                    break;
            }
        }
        if(b[n-1]<a[i-1])        i--;
        w = n - i;
        j = 0;
        for(i = 0;i < n && j < n;i++)
        {
            while(j < n)
            {
                if(b[i] < a[j++])
                    break;
            }

        }
        if(a[n-1]<b[i-1])        i--;
        dw = i;
        cout<<"Case #"<<no + 1<<": "<<dw<<" "<<w<<"\n";
    }
    return 0;
}
