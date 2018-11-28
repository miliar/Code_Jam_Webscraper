#include <iostream>
using namespace std;
#include <stdio.h>
#include <vector>
#include <algorithm>
int find1(vector <double> A,vector <double> B)
{
    int ans = 0;
    int left = 0,right = B.size()-1;
    for(int i=0;i<A.size();i++)
    {
        if(A[i]<B[left]) right--;
        else if(A[i]>B[right]) { right--; ans++; }
        else { left++; ans++; }
    }
    return ans;
}

int find2(vector <double> A,vector <double> B)
{
    int ans = 0;
    vector <bool> used;
    used.resize(B.size(),false);
    for(int i=0;i<A.size();i++)
    {
        for(int j=0;j<B.size();j++)
        {
            if(B[j]>A[i]&&used[j]==false)
            {
                ans++;
                used[j] = true;
                break;
            }
        }
    }
    return A.size()-ans;
}

int main()
{
    int T,M;
    vector <double> A,B;
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    cin>>T;
    for(int cnt = 1;cnt<=T;cnt++)
    {
        A.clear();
        B.clear();
        cin>>M;
        double m;
        for(int i=0;i<M;i++) { cin>>m; A.push_back(m); }
        for(int i=0;i<M;i++) { cin>>m; B.push_back(m); }
        sort(A.begin(),A.end());
        sort(B.begin(),B.end());
        printf("Case #%d: ",cnt);
        printf("%d ",find1(A,B));
        printf("%d\n",find2(A,B));
    }
    return 0;
}
