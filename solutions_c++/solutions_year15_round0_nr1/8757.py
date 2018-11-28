#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    int t ,i,j=0,k,smax,sum,add;
    cin>>t;
while(j<t)
    {
    k=add=0;
    cin>>smax;
    char s[smax+1];
    cin>>s;
    int c[smax+1];
    sum=s[0]-48;
    for(i=0;i<smax;i++)
    {

        s[i+1]=s[i+1]-48;
        if(i+1<=sum)
            sum+=s[i+1];
        else
          {  add=i+1-sum;
        sum+=add+s[i+1];
          c[k++]=add;}
    }
    sum=0;
    for(i=0;i<k;i++)
        sum+=c[i];

    printf("Case #%d: %d\n",j+1,sum);

j++;
}
}
