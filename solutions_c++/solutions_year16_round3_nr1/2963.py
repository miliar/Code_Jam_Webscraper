#include<iostream>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
#include<limits.h>
using namespace std;

/*printing definitions*/
#define pi(x) printf("%d\n",(x))
#define pii(x,y) printf("%d %d\n",(x),(y))
#define pl(x) printf("%lld\n",(x))
#define pll(x,y) printf("%lld %lld\n",(x),(y))
#define pil(x,y) printf("%d %lld\n",(x),(y))
#define pli(x,y) printf("%lld %d\n",(x),(y))
#define plf(x) printf("%lf\n",(x))
#define plflf(x,y) printf("%lf %lf\n",(x),(y))

/*scanning definitions*/
#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define sil(x,y) scanf("%d %lld",&x,&y)
#define sli(x,y) scanf("%lld %d",&x,&y)
#define slf(x) scanf("%lf",&x)
#define slflf(x,y) scanf("%lf %lf",&x,&y)

//  CREATED BY: ATUL SEHGAL

int x[256],c[256];

void mergesort2(int *,int *,int,int);
void merge2(int *,int *,int,int,int);
int i1,b1[1005],e1[1005];
int main()
{
    freopen("input-A-small.txt","r",stdin);
    freopen("output-A-small.txt","w",stdout);
 	int t,n,cnt,T=1, i, j;
 	
	si(t);
	while(t--)
	{
		si(n);
		cnt=0;
		for(i=0;i<200;i++)
            c[i] = i;
        memset(x,0,sizeof(x));
        
		for(i=0;i<n;i++)
        {
            si(x[i]),cnt+=x[i];
        }
		
		printf("Case #%d: ",T++);
		
		//for(j=0;j<n;j++)
               // cout<<x[j]<< " " <<c[j]<<endl;
		int cc = cnt;
		for(i=0;i<cc;i++)
        {
            //cout<< "i =  "<<i<<endl;
            //cout<<"into loop -> "<<i<<endl;
            //cout<<"cnt -> "<<cnt <<endl;
            mergesort2(x,c,0,n-1);
            
            //cout<<endl;
            //for(j=0;j<n;j++)
            //    cout<<x[j]<< " " <<c[j]<<endl;
            if(cnt==2)
            {
              //  cout<<"the count became 2\n";
              //  cout<<"x[n-1] -> "<<x[n-1]<<"   x[n-2] -> "<<x[n-2]<<endl;
                if(x[n-1] && x[n-2])
                    printf("%c%c",'A' + c[n-1],'A' + c[n-2]);
                else
                    printf("%c%c",'A' + c[n-1],'A' + c[n-1]);
                cnt=0;
                x[n-1]=x[n-2]=0;
                break;
            }
            if(cnt)
            {
                double pr = 0.0, limit =50.0;
                //case- 1 apne hi do
                for(j=0;j<n;j++)
                {
               //    // cout<<((double)x[j]*100.0)/(double)(cnt-2)<<endl;
                //   // cout<<((double)(x[j]-2)*100.0)/(double)(cnt-2)<<endl;
                //   // cout<<"j = "<<j<<endl;
                    if(j == n-1 && !(((double)(x[j]-2)*100.0)/(double)(cnt-2) <= limit))
                        break;
                    else if(j < n-1 && !(((double)x[j]*100.0)/(double)(cnt-2) <= limit))
                        break;
                }
                if(j==n)
                {
                  // // cout<<"case-1 passed\n";
                    x[n-1] -= 2;
                    cnt -= 2;
                    printf("%c%c",'A'+c[n-1],'A'+c[n-1]);
                }
                else
                {
                    //case-2 mix of two
                    for(j=0;j<n;j++)
                    {
                    //cout<<((double)x[j]*100.0)/(double)(cnt-2)<<endl;
                    //cout<<((double)(x[j]-1)*100.0)/(double)(cnt-2)<<endl;
                        if(j > n-3 && !(((double)(x[j]-1)*100.0)/(double)(cnt-2) <= limit))
                            break;
                        else if(j < n-2 && !(((double)x[j]*100.0)/(double)(cnt-2) <= limit))
                            break;
                    }
                    
                    if(j==n)
                    {
                       // cout<<"case-2 passed\n";
                        x[n-1] -= 1;
                        x[n-2] -= 1;
                        cnt -= 2;
                        printf("%c%c",'A'+c[n-1],'A'+c[n-2]);
                    }
                    else
                    {
                   // cout<<"into case-3\n";
                        //case-3 Only one max wala
                        for(j=0;j<n;j++)
                        {
                            
                   // cout<<((double)x[j]*100.0)/(double)(cnt-1)<<endl;
                   // cout<<((double)(x[j]-1)*100.0)/(double)(cnt-1)<<endl;
                            if(j == n-1 && !(((double)(x[j]-1)*100.0)/(double)(cnt-1) <= limit))
                                break;
                            else if(j < n-1 && !(((double)x[j]*100.0)/(double)(cnt-1) <= limit))
                                break;
                        }
                        x[n-1] -= 1;
                        cnt -= 1;
                        printf("%c",'A'+c[n-1]);
                    }
                }
            
            }
            //cout<<"cnt -> "<<cnt<<endl;
            if(cnt)
                printf(" ");
        }
		
		printf("\n");
	}
	return 0;
}


void mergesort2(int a[],int e[],int i1,int j)
{
   int mid;
   if(i1<j)
   {
      mid=(i1+j)/2;
      mergesort2(a,e,i1,mid);
      mergesort2(a,e,mid+1,j);
      merge2(a,e,i1,mid,j);
   }
}
void merge2(int a[],int e[],int low,int mid ,int high)
{
   int h,i,j,k;
   h=low;
   i=low;
    j=mid+1;
   while(h<=mid && j<=high)
   {
      if(a[h]<=a[j])
	   {
            b1[i]=a[h];
            e1[i]=e[h++];             
       }
      else
	   {
            b1[i]=a[j];
            e1[i]=e[j++];
       }
      i++;
   }
   if( h > mid)
    {
        for(k=j;k<=high;k++)
        {
            b1[i]=a[k];
            e1[i++]=e[k];
        }
    }
   else
   {
        for(k=h;k<=mid;k++)
        {
            b1[i]=a[k];
            e1[i++]=e[k];
        }
   }
   for(k=low;k<=high;k++)
   { 
        a[k]=b1[k];
        e[k]=e1[k];
   }
}
