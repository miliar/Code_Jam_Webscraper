#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
vector<float> a;
vector<float> b;
int main()
{
    int t;
	scanf("%d",&t);
	int n,i,j,cas=0,cn,cnt,top;
	while(t>0)
	{
		t-=1;cas+=1;
        scanf("%d",&n);
        a.resize(n);
        b.resize(n);
        for(i=0;i<n;i++)
            scanf("%f",&a[i]);
        for(i=0;i<n;i++)
            scanf("%f",&b[i]);
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        printf("Case #%d: ",cas);
        cnt=0;top=n-1;
        for(i=n-1;i>=0;i--)
        {
            if(a[i]>b[top])
            {
                cnt++;;
            }
            else
            {
                top-=1;
            }
        }
        //cout<<cnt<<endl;
        i=n-1;j=n-1;cn=0;
        while((i>=0)&&(j>=0))
        {
            if(a[i]>b[j])
            {
                i--;j--;cn++;
            }
            else
            {
                j--;
            }
        }
        cout<<cn<<" "<<cnt<<endl;
	}
    return 0;
}
