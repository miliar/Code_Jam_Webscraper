#include <bits/stdc++.h>
using namespace std;
map<vector<int> , int> mem;
int fin(std::vector<int> A)
{
    //sort(A.rbegin(), A.rend());
    if(mem[A])
        return mem[A];
    int i,j,k;
    for(i=9;i>=0;i--)
        if(A[i])
            break;
    k=i;
    if(k<=3)
        return k;
//    cout<<"1."<<i<<endl;
    for(j=1;j<=i/2;j++)
    {
        A[i-j]++;
        A[j]++;
        A[i]--;
        k=min(k,fin(A)+1);
        A[i-j]--;
        A[j]--;
        A[i]++;
    }
    return mem[A]=k;
}
int main()
{
   /* #ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    #endif
    */int t,i,j,k,l;
    cin>>t;
    for(i=0;i<t;i++){
        cin>>j;
        vector<int> A(10,0);
        for(k=0;k<j;k++)
        {
            cin>>l;
            A[l]++;
        }
        cout<<"Case #"<<i+1<<": "<<fin(A)<<endl;
    }
    return 0;
}