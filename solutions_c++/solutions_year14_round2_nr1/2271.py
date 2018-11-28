#include <bits/stdc++.h>
using namespace std;

#define sc(a) scanf("%d",&a)
#define scm(a,b) scanf("%d%d",&a,&b)
#define fl(c,i,n) for(i=c;i<n;i++)
#define f(i,n) for(i=0;i<n;i++)
#define mem(a,val) memset(a,val,sizeof(a))
#define ll long long int
#define ull unsigned long long int
#define inf INT_MAX
#define linf LONG_LONG_MAX
#define pb push_back
#define pp pop_back()
#define aov(a) a.begin(),a.end()
#define mp make_pair
#define nl printf("\n")
#define PI 2.0*acos(0.0) //#define PI acos(-1.0)
#define xx first
#define yy second

#define mxv(a) *max_element(aov(a))
#define mnv(a) *min_element(aov(a))

#define LB(a,x) (lower_bound(aov(a),x)-a.begin())
#define UB(a,x) (upper_bound(aov(a),x)-a.begin())

#define to_c_string(a) a.c_str()
#define strtoint(c) atoi(&c[0])

#define M 10000

#define COUT(x) #x

string a[109];
char c[109],q;
int p[109][109];

int main ()
{
    FILE  *fo;
    fo=fopen("out.txt","w");

    int t,i,n,k,j,l,it,s,cs=1;
    sc(t);
    while(t--)
    {
        sc(n);
        f(i,n)
        {
            cin>>a[i];
        }
        fprintf(fo,"Case #%d: ",cs++);
        l=a[0].size();
        q='.';
        j=0;
        f(k,l)
        {
            if(a[0][k]!=q)
            {
                q=a[0][k];
                c[j++]=q;
            }
        }

        mem(p,0);
        f(i,n)
        {
            k=0;
            f(it,j)
            {
                if(c[it]==a[i][k])
                {
                    while(k<a[i].size()&&c[it]==a[i][k]){
                        p[i][it]++;
                        k++;
                    }
                }
                else
                    break;
            }
            if(it<j||k<a[i].size())break;
        }
        if(i<n)
            fprintf(fo,"Fegla Won\n");
        else
        {
            s=0;
            f(it,j)
            {
                l=0;
                f(i,n)
                {
                    l+=p[i][it];
                }
                l/=n;

                f(i,n)
                {
                    s+=abs(p[i][it]-l);
                }
                //cout<<c[it]<<" "<<s<<endl;
            }
            fprintf(fo,"%d\n",s);
        }
    }


    return 0;
}

