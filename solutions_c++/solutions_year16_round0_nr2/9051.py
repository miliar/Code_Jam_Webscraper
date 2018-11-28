
/*
    Author:- Deepak Singh Mehta.

    Deciding what not to do is
    as important as deciding
    what to do.

*/


#include<bits/stdc++.h>
#define s(a) scanf("%d",&a)
#define pb push_back
#define p(a) pair<int,int>
#define mp make_pair
#define NAX 100000
#define MOD 1000000007
#define v(a) vector<int>
#define fastio ios::sync_with_stdio(false)
#define si(a) scanf("%d",&a)
#define ll long long
#define ff first
#define ss second

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
    s(t);
    for(int tt=0;tt<t;tt++)
    {
        char st[NAX];
        cin>>st;
        int min = 0;
        int len=strlen(st);
        for(int i=0;i<len;i++)
        {
           if(st[i]=='-')
             min = i;
        }
        int arr[len];
        fill(arr,arr+len,0);
        long long int ans=0;
        int first=0,last=min;
        while(first<last ||(first==last&&(st[first]=='-')))
        {
            int cnt = 0;
            while(findsymbol(arr[first],st[first])=='+'&&first<last)
            {
                cnt++;
                arr[first+1]=arr[first];
                first++;
            }
            if(cnt>0 && first<=last) ans++;
            cnt=0;
            while(findsymbol(arr[first],st[first])=='-' && first<=last)
            {
                cnt++;
                arr[first+1]=arr[first];
                first++;
            }
            if(cnt>0){ans++;arr[first]++;arr[last]++;}
            cnt=0;
            while(findsymbol(arr[last],st[last])=='+' && first<last)
            {
                cnt++;
                arr[last-1]=arr[last];
                last--;
            }
            if(cnt>0 && first<=last) ans++;
            cnt=0;
            while(findsymbol(arr[last],st[last])=='-' && first<=last)
            {
                cnt++;
                arr[last-1]=arr[last];
                last--;
            }
            if(cnt>0){ans++;arr[first]++;arr[last]++;}
        }
       cout<<"Case #"<<tt+1<<": "<<ans<<endl;
    }
    }
