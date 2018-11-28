#include<iostream>
#include<math.h>
#include<vector>
#include<stdio.h>
using namespace std;
#define lim 1001
unsigned long long int b,c;
bool palin(unsigned long long int a)
{
     b=0,c=a;
    while(a)
    {
        b=b*10+a%10;
        a/=10;
    }
    if(b==c)
        return true;
    return false;
}
int main()
{
    int i;
    unsigned long long int k;
    vector<unsigned long long int> v;
    for(i=1;i<40;i++)
    {
        if(!palin(i))
            continue;
            //cout<<i<<endl;
        k=i*i;
        if(palin(k))
        {
            v.push_back(k);
            //cout<<v[v.size()-1]<<endl;
        }

    }
    int t,a,b;
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int ts=1;ts<=t;ts++)
    {
        scanf("%d %d",&a,&b);
        //int p1,p2;
        int cnt=0;
        for(i=0;i<v.size();i++)
        {
            if(v[i]<=b && v[i]>=a)
                cnt++;
        }

        printf("Case #%d: %d\n",ts,cnt);
    }


}

