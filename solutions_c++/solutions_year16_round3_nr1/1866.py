#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define pb(v,x) v.push_back(x)
#define REP(i,n) for(i=0;i<n;i++)
using namespace std;
struct node{
    int val;
    char c;
};
bool cmp(node x , node y){
    return x.val > y.val;
}
int safe1(node a[] , int n , int s)
{
    if(n==2){
        if(2*a[0].val<=s and 2*a[1].val<=s) return 1;
        return 0;
    }
    if(2*a[2].val<=s-2 and 2*a[0].val<=s and 2*a[1].val<=s) return 1;
    return 0;
}
int safe2(node a[] , int n , int s)
{
    if(2*a[0].val<=s+2 and 2*a[1].val<=s-2) return 1;
    return 0;
}
int main()
{
    FILE *fp1;FILE *fp2;
    fp1 = fopen("input.txt","r");
    fp2 = fopen("output.txt","w");
    int t;
    int n,i,j;
    fscanf(fp1,"%d",&t);
    for(int test=1;test<=t;test++)
    {
        fscanf(fp1,"%d",&n);
        node a[n];
        int s=0;
        REP(i,n) fscanf(fp1,"%d",&a[i].val) , s += a[i].val , a[i].c = 'A'+i;
        fprintf(fp2,"Case #%d: ",test);
        while(s>0)
        {
            sort(a,a+n,cmp);
            if(a[1].val==0){
                if(a[0].val==1) fprintf(fp2,"%c ",a[0].c);
                else fprintf(fp2,"%c%c ",a[0].c,a[0].c);
                break;
            }
            if(safe1(a,n,s)){
                fprintf(fp2,"%c%c ",a[0].c,a[1].c);
                a[0].val--;a[1].val--;s-=2;
            }
            else if(safe2(a,n,s)){
                fprintf(fp2,"%c%c ",a[0].c,a[0].c);
                a[0].val-=2;s-=2;
            }
            else{
                fprintf(fp2,"%c ",a[0].c);
                a[0].val--;s--;
            }
        }
        fprintf(fp2,"\n");
    }
    return 0;
}
