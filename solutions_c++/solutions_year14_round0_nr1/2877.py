//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
using namespace std;
int ar[100];
int main()
{
    int a,s,d,f,g,h,j,k,l,q;
    freopen("in.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    cin>>a;
    for(s=1;s<=a;s++)
    {
        for(d=1;d<=16;d++) ar[d]=0;
        cin>>f;
        for(g=1;g<=4;g++)
        {
            for(h=1;h<=4;h++)
            {
                cin>>j;
                if(g==f) ar[j]++;
            }
        }
        cin>>f;
        for(g=1;g<=4;g++)
        {
            for(h=1;h<=4;h++)
            {
                cin>>j;
                if(g==f) ar[j]++;
            }
        }
        h=0;
        for(j=1;j<=16;j++)
        {
            if(ar[j]>1)
            {
                h++;
                k=j;
            }
        }
        printf("Case #%d: ",s);
        if(h==0) cout<<"Volunteer cheated!\n";
        else if(h>1) cout<<"Bad magician!\n";
        else cout<<k<<endl;
    }
}
