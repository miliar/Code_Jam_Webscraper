#pragma warning(disable:4996)
#include<stdio.h>
#include<string.h>
#include<algorithm>
#define INF 999999999
using namespace std;
char p[201][50];
int r1;
int mr(int n,int n1,char ch[1001])
{
    int st=0;
     int i=0,r=0;
//printf("\tif=%c\t",ch[n]);
    if(ch[n]!='0')
    {
    char cch[1001];
		for(i=0;i<n;i++)
        {
            cch[i]=ch[i];
        st=st+(cch[i]-'0');
        }
        cch[i]='\0';
        //st--;
       // i--;

        if(st<i)
        {r=i-st;
        }else r=0;

       // printf("\t||cch=%s- st=%d-- i=%d-- r=%d--||\t",cch,st,i,r);

        }
        if(r1<r)r1=r;
        if(n<n1){
                n++;
        mr(n,n1,ch);
        }

       // printf("r=%d, ch=%s  st=%d ,i=%d\n",r,ch,st,i);
       return r1;
}
bool o[201];
int main()
{
	freopen("input3.in", "r", stdin);
	freopen("output3.txt", "w", stdout);
	int i, TC,T,  nr,m;
	scanf("%d", &TC);
	for (T = 1; T <= TC; T++){
           r1=m=0;
		printf("Case #%d: ", T);
		scanf("%d", &nr);

		char ch[1001];

		scanf("%s",&ch);
//printf("\n nr=%d ,ch= %s  \n ", nr,ch);
     m=mr(0,nr,ch);


		printf("%d\n",m);
	}
}
