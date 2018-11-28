#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

#define s(n) scanf("%d",&n)
#define p(n) printf("%d",n)
#define ll long long
#define ld long double
#define D (double)
#define LD (long double)
int num(int a,int* arr,int s,int e)
{
    //cout<<"num "<<a<<" "<<s<<" "<<e<<endl;
    if(e<s)return 0;
    if(arr[s]<a)return num(a+arr[s],arr,s+1,e);
    if(a==1)return 1+num(a,arr,s,e-1);
    return min(1+num(a+a-1,arr,s,e),1+num(a,arr,s,e-1));
}

int main()
{
	freopen("ip.in","r",stdin);
	freopen("op.in","w",stdout);
	int t,c=0;cin>>t;
	while(t--)
	{
		c++;
        int a;
        cin>>a;
        int  n;
        cin>>n;int arr[n];
        for(int i=0;i<n;i++)cin>>arr[i];
        //cout<<"aman";
        sort(arr,arr+n);
        printf("Case #%d: ",c);
        cout<<num(a,arr,0,n-1)<<endl;



	}
}
