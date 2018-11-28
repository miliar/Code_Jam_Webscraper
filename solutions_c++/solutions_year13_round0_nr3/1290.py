#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

/*struct numtype
{
    int num[105];
    int len;
}nummin,nummax,numtemp;*/
long long nummin,nummax,numtemp;
bool judge(long long num)
{
    char ch[20];
    int i,j;
    for(i=0;num!=0;i++)
    {
        ch[i]=num%10+'0';
        num/=10;
        //cout<<ch[i];
    }
    //cout<<endl<<i<<endl;
    i--;
    j=i;
    for(;i>=0;i--)
    {
        if(ch[j-i]!=ch[i]) return false;
    }
    return true;
}
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("C-large-1.out","w",stdout);
    int T,cas=0,c=0;
    long long numb[40]={0};

    for(long long num=1;num<=10000000;num++)
    {
        if(judge(num))
        {
            if(judge(num*num))
            {
                c++;
                numb[c]=num*num;
                //cout<<numb[c]<<endl;
            }
        }
    }
    cin>>T;
    while(T--)
    {
        cas++;
        cin>>nummin>>nummax;
        int k=0;
        for(int i=1;i<=39;i++)
        {
            if(numb[i]>=nummin&&numb[i]<=nummax) k++;
        }
        cout<<"Case #"<<cas<<": "<<k<<endl;

    }
    return 0;
}
