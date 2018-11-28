#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int hash[17];

int main()
{
    int t,kase,num,i,j,tmp,cnt;
    cnt;
    scanf("%d",&t);
    for(kase=1;kase<=t;kase++)
    {
        memset(hash,0,sizeof(hash));
        scanf("%d",&num);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&tmp);
                if(i+1==num){
                    hash[tmp]++;
                }
            }
        }
        scanf("%d",&num);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&tmp);
                if(i+1==num){
                    hash[tmp]++;
                }
            }
        }
        cnt=0;
        for(i=1;i<=16;i++)
        {
            if(hash[i]==2){
                cnt++;
                num=i;
            }
        }
        if(cnt==1)    cout<<"Case #"<<kase<<": "<<num<<endl;
        else if(cnt>=2)           cout<<"Case #"<<kase<<": "<<"Bad magician!"<<endl;
        else cout<<"Case #"<<kase<<": "<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
