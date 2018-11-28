#include<stdio.h>

using namespace std;

int arr[1001];

int main()
{
    freopen("cin.in","r",stdin);

    freopen("cout.in","w",stdout);

    for(int i=1;i<1001;i++) arr[i]++;

    for(int i=4;i<1001;i++) arr[i]++;
    for(int i=9;i<1001;i++) arr[i]++;
    for(int i=121;i<1001;i++) arr[i]++;
    for(int i=484;i<1001;i++) arr[i]++;

    int T;
    scanf(" %d",&T);

    for(int tt=1;tt<=T;tt++)
    {
        int a,b;
        scanf(" %d %d",&a,&b);

        printf("Case #%d: %d\n",tt,arr[b]-arr[a-1]);
    }

    return 0;
}
