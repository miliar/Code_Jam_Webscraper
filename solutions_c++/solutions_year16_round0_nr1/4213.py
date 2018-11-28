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
        LL n;
        fscanf(in,"%lld",&n);
        //scanint(n);
        int flag=0;
        int present[11]={0};
        int counter=0;
        if(n==0)
            fprintf(out,"Case #%d: INSOMNIA\n",tt);
        else
        {
            LL temp=1,temp1,k,curr;
            while(1)
            {
                temp1=n*temp;
                curr=temp1;
                while(temp1)
                {
                    k=temp1%10;
                    if(!present[k])
                    {
                        present[k]=1;
                        counter++;
                    }
                    temp1/=10;
                    if(counter==10)
                    {
                        fprintf(out,"Case #%d: %lld\n",tt,curr);
                        flag=1;
                        break;
                    }
                }
                temp++;
                if(flag==1)
                    break;
            }
        }
    }
    return 0;
}

// Can a man still be brave if he's afraid?  That is the only time a man can be brave !!
