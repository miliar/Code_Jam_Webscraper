#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
main()
{
    int n;
    scanf("%d",&n);
    for(int k=1; k<=n; k++)
    {
        int a,b;
        scanf("%d %d",&a,&b);
        int field[a][b];
        int m=-555;
        int count[101]= {0};
        for(int i=0; i<a; i++)
        {
            for(int j=0; j<b; j++)
            {
                scanf("%d",&field[i][j]);
                if(field[i][j]>m)m=field[i][j];
                count[field[i][j]]++;
            }
        }
        bool ans=true;
        printf("Case #%d: ",k);
        int crr[a][b];
        bool f[a][b];
        for(int i=0; i<a; i++)
        {
            for(int j=0; j<b; j++)
            {
                crr[i][j]=m;
                f[i][j]=false;
            }
        }
        for(int l=m; l>0; l--)
        {
            for(int i=0; i<a; i++)
            {
                bool tmp=true;
                for(int j=0; j<b; j++)
                {
                    if(f[i][j])
                    {
                        tmp=false;
                        break;
                    }
                }
                if(tmp)
                {
                    //printf("%d\n",i);
                    for(int j=0; j<b; j++)
                    {
                        crr[i][j]=l;
                        //printf("%d %d\n",i,j);
                        if(crr[i][j]==field[i][j])
                        {
                            f[i][j]=true;
                            count[crr[i][j]]--;
                        }
                    }
                }
            }
            for(int i=0; i<b; i++)
            {
                bool tmp=true;
                for(int j=0; j<a; j++)
                {
                    if(f[j][i]&&crr[j][i]!=l)
                    {
                        tmp=false;
                        break;
                    }
                }
                if(tmp)
                {
                    //printf("%d\n",i);
                    for(int j=0; j<a; j++)
                    {
                        crr[j][i]=l;
                        if(crr[j][i]==field[j][i]&&!f[j][i])
                        {
                            f[j][i]=true;
                            count[crr[j][i]]--;
                        }
                    }
                }
            }
            //printf("%d\n",count[l]);
            if(count[l]>=1)
            {
                ans=false;
                break;
            }
        }
        /*for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                if(f[i][j])printf("1 ");
                else printf("0 ");
            }
            printf("\n");
        }*/
        if(ans)printf("YES\n");
        else printf("NO\n");
    }
}
