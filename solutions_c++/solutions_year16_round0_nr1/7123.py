#include<iostream>
#include<cstdio>
#include<climits>
#define gc getchar_unlocked
using namespace std;
void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
bool isGotAll(int arr[])
{
    for(int i=0;i<10;i++)
        if(arr[i]==0)
            return true;
    return false;
}
int main()
{  

    int T,N,i=1;
    scanint(T);
    while(T--)
    {
        int num[10];
        for(int j=0;j<10;j++)
            num[j]=0;
        int N;
        scanint(N);
        int mul=2;
        int M=N;
        while(isGotAll(num))
        {
            int n=N;
            while(n>0)
            {
                num[n%10]=1;
                n=n/10;
            }
            if(isGotAll(num))
                N=M*mul;
            //cout<<N<<"\n";
            mul++;
            if(mul>2 && N==M)
                break;
        }
        if(N==M)
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        else
            cout<<"Case #"<<i<<": "<<N<<endl;
        i++;
        for(int j=0;j<10;j++)
            num[j]=0;
     
    }   
    return 0;            
}