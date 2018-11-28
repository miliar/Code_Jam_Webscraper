#include<stdio.h>
#include<string>
using namespace std;
main()
{
    int a,b,c,rps[3],nrps[3],n,i,j,k,l,nq,q;
    string str,temp;
    scanf("%d",&nq);
    for(q=0;q<nq;q++)
    {
        scanf("%d%d%d%d",&n,&nrps[0],&nrps[1],&nrps[2]);
        rps[0]=1;
        rps[1]=0;
        rps[2]=0;
        for(i=0;i<n;i++)
        {
            a=rps[0]+rps[1];
            b=rps[1]+rps[2];
            c=rps[2]+rps[0];

            rps[0]=a;
            rps[1]=b;
            rps[2]=c;
        }
        for(i=0;i<3;i++)
        {
            for(j=0;j<3;j++)
                if(rps[j]!=nrps[j])
                    break;
            if(j>=3)
                break;
            a=rps[2];
            b=rps[0];
            c=rps[1];
            rps[0]=a;
            rps[1]=b;
            rps[2]=c;
        }
        if(i>=3)
            printf("Case #%d: IMPOSSIBLE\n",q+1);
        else
        {
            if(i==0)
                str="R";
            else if(i==1)
                str="P";
            else if(i==2)
                str="S";
            for(i=0;i<n;i++)
            {
                temp="";
                for(j=0;j<str.length();j++)
                {
                    if(str[j]=='R')
                        temp+="RS";
                    else if(str[j]=='P')
                        temp+="PR";
                    else if(str[j]=='S')
                        temp+="PS";
//                    printf("%s %s\n",str.c_str(),temp.c_str());
                }
                str=temp.c_str();
            }
            for(i=2;i<=(1<<n);i=(i<<1))
            {
                for(k=0;k<str.length();k+=i)
                {
                    for(j=0;j<i/2;j++)
                    {
                        if(str[k+j]>str[k+i/2+j])
                            break;
                    }
                    if(j<i/2)
                    {
                        for(l=0;l<i/2;l++)
                            swap(str[k+l],str[k+i/2+l]);
                    }
                }
            }
            printf("Case #%d: %s\n",q+1,str.c_str());
        }
    }
    return 0;
}
