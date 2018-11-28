#include <iostream>
#include <cstdio>
#define REP(i,a) for(int i=0;i<a;i++)

using namespace std;

int maxArr(int A[],int N,int& maxI)
{
    int maxV=-1;
    maxI=-1;
    REP(i,N){
       // cout<<A[i]<<' ';
        if(maxV<A[i]){
            maxV=A[i];
            maxI=i;
        }
    }
    //cout<<endl;
    return maxV;

}
int minArr(int A[],int N,int& maxI)
{
    int maxV=10000;
    maxI=-1;
    REP(i,N){
        if(maxV>A[i] && A[i]!=0){
            maxV=A[i];
            maxI=i;
        }
    }
    return maxV;
}


int recurAns(int A[],int N,int st)
{
    if(st>9)
        return 100000;
    int maxV,maxI,minV,minI,tmp;
    //REP(i,N)    cout<<A[i]<<' ';
   // cout<<endl;
    maxV=maxArr(A,N,maxI);
    minV=minArr(A,N,minI);
    if(maxV==1)
        return 1;
    int A1[N+1],A2[N+1],A3[N];
    REP(i,N){    A1[i]=A[i]; A2[i]=max(0,A[i]-1);A3[i]=A[i]; }
    A1[maxI]=maxV/2 + maxV%2;
    A1[N]=maxV-A1[maxI];
    tmp=A3[maxI];
    A3[maxI]=tmp/3 + tmp%3;
    A3[N]=tmp-A3[maxI];
   // A3[minI]=tmp-A3[maxI];
    /*if(recurAns(A2,N,st+1)<recurAns(A1,N+1,st+1)){
        if(recurAns(A3,N,st+1)<recurAns(A2,N,st+1))
            cout<<"A3"<<endl;
        else
            cout<<"A2"<<endl;
    }*/
    //else
   //     cout<<"A1"<<endl;
    return 1+min(min(recurAns(A2,N,st+1),recurAns(A1,N+1,st+1)),recurAns(A3,N+1,st+1));
}

int main()
{
   freopen("f2.in","r",stdin);
    freopen("o2.txt","w",stdout);
    int T;
    cin>>T;
    REP(t,T){
        int N;
        cin>>N;
        int A[N];
        REP(i,N)    cin>>A[i];

        cout<<"Case #"<<t+1<<": "<<recurAns(A,N,0)<<endl;
    }
}

