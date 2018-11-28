//Author: Tusshar Singh
#include<cstdlib>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<deque>
#include<algorithm>

using namespace std;

#define mod 1000000007
#define inf 2147483647
#define ninf -2147483648
#define FOR(i,a,b) for(i=a;i<b;i++)
#define s(a) fscanf(fp,"%d",&a)
#define lls(a) fscanf(fp,"%lld",&a)
#define ss(a) fscanf(fp,"%s",a)
#define p(a) printf("%d",a)
#define llp(a) printf("%lld",a)
#define sp(a) printf("%s",a)
#define cp(a) printf("%c",a)
#define nline printf("\n")
#define space printf(" ")
#define ll long long
int arr[1000001];
int main()
{
    int i,j,k,t,x;
    FILE *fp,*fw;
        //cout<<"here";

    fp=fopen("ALC.in","r");
    fw=fopen("output.txt","w");
    s(t);
    //cout<<t<<endl;
    FOR(x,1,t+1)
    {
        int fin;
        vector<int> sol;
        int mote,n;
        s(mote);
        //cout<<mote<<endl;
        s(n);
        //cout<<n<<endl;
        FOR(i,0,n)
        {
            s(arr[i]);
            //cout<<arr[i]<<" ";
        }
        //cout<<endl;
        sort(arr,arr+n);
        int ans=0;
        FOR(i,0,n)
        {
            if(arr[i]<mote)
            {
                mote+=arr[i];
                continue;
            }
            else if((2*mote-1)>arr[i])
            {
                ans+=1;
                mote=2*mote-1;
                mote+=arr[i];
                continue;
            }
            else if((2*mote-1)<=arr[i])
            {
                int temp=n-i;
                sol.push_back(ans+temp);
                //cout<<"pushing ";
                //cout<<ans+temp<<endl;
                if(mote==1)
                break;
                while(arr[i]>=mote)
                {
                    mote=2*mote-1;
                    ans++;
                }
                mote+=arr[i];
            }
        }
                if(i==n)
                {
                    sol.push_back(ans);
                    //cout<<"pushing back "<<ans<<endl;
                }


        fin=*std::min_element(sol.begin(),sol.end());
        fprintf(fw,"Case #%d: %d\n",x,fin);
    }
    return 0;
}
