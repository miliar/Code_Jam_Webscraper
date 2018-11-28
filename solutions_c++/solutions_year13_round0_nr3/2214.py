#include <iostream>
#include <stdio.h>
#include <vector>
FILE *fin = fopen("input.in","r");
FILE *fout = fopen("output.txt","w");
using namespace std;
unsigned long long int list[]={
1,
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
2001002
};
void pro()
{
    unsigned long long int a,b,cnt=0,square;
    fscanf(fin,"%llu",&a);
    fscanf(fin,"%llu",&b);
    for(int i=0;i<46-8+1;i++)
    {
        square=list[i]*list[i];
        if(a<=square&&square<=b)
            cnt++;
    }
    fprintf(fout,"%llu\n",cnt);
}
int main()
{
    int n;
    fscanf(fin,"%d",&n);
    for(int i=0;i<n;i++)
    {
        fprintf(fout,"Case #%d: ",i+1);
        pro();
    }
    return 0;
}
