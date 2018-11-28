#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<string>
#include<set>
#include<map>
using namespace std;

int main()
{
    freopen("C:\\Users\\vivek\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\vivek\\Desktop\\out.txt","w",stdout);
    /* 0-40 */
    long long int ar[]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000001,};
    long long int A,B,roota,rootb;
    int i,T,t,index1=-1,index2=-1;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        cin>>A>>B;
        roota=(long long int)ceil(sqrt(A));
        rootb=(long long int)floor(sqrt(B));
        for(i=0;i<40;i++)
          if(ar[i]>=roota) {index1=i; break;}
        
        for(i=39;i>=0;i--)
          if(ar[i]<=rootb) {index2=i; break;}
        
        if(index1>index2) cout<<"0"<<endl;
        else cout<<index2-index1 +1<<endl;
        index1=-1; index2=-1;
    }
    return 0;
}
