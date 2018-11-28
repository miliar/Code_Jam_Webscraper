/***********************

Shubham Singhal

CodeChef - torque
HackerEarth - torque
SPOJ - torque
HackerRank - torquecode
CodeForces - torquecode
***********************/

// If Tyrion dies, I am gonna riot :P


# include <bits/stdc++.h>
using namespace std;

# define gc          getchar
# define LL          long long
# define L           long
# define pb          push_back
# define pINF        999999
# define nINF        -999999
# define printi(x)   printf("%d",&x);
# define printli(x)  printf("%ld",&x);
# define printlli(x) printf("%lld",&x);
# define mp          make_pair
# define vi          vector<int>
# define MAXN        150005

template<class T>
void scanint(T &x)
{
    register T c = gc();
    x = 0;
    T neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

int main()
{
    FILE *in,*out;
    in=fopen("input.in","rt");
    out=fopen("output.txt","wt");
    int t;
    fscanf(in,"%d",&t);
    //scanint(t);
    for(int tt=1;tt<=t;tt++)
    {
        char s[105];
        fscanf(in,"%s",&s);
        //scanint(n);
        int len=strlen(s),ans=0;
        for(int i=len-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                ans++;
                s[i]='+';
                int j;
                for(j=i-1;j>=1;j--)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        break;
                }
                i=j+1;
                for(int k=i-1;k>=0;k--)
                {
                    if(s[k]=='+')
                        s[k]='-';
                    else
                        s[k]='+';
                }
            }
        }
        fprintf(out,"Case #%d: %d\n",tt,ans);
    }
    return 0;
}

// Can a man still be brave if he's afraid?  That is the only time a man can be brave !!
