#include<bits/stdc++.h>
using namespace std;

// Input macros
#define s(n)                        scanf("%d",&n)
#define sl(n)                       scanf("%ld",&n)
#define sll(n)                      scanf("%lld",&n)
#define sllu(n)                     scanf("%llu",&n)
#define p(n)						printf("%d\n",n)
#define pl(n)						printf("%ld\n",n)
#define pll(n)						printf("%lld\n",n)
#define pllu(n)						printf("%llu\n",n)

typedef long long int ll;

FILE *fin=freopen("A-large.in","r",stdin);
FILE *fout=freopen("a_large.txt","w",stdout);
/*
int maj(vector<int> &a)
{
    int sum;
    for(int x=0;x<a.size();x++)sum+=a[x];
    for(int x=0;x<a.size();x++)
    {
        if((double)a[x]/(double)sum >= (double)sum/2.0)
            return 0;
    }
    return 1;
}
*/
int main()
{
    int t;s(t);
    for(int i=1;i<=t;i++)
    {
        int n;s(n);
        int a[n];
        for(int x=0;x<n;x++)s(a[x]);
        int sum=0;
        for(int x=0;x<n;x++)sum+=a[x];
        char ch;
        if(n==2)
        {
            cout<<"Case "<<"#"<<i<<": ";
            while(a[0]--)
            {
                //cout<<"Case "<<"#"<<i<<": AB ";
                cout<<"AB ";
                /////////////////////

            }
            printf("\n");
            continue;
        }
         cout<<"Case "<<"#"<<i<<": ";
            while(sum>2)
            {
                int *m = max_element(a,a+n);
                int pos=distance(a,max_element(a,a+n));
                //cout<<"!!!!!!!!!!"<< *m<<endl;
                    if(sum>2)
                    {
                        a[pos]--;
                        //cout<<"@@@@@@@@@"<<a[pos]<<"######"<<endl;
                        ch = pos+65;
                       cout<<ch<<" ";
                        //cout<<"%%%%%%%%%"<<ch<<endl;
                    }

            sum--;
            }
            if(sum<=2)
                {
                    vector<int> v;
                    for(int x=0;x<n;x++)
                        if(a[x]==1)
                            v.push_back(x);

                    for(int x=0;x<v.size();x++)
                    {
                        ch=v[x]+65;

                        cout<<ch;
                    }
                    cout<<"\n";
                }




        //printf("Case #%d: %@\n",i,@);
    }
}
