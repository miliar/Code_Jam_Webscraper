#include<bits/stdc++.h>
using namespace std;
struct point{
    long long x,y;
    int ind;
};
point P1[20],C[20],T[20];
int N;
int ans[20];
point P0;
int mask;

inline long long line(point a,point b,point c)//computes area of tringle area,if 0,then same line
{
   long long area=a.x*b.y+b.x*c.y+c.x*a.y-a.y*b.x-b.y*c.x-c.y*a.x;
   return area;
}

inline long long sqdist(point A,point B)
{
   long long ret=(A.x-B.x)*(A.x-B.x)+(A.y-B.y)*(A.y-B.y);
   return ret;
}

bool comp(point A,point B)
{
    long long area=line(P0,A,B);
    if(area<0) return false;//right turn
    else if(area>0) return true;//left turn
    else
    {
        return (sqdist(P0,A)<sqdist(P0,B));//shorter dist point comes first
    }
}

bool onseg(point A,point B,point C)
{
    long long minX,minY,maxX,maxY;
    minX=min(A.x,B.x);
    minY=min(A.y,B.y);
    maxX=max(A.x,B.x);
    maxY=max(A.y,B.y);
    if(C.x>=minX && C.x<=maxX && C.y>=minY && C.y<=maxY)  return true;
    else return false;
}

//inside 1,outside -1,online 0
int inside(point P[],int n,point A)
{
    int i;
    long long area;
    //cout<<A.x<<" "<<A.y<<endl;
    for(i=0; i<n; i++)
    {
        area=line(P[i],P[(i+1)%n],A);
        if(area==0 && onseg(P[i],P[(i+1)%n],A))  return 0;
    }

    int sgn=0;
    for(i=0; i<n; i++)
    {
        area=line(P[i],P[(i+1)%n],A);
        //cout<<i<<" area:"<<area<<endl;
        if(area<0)  return -1;
    }


    //printf("here\n");
    return 1;
}



void C_hull(point P[],int sz)
{
    int i,j,k,n;
    int mn=0;
    for(i=1; i<sz; i++)
    {
          if(P[i].y<P[mn].y)
              mn=i;
          else if(P[i].y==P[mn].y)
          {
             if(P[i].x<P[mn].x)  mn=i;
          }
    }
    P0=P[mn];
    swap(P[mn],P[0]);
    P[sz]=P[0];
    sort(P+1,P+sz,comp);
//    for(i=0; i<sz; i++)
//    {
//        cout<<P[i].ind<<" "<<P[i].x<<" "<<P[i].y<<endl;
//    }
//    cout<<endl;
    bool deg=true;
    for(i=0; i+2<sz; i++)
    {
        long long area=line(P[i],P[i+1],P[i+2]);
        if(area!=0)  deg=false;
    }

    if(deg)
    {
        for(i=0; i<sz; i++)
        {
            int indx=P[i].ind;
            ans[indx]=min(ans[indx],N-sz);
        }
        return;
    }

    C[0]=P[0];C[1]=P[1];P[sz]=P0;
    for(i=2,n=2; i<=sz; i++)
    {
      while(n>=2 && line(C[n-2],C[n-1],P[i])<0) n--;//while it takes right turn,not member of Hull
      C[n++]=P[i];
    }
    --n;//excluding the end point,as it is same as the starting point


//    for(i=0; i<n; i++)
//    {
//        cout<<C[i].ind<<" "<<C[i].x<<" "<<C[i].y<<endl;
//    }
//    cout<<endl;

//      P1[N].x=-3;P1[N].y=0;
//      N++;

      int out=0;


      for(i=0; i<N; i++)
      {
          int ins=inside(C,n,P1[i]);
          //cout<<"ins:"<<ins<<" "<<P1[i].x<<" "<<P1[i].y<<endl;
          if(ins==-1)  out++;
      }
      //printf("OUT:%d\n",out);


      for(i=0; i<N; i++)
      {
          if(inside(C,n,P1[i])==0){
              int indx=P1[i].ind;
              ans[indx]=min(ans[indx],out);

          }
      }
}

int main()
{
    int Test,it,i,nn;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&Test);
    for(it=1; it<=Test; it++)
    {
        scanf("%d",&N);
        for(i=0; i<N; i++){
                cin>>P1[i].x>>P1[i].y;
                P1[i].ind=i;
        }

        for(i=0; i<N; i++)  ans[i]=2*N;
        //mask=19;
        for(mask=1; mask<(1<<N); mask++)
        {
            nn=0;
            for(i=0; i<N; i++)
            {
                if(mask&(1<<i)){
                    T[nn++]=P1[i];
                }
            }
            C_hull(T,nn);
        }
        printf("Case #%d:\n",it);
        for(i=0; i<N; i++)  printf("%d\n",ans[i]);
    }
    return 0;
}
