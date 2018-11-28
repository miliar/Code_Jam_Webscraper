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
# define MAXN        66000

LL power[11][17];
LL arr[20];
FILE *in,*out;
int counter=0;
void calculate_power()
{
    for(int i=2;i<=10;i++)
        power[i][0]=1;
    for(LL i=2;i<=10;i++)
    {
        for(int j=1;j<=16;j++)
            power[i][j]=power[i][j-1]*i;
    }
}
LL calculate_divisor(LL ans)
{
    LL i;
    for(i=2;i*i<=ans;i++)
    {
        if(ans%i==0)
            return i;
    }
    return -1;
}
void calculate_bases(int len)
{
    vector<LL> seq;
    int flag=0;
    for(int i=2;i<=10;i++)
    {
        LL ans=0;
        for(int j=len-1;j>=0;j--)
        {
            ans+=(power[i][len-1-j]*arr[len-1-j]);
        }
        LL temp=calculate_divisor(ans);
        if(temp==-1)
        {
            flag=1;
            break;
        }
        else
        {
            seq.pb(temp);
        }
    }
    if(flag==0)
    {
        counter++;
        for(int i=len-1;i>=0;i--)
            fprintf(out,"%lld",arr[i]);
        for(int i=0;i<9;i++)
            fprintf(out," %lld",seq[i]);
        fprintf(out,"\n");
    }
}
void calculate_binary(LL n)
{
    int i=0;
    while(n)
    {
        arr[i++]=n%2;
        n/=2;
    }
    if(arr[0]==0)
        return;
    calculate_bases(i);

}
int main()
{

    in=fopen("input.in","rt");
    out=fopen("output.txt","wt");
    int t,a,b;
    fscanf(in,"%d%d%d",&t,&a,&b);
    //scanint(t);
    calculate_power();
    fprintf(out,"Case #1:\n");
    for(LL i=32769;i<=65535;i++)
    {
        calculate_binary(i);
        if(counter==50)
            break;
    }
    return 0;
}

// Can a man still be brave if he's afraid?  That is the only time a man can be brave !!
