#include <iostream>
#include<string>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<fstream>
#include<vector>
using namespace std;

class node
{
    public:
    int val;
    int x;
    int y;
    node()
    {
        val=0;x=0;y=0;
    }
};
vector< node > arr(10010);
int inp[102][102];
vector<int> row_min(102),col_min(102);

bool func(node a, node b)
{
    return(a.val>b.val);
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output.out");
    int t,case_no,n,m,val,i,j;
    fin>>t;
    for(case_no=1;case_no<=t;case_no++)
    {
        fin>>n>>m;

        int p=0;
        for(i=0;i<n;i++)
        {
            row_min[i]=0;

        }
        for(j=0;j<m;j++)
        {
            col_min[j]=0;
        }
        for(i=0;i<n;i++)
        {
                for(j=0;j<m;j++)
                {
                    fin>>inp[i][j];
                    arr[p].val=inp[i][j];
                    arr[p].x=i;
                    arr[p].y=j;
                    p++;
                }
        }
//        for(i=0;i<n;i++)
//        {
//                for(j=0;j<m;j++)
//                {
//                    cout<<inp[i][j]<<"\t";
//                }
//                cout<<"\n";
//        }

    sort(arr.begin(),arr.begin()+p,func);
    //cout<<"\n\n\n";
//    for(i=0;i<p;i++)
//    {
//        cout<<arr[i].val<<"\t"<<arr[i].x<<"\t"<<arr[i].y<<"\n";
//    }
    int flag=1;
    for(i=0;i<p;i++)
    {
        if(arr[i].val<row_min[arr[i].x]&&arr[i].val<col_min[arr[i].y])
        {
            flag=0;
            break;
        }
         if(row_min[arr[i].x]<=arr[i].val)
        row_min[arr[i].x]=arr[i].val;
        if(col_min[arr[i].y]<=arr[i].val)
        col_min[arr[i].y]=arr[i].val;
    }
    if(flag==1)
    {
        fout<<"Case #"<<case_no<<":"<<" YES\n";
    }
    else
    {
        fout<<"Case #"<<case_no<<":"<<" NO\n";
    }

    }
    return(0);
}
