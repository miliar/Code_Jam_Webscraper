#include <iostream>
#include <cstring>
#include <algorithm>

#define rfe(i,a,b) for(int i=a;i<b;i++)
#define MAXM 100100

using namespace std;

int t,n;
int A[MAXM],B[MAXM];
int bin_val;

void bin_search(int val,int st,int en)
{
    if(st>en){
        return;
    }
    int mid=st+(en-st)/2;
    if(B[mid]>=val){
        bin_val=mid;
        bin_search(val,mid+1,en);
    }
    else{
        bin_search(val,st,mid-1);
    }

}


int monkiness()
{
    int ans=0;
    rfe(i,0,n){
        bin_val=0;
        bin_search(A[i],i,n);
        ans=max(ans,bin_val-i);
    }
    return ans;
}



int main()
{
    ios::sync_with_stdio(false);
    cin>>t;
    while(t--){
        cin>>n;
        rfe(i,0,n)  cin>>A[i];
        rfe(i,0,n)  cin>>B[i];
        cout<<monkiness()<<endl;
    }


}
