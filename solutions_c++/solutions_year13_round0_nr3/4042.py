#include<stdio.h>
#include<iostream>
#include<vector>
using namespace std;
long long q[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
bool pali(long long v)
{
    long long r=0,cv=v;
    do
    {
        r=r*10+cv%10;
        cv/=10;
    }while(cv);
    return r==v;
}
int main()
{
    //ofstream cout("f.out");
    //ifstream cin("f.in");
    long long A,B;int T,t=0;
    fprintf(stderr,"%d\n",sizeof(q)/sizeof(long long));
    for(cin>>T;T;T--)
    {
        cin>>A>>B;
        int nr=0;
        for(int i=0;i<39;i++)
            if(A<=q[i] && q[i]<=B)
                nr++;
        cout<<"Case #"<<++t<<": "<<nr<<endl;
    }
    return 0;
}
