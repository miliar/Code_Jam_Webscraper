#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    freopen("Ainput.txt","r",stdin);
    freopen("Aoutput.txt","w",stdout);
    ll t,n,i,no=0,arr[109],l,j,k,cnt;
    string s;
    cin>>t;
    getchar();
    while(t--)
    {
        getline(cin,s);
        l=s.size();
        cnt=0;
        for(i=0; i<l; i++)
        {
            if(s[i]=='+')arr[i]=1;
            else arr[i]=0;
        }
        for(k=l-1; k>=0; k--)
        {
            if(arr[k]==0)
            {
                cnt++;
                for(j=k; j>=0; j--)
                {
                    if(arr[j]==1)
                        arr[j]=0;
                    else arr[j]=1;
                }
                //reverse(arr,arr+k+1);
                for(i=0;i<=k;i++)
                    swap(arr[i],arr[k-i]);
            }
//            for(i=0; i<l; i++)
//            {cout<<arr[i]<<"  ";
//            }
            //cout<<endl;
        }
        s.clear();
        cout<<"Case #"<<++no<<": "<<cnt<<endl;
    }
}
