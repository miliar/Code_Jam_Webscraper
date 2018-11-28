/****************************************************************
*    sonu kumar
*    MNNIT allahabad
*    computer science and engineering
****************************************************************/
#include<bits/stdc++.h>
#define ll long long int 
#define mod 1000000007
#define pb(i) push_back(i) 
#define mp(i,j) make_pair(i,j)
#define line printf("\n")
#define space printf(" ")
#define sci(i) scanf("%d",&i)
#define scl(i) scanf("%lld",&i)
#define chk(a) cerr << endl << #a << " : " << a << endl
#define chk2(a,b) cerr << endl << #a << " : " << a << "\t" << #b << " : " << b << endl
using namespace std;
char arr[50000];
int main()
{
    int t;
    scanf("%d",&t);
    cin.ignore();
    for(int sonu=1;sonu<=t;sonu++)
    {
        char str[20000];
        scanf("%s",str);
        int len=strlen(str);
        int l,r;
        l=2000,r=2001;
        arr[l]=str[0];
        printf("Case #%d: ",sonu);
        for(int i=1;i<len;i++)
        {
            int a=str[i];
            int b=arr[l];
            if(a>=b)
            l--,arr[l]=str[i];
            else 
            arr[r]=str[i],r++;
        }
        for(int i=l;i<r;i++)
        printf("%c",arr[i]);
        printf("\n");
    }
    return 0;
}