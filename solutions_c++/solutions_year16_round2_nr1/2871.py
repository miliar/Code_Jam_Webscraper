#include<bits/stdc++.h>

using namespace std;

#define std::cout cout;
#define std::cin cin;

int main()
{
	int i,j,t,cases;
	int a[26],b[10],length;
	char c[3000];
	freopen("problem1 large.in","r",stdin);
    freopen("problem1 large.out","w",stdout);
    scanf("%d",&cases);
    for(t=1;t<=cases;t++)
    {
    cin>>c;
    length=strlen(c);
    for(i=0;i<26;i++)
    {
        a[i]=0;
    }
    for(i=0;i<10;i++)
    {
        b[i]=0;
    }
    for(i=0;i<length;i++)
    {
        a[c[i]-'A']++;
    }
    printf("Case #%d: ",t);
    while(a[5]>=1 && a[14]>=1 && a[20]>=1 && a[17]>=1)
    {
        b[4]++;
        a[5]--;
        a[14]--;
        a[20]--;
        a[17]--;
    }
    while(a[5]>=1 && a[8]>=1 && a[21]>=1 && a[4]>=1)
    {
        b[5]++;
        a[5]--;
        a[8]--;
        a[21]--;
        a[4]--;
    }
    while(a[18]>=1 && a[8]>=1 && a[23]>=1)
    {
        b[6]++;
        a[18]--;
        a[8]--;
        a[23]--;
    }
    while(a[18]>=1 && a[4]>=2 && a[21]>=1 && a[13]>=1)
    {
        b[7]++;
        a[18]--;
        a[4]=a[4]-2;
        a[21]--;
        a[13]--;
    }
    while(a[4]>=1 && a[8]>=1 && a[6]>=1 && a[7]>=1 && a[19]>=1)
    {
        b[8]++;
        a[4]--;
        a[8]--;
        a[6]--;
        a[7]--;
        a[19]--;
    }
    while(a[13]>=2 && a[8]>=1 && a[4]>=1)
    {
        b[9]++;
        a[13]=a[13]-2;
        a[8]--;
        a[4]--;
    }
    while(a[25]>=1 && a[4]>=1 && a[17]>=1 && a[14]>=1)
    {
        b[0]++;
        a[25]--;
        a[4]--;
        a[17]--;
        a[14]--;
    }
    while(a[19]>=1 && a[22]>=1 && a[14]>=1)
    {
        b[2]++;
        a[19]--;
        a[22]--;
        a[14]--;
    }
    while(a[19]>=1 && a[7]>=1 && a[17]>=1 && a[4]>=2)
    {
        b[3]++;
        a[19]--;
        a[7]--;
        a[17]--;
        a[4]=a[4]-2;
    }
    while(a[14]>=1 && a[13]>=1 && a[4]>=1)
    {
        b[1]++;
        a[14]--;
        a[13]--;
        a[4]--;
    }
    for(i=0;i<10;i++)
    {
        while(b[i]!=0)
        {
            printf("%d",i);
            b[i]--;
        }
    }
    printf("\n");
    }
	return 0;
}
