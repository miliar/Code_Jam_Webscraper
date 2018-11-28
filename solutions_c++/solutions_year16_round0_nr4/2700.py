#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main() {
    int t,k,c,s,count=1,i;
    cin>>t;
    while(t--)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<count++<<": ";

        for(i=0;i<k;i++)
            cout<<i+1<<" ";

        cout<<endl;
    }
    return 0;
}
