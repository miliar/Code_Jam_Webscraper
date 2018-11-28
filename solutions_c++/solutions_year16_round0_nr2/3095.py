#include<stdio.h>
#include<iostream>
#include<set>
#include<algorithm>
#define mod(x) x%1000000007
#include<cstring>
#include<vector>
#include<math.h>
#include <stdlib.h>
using namespace std;

char findsymbol(int rot,char ch)
{
    if(ch=='+' && rot%2==0)
        return '+';
    else if(ch=='+' && rot%2!=0)
        return '-';
    else if(ch=='-' && rot%2!=0)
        return '+';
    else
        return '-';
}

int main(){
    int t;
    cin>>t;
    for(int tt=0;tt<t;tt++)
    {
        char st[100000];
        cin>>st;
        int minus = 0;
        int len=strlen(st);
        for(int i=0;i<len;i++)
        {
           if(st[i]=='-')
             minus = i;
        }
        int arr[len];
        memset(arr,0,sizeof(arr));
        long long int ans=0;
        int start=0,end=minus;
        while(start<end ||(start==end&&(st[start]=='-')))
        {
            int count = 0;
            while(findsymbol(arr[start],st[start])=='+'&&start<end)
            {
                count++;
                arr[start+1]=arr[start];
                start++;
            }
            if(count>0 && start<=end) ans++;
            count=0;
           // cout<<start<<" "<<end<<endl;
            while(findsymbol(arr[start],st[start])=='-' && start<=end)
            {
                count++;
                arr[start+1]=arr[start];
                start++;
            }
            if(count>0){ans++;arr[start]++;arr[end]++;}
            count=0;
            while(findsymbol(arr[end],st[end])=='+' && start<end)
            {
                count++;
                arr[end-1]=arr[end];
                end--;
            }
            if(count>0 && start<=end) ans++;
            count=0;
            while(findsymbol(arr[end],st[end])=='-' && start<=end)
            {
                count++;
                arr[end-1]=arr[end];
                end--;
            }
            if(count>0){ans++;arr[start]++;arr[end]++;}
        }
       cout<<"Case #"<<tt+1<<": "<<ans<<endl;
    }
    }

