#include<cstdio>
int h[101][101];
int count[101];
int Min(int a,int b){return a<b?a:b;}
int main()
{
    int T;
    scanf("%d",&T);
    int index=0;
    while(T--)
    {
        for(int i=1;i<=100;i++)count[i]=0;
        int N,M;
        index++;
        scanf("%d %d",&N,&M);
        for(int i=0;i<N;i++)for(int j=0;j<M;j++)
        {
            scanf("%d",&h[i][j]);
            count[h[i][j]]++;
        }
        int nowh=1;
        int nownum=0;
        bool ww=true;
        while(nowh<=100)
        {
            int r=0,c=0;
            nownum+=count[nowh];
            for(int i=0;i<N;i++)
            {
                bool w=true;
                for(int j=0;j<M;j++)
                    if(h[i][j]>nowh)
                    {
                        w=false;
                        break;
                    }
                if(w)r++;
            }
            for(int i=0;i<M;i++)
            {
                bool w=true;
                for(int j=0;j<N;j++)
                    if(h[j][i]>nowh)
                    {
                        w=false;
                        break;
                    }
                if(w)c++;
            }
            nowh++;
            if((r*M+c*N-r*c)!=nownum){ww=false;break;}
            if(r*M+c*N-r*c==M*N)break;
        }
        printf("Case #%d: ",index);
        if(ww)puts("YES");
        else puts("NO");
    }
}
