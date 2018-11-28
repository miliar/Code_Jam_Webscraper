#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int j=0; j<t; j++)
    {
        int Smax;
        scanf("%d",&Smax);
        int count=Smax+1;
        int initial=0;
        int minReq=0;
        char dummy;
        //cin>>dummy;
        string a;
        cin>>a;
        //cout<<a<<endl;
        for(int i=0; i<count; i++)
        {
            char ch;
            //scanf("%c",&ch);
            //cin>>ch;
            ch=a[i];
            //printf("%c\n",ch);
            int num=ch-48;
            if(i==0)
            {
                initial=num;
                continue;
            }
            else if(num==0)
                continue;
            else
            {
                if(initial>=i) // guy will clap
                    initial+=num;
                else
                {
                    minReq+=i-initial;
                    initial=i;
                    initial+=num;
                }
            }
        }
        printf("Case #%d: %d\n",j+1,minReq);
    }
    return 0;
}
