#include<bits/stdc++.h>
#include<cmath>
#define M_PI  3.14159265358979323846
using namespace std;
void check(int a[],vector<int> &v,int &j)
{
    if(a[25]>0&&a[4]>0&&a[17]>0&&a[14]>0)
    {
        v.push_back(0);
        j+=4;
        a[25]--;
        a[4]--;
        a[17]--;
        a[14]--;
    }
    if(a[14]>0&&a[13]>0&&a[4]>0)
    {
        v.push_back(1);
        j+=3;
        a[14]--;
        a[13]--;
        a[4]--;
    }
    
    if(a[14]>0&&a[22]>0&&a[19]>0)
    {
        v.push_back(2);
        j+=3;
        a[14]--;
        a[22]--;
        a[19]--;
    }
    if(a[19]>0&&a[7]>0&&a[17]>0&&a[4]>1)
    {
        v.push_back(3);
        j+=5;
        a[4]-=2;
        a[17]--;
        a[19]--;
        a[7]--;
    }
    if(a[14]>0&&a[20]>0&&a[5]>0&&a[17]>0)
    {
        v.push_back(4);
        j+=4;
        a[14]--;
        a[17]--;
        a[5]--;
        a[20]--;
    }
    if(a[5]>0&&a[8]>0&&a[21]>0&&a[4]>0)
    {
        v.push_back(5);
        j+=4;
        a[4]--;
        a[8]--;
        a[21]--;
        a[5]--;
    }
    if(a[18]>0&&a[8]>0&&a[23]>0)
    {
        v.push_back(6);
        j+=3;
        a[18]--;
        a[8]--;
        a[23]--;
    }
    if(a[18]>0&&a[4]>1&&a[21]>0&&a[13]>0)
    {
        v.push_back(7);
        j+=5;
        a[4]-=2;
        a[18]--;
        a[21]--;
        a[13]--;
    }
    if(a[7]>0&&a[6]>0&&a[4]>0&&a[19]>0&&a[8]>0)
    {
        v.push_back(8);
        j+=5;
        a[7]--;
        a[6]--;
        a[4]--;
        a[19]--;
        a[8]--;
    }
    if(a[4]>0&&a[8]>0&&a[13]>1)
    {
        v.push_back(9);
        j+=4;
        a[13]-=2;
        a[8]--;
        a[4]--;
    }    
}
int main()
{
    ios_base::sync_with_stdio(false);
    int t,tt;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
       int a,b=0,c;
        int arr[26]={0};
        vector<int> v;
        string i,j="",k;
        cin>>i;
        for(a=0;a<i.size();a++)
            arr[i[a]-'A']++;
        while(1)
        {
              check(arr,v,b);
               if(b>=i.size())
                break;
        }
        sort(v.begin(),v.end());
        cout<<"Case #"<<tt<<": ";
        for(b=0;b<v.size();b++)
            cout<<v[b];
        cout<<"\n";
    }
    return 0;
}
