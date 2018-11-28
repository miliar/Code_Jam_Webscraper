#include<iostream>
#include<stdio.h>
#include<string.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<set>
#include<math.h>
#include<map>
using namespace std;

#define mp make_pair
#define pb push_back

int arr[10],idx;

bool isPrime(long long x) {
    for(long long i=2;i*i<=x;i++) {
        if(x%i==0) {
            arr[idx]=i;
            return false;
        }
    }
    return true;
}

bool check(int x) {
    //cout<<x<<"\n";
    for(int div=2;div<=10;div++) {
        idx=div-1;
        long long temp=x,p=1,num=0;
        while(temp!=0) {
            num=num+p*(temp%2);
            temp=temp/2;
            p=p*div;
        }
        //cout<<div<<","<<num<<"\n";
        if(isPrime(num))
            return false;
    }
    return true;
}

string createString(long long x) {
    int len=0;
    long long temp=x;
    string ret="";
    while(temp!=0) {
        if(temp%2==0)
            ret="0"+ret;
        else
            ret="1"+ret;
        temp=temp/2;
        len++;
    }
    len=len*2;
    string tmp = "";
    for(int i=0;i<32-len;i++)
        tmp=tmp+"0";
    return (ret+tmp+ret);
}

int main()
{
    freopen ("C-small-attempt0.in","r",stdin);
    freopen ("op3-2.out","w",stdout);
    long long i=2;
    int cnt=0;
    cout<<"Case #1:\n";
    while(cnt<500) {
        if(i%2)
        {
            if(check(i)) {
                //cout<<i<<"\n";
                cout<<createString(i)<<" ";
                for(int j=1;j<10;j++) {
                    cout<<arr[j]<<" ";
                }
                cnt++;
                cout<<"\n";
            }
        }
        i++;
    }
}
