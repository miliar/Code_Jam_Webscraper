#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
int main()
{
    freopen("in.txt","r",stdin); //�������ݽ���in.txt�ļ��ж�ȡ
    freopen("out.txt","w",stdout); //������ݽ�������out.txt�ļ���
    double C,F,X,mintime,temptime,cookie,nowtime,temp,ans,nowmin;
    int T;
    scanf("%d",&T);
    for (int k=1;k<=T;k++)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        cookie=0.0;
        ans=2.0;
        nowtime=0;
        mintime=9999999999.99999;
        while(cookie<X)
        {
            temptime=X/ans;
            if(mintime>nowtime+temptime) mintime=nowtime+temptime;
            temp=C/ans;
            if (temptime>temp+X/(ans+F))
            {
                if(mintime>temp+nowtime+X/(ans+F)) mintime=temp+nowtime+X/(ans+F);
                nowtime+=temp;cookie+=C;ans+=F;
            }
            else if (temptime<=temp+X/(ans+F))
            {
                if(mintime<nowmin+temptime)mintime=nowmin+temptime;
                nowtime+=temp;
                cookie+=C;
            }
        }
        printf("Case #%d: %.7lf\n",k,mintime);
    }
    fclose(stdin);//�ر��ļ�
    fclose(stdout);//�ر��ļ�
    return 0;
}
