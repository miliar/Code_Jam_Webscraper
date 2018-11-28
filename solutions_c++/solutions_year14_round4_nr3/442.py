
#include<stdio.h>
#include<iostream>
#include<cstring>

#define infi 1000000000
const int maxn=100111;
const int maxm=maxn*20;

struct cc
{
       int f,n,v;
};

cc e[maxm];
int dl[maxn],head[maxn],vh[maxn],h[maxn],W,H,
    maxx,ans,st,ed,totm,p,q,i,j,k,m,n,open,closed;
int ma[555][555];

int dx[]={0,1,-1,0};
int dy[]={1,0,0,-1};

void push(int x,int y,int ff)
{
     totm++;
     e[totm].v=y;e[totm].f=ff;
     e[totm].n=head[x];head[x]=totm;
     totm++;
     e[totm].v=x;e[totm].f=0;
     e[totm].n=head[y];head[y]=totm;
}

int aug(int x,int t)
{
    int p,l,d,minh;
    if (x==ed) return t;
    l=t;
    minh=ed-1;
    p=head[x];
    while (p>0)
    {
          if (e[p].f>0)
          {
			  if(h[x]==h[e[p].v]+1)
			  {
					if (l<e[p].f) d=l;else d=e[p].f;
					d=aug(e[p].v,d);
					l=l-d;
					e[p].f=e[p].f-d;
					e[p^1].f=e[p^1].f+d;
					if (h[st]>=ed) return t-l;
					if (l==0) break;
			  }
			  if (h[e[p].v] < minh) minh=h[e[p].v];
          }
       p=e[p].n;
    }
    if (t==l)
    {
             vh[h[x]]--;
             if (vh[h[x]]==0) h[st]=ed;
             h[x]=minh+1;
             vh[h[x]]++;
    }
    return t-l;
}

void bfs()
{
    for (i=1;i<=ed;i++) h[i]=-1;

    open=1;closed=0;dl[1]=ed;h[ed]=0;

    while (open!=closed)
    {
          closed++;
          i=dl[closed];
          p=head[i];
          while (p)
          {
                if (h[e[p].v]==-1)
                {
                    h[e[p].v]=h[i]+1;
                    open++;dl[open]=e[p].v;
                }
                p=e[p].n;
          }
    }

	memset(vh,0,sizeof(vh));
    for (i=1;i<=ed;i++) vh[h[i]]++;
    ans=0;
    maxx=infi;
}

int id(int x,int y,int z)
{
	return (x-1)*H+y+z*W*H;
}

int main()
{
	int x,y;


    //freopen("c.in","r",stdin);
    //freopen("c.out","w",stdout);
    int cas,cass=0,n,wid,hei,b,x0,y0,x1,y1;
    scanf("%d",&cas);
    while(cas--){
        cass++;

        memset(head,0,sizeof(head));
        memset(dl,0,sizeof(dl));
        memset(ma,0,sizeof(ma));



        scanf("%d%d%d",&wid,&hei,&b);

        n=wid*hei;

        totm=1;
        st=n+n+1;ed=n+n+2;

        for(int i=1;i<=b;i++){
            scanf("%d%d%d%d",&x0,&y0,&x1,&y1);

            x0++;y0++;x1++;y1++;

            for(int j=x0;j<=x1;j++)
            for(int k=y0;k<=y1;k++)
                ma[j][k]=1;
        }
        W=wid,H=hei;

		for(int i=1;i<=W;i++)
			for(int j=1;j<=H;j++)
				if( !ma[i] [j] )
					push(id(i,j,0),id(i,j,1),1);
		for(int x=1;x<=W;x++)
        for(int y=1;y<=H;y++)
        {
            for(int k=0;k<4;k++)
            {
                int xx=x+dx[k] ;
                int yy=y+dy[k] ;
                if(xx>=1&&xx<=W&&yy>=1&&yy<=H&&!ma[x] [y] &&!ma[xx] [yy] )
                    push(id(x,y,1),id(xx,yy,0),infi);
            }
        }


		for(int i=1;i<=W;i++)
			push(st,id(i,1,0),1);
		for(int i=1;i<=W;i++)
			push(id(i,H,1),ed,1);

        bfs();
        while (h[st]<ed)
            ans=ans+aug(st,maxx);

        printf("Case #%d: %d\n",cass,ans);
    }



    return 0;
}
