#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
using namespace std;
int table[45]={1,
2,
3,
11,
22,
101,
111,
121,
202,
212,
1001,
1111,
2002,
10001,
10101,
10201,
11011,
11111,
11211,
20002,
20102,
100001,
101101,
110011,
111111,
200002,
1000001,
1001001,
1002001,
1010101,
1011101,
1012101,
1100011,
1101011,
1102011,
1110111,
1111111,
2000002,
2001002,};
int main()
{
    freopen("D:/C-large-1.in","r",stdin);
    freopen("D:/out.txt","w",stdout);
    int t,iii;
    cin>>t;
    for(iii=1;iii<=t;iii++){
        long long f,t;
        cin>>f>>t;
        long c=0;
        long long ff=sqrt(f);
        if(ff*ff!=f) ff++;
        long long tt=sqrt(t);
        for(int i=0;i<45;i++){
            if(table[i]>=ff&&table[i]<=tt)
                c++;
        }
        cout<<"Case #"<<iii<<": "<<c<<endl;

    }
}
