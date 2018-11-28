#include <iostream>
#include <iomanip>
#include <cstdio>
#include <queue>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;

#define all(x) (x).begin(),(x).end()
#define min(x,y) (x)<(y)?(x):(y)
#define max(x,y) (x)>(y)?(x):(y)

const int Base=1000000000;
const int Capacity=100;
typedef long long huge;
struct BigInt{
    int Len;
    int Data[Capacity];
    BigInt():Len(0){}
    BigInt(const BigInt &V):Len(V.Len){memcpy(Data,V.Data,Len*sizeof*Data);}
    BigInt(int V):Len(0){for(;V>0;V/=Base) Data[Len++]=V%Base;}
    BigInt &operator=(const BigInt &V){Len=V.Len;memcpy(Data,V.Data,Len*sizeof*Data);return *this;}
    int &operator[](int Index){return Data[Index];}
    int operator[](int Index)const{return Data[Index];}
};
int compare(const BigInt &A,const BigInt &B){
    if(A.Len!=B.Len) return A.Len>B.Len ? true:false;
    int i;
    for(i=A.Len-1;i>=0 && A[i]==B[i];i--);
    if(i<0)return 0;
    return A[i]>B[i] ? true:false;
}
BigInt operator+(const BigInt &A,const BigInt &B){
    int i,Carry(0);
    BigInt R;
    for(i=0;i<A.Len||i<B.Len||Carry>0;i++){
        if(i<A.Len) Carry+=A[i];
        if(i<B.Len) Carry+=B[i];;
        R[i]=Carry%Base;
        Carry/=Base;
    }
    R.Len=i;
    return R;
}
BigInt operator-(const BigInt &A,const BigInt &B){
    int i,Carry(0);
    BigInt R;
    R.Len=A.Len;
    for(i=0;i<R.Len;i++){
        R[i]=A[i]-Carry;
        if(i<B.Len) R[i]-=B[i];
        if(R[i]<0) Carry=1,R[i]+=Base;
        else Carry=0;
    }
    while(R.Len>0&&R[R.Len-1]==0) R.Len--;
    return R;
}
BigInt operator*(const BigInt &A,const int &B){
    int i;
    huge Carry(0);
    BigInt R;
    for(i=0;i<A.Len||Carry>0;i++){
        if(i<A.Len) Carry+=huge(A[i])*B;
        R[i]=Carry%Base;
        Carry/=Base;
    }
    R.Len=i;
    return R;
}
BigInt operator*(const BigInt &A, const BigInt &B)
{
       int i, j;
       huge Carry(0);
       BigInt R;
       for (i=0; i<A.Len+B.Len; i++) R[i]=0;
       for (i=0; i<B.Len; i++)
           for (j=0; j<A.Len; j++)
           {
               Carry=huge(A[j])*huge(B[i]);
               R[j+i+1]+=(R[j+i]+Carry)/Base;
               R[j+i]=(R[j+i]+Carry)%Base;
           }
       R.Len=A.Len+B.Len;
       while (R[R.Len-1]==0) R.Len--;
       while (R[R.Len-1]>=Base)
       {
             R[R.Len]=R[R.Len-1]/Base;
             R[R.Len-1]%=Base;
             R.Len++;
       }
       return R;
}
istream &operator>>(istream &In,BigInt &V){
    char Ch;
    for(V=0;In>>Ch;){
        V=V*10+(Ch-'0');
        if(In.peek()<=' ') break;
    }
    return In;
}
ostream &operator<<(ostream &Out,const BigInt &V){
    int i;
    Out<<(V.Len==0 ? 0:V[V.Len-1]);
    for(i=V.Len-2;i>=0;i--) for(int j=Base/10;j>0;j/=10) Out<<V[i]/j%10;
    return Out;
}

int cas;
BigInt r;
BigInt t;

int main()
{

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>cas;
    for (int l=1; l<=cas; l++)
    {
        cin>>r>>t;
        int count;
        BigInt zero, one;
        zero.Len = 1; zero.Data[0] = 0;
        one.Len = 1; one.Data[0] = 1;
        BigInt rwhite=zero;
        BigInt rblack=r-one;
        BigInt tremain = t;
        BigInt temp;
        count = 0;
        while (true)
        {
            rwhite = rblack + one;
            rblack = rwhite + one;
            temp = rblack*rblack-rwhite*rwhite;
            if (compare(temp, tremain))
                break;
            else
            {
                tremain = tremain - temp;
                count++;
            }
        }
        cout<<"Case #"<<l<<": "<<count<<endl;
    }
	return 0;
}