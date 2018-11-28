#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int main()
{
	int Test,k=1;
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	scanf("%d",&Test);
	while(Test--)
	{
        int Smax,i,cnt=0,total=0;
        string str;
        scanf("%d",&Smax);
        cin>>str;
        if(str[0]=='0')
        {
            cnt++;
            total++;
        }
        else
            total=str[0]-48;
        for(i=1;i<=Smax;i++)
        {
            //cout<<cnt<<endl;
            if(i<=total)
            {
                if(str[i]=='0'&&i==total )
                {
                    cnt++;
                    total++;
                }
                else
                    total+=str[i]-48;
            }
            else
            {
                cnt++;
                total+=1;
            }
           // printf("i = %d total = %d cnt = %d\n",i,total,cnt);
        }
        printf("Case #%d: %d\n",k,cnt);
        k++;
	}
	return 0;
}
