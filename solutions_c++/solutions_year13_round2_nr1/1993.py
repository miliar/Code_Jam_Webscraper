#include <iostream>

using namespace std;

bool isHuiWen(int i)
{
    int weishu=1;int tempi=i;
    while(tempi/10!=0){weishu++;tempi=tempi/10;}
    int *p=new int [weishu];

    for(int j=0;j<weishu;++j)
    {
        p[j]=i%10;//cout<<p[j]<<endl;
        i=(i-p[j])/10;
    }
    //cout<<weishu<<"miao"<<endl;
    for(int k=0;k<weishu;++k)
    {
        if(p[k] != p[weishu-k-1]) return 0;
    }
    return 1;
}

int main()
{
    int a;cin>>a;
    cout<<isHuiWen(a);
}

/*int main()
{
   int i;cin>>i;
    int weishu=1;int tempi=i;
    while(tempi/10!=0){weishu++;tempi=tempi/10;}
    int *p=new int [weishu];

    for(int j=0;j<weishu;++j)
    {
        p[j]=i%10;//cout<<p[j]<<endl;
        i=(i-p[j])/10;
    }
    //cout<<weishu<<"miao"<<endl;
    for(int k=0;k<weishu;++k)
    {
        if(p[k] != p[weishu-k-1]) {cout<<0;return 0;}
    }
    cout<<1;return 1;
}
*/
