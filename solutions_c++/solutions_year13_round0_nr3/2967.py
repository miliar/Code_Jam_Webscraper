#include<iostream>
#include<string>
#include<cstdio>
#include<algorithm>
using namespace std;
int a[1001];

int main()
{

   //freopen("in.txt","r",stdin);
	//freopen("out4.txt","w",stdout);
    int time=1;
    a[1]=a[4]=a[9]=a[121]=a[484]=1;
    int t,x,y,sum;
    cin>>t;
    while(t--)
    {
        sum=0;
        cin>>x>>y;
        for(int i=x;i<=y;i++)
        {
            if(a[i])sum++;
        }
        printf("Case #%d: %d\n",time++,sum);
    }
	return 0;
}
