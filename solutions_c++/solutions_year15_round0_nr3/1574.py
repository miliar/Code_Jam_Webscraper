#include<cstdio>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstdlib>

using namespace std;

const int r[6][6]={{},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};

int mul(long long  x,long long y)
{
  int k,ff;
  ff=1;k=x*y;
  if (k<0) {ff=-1;k=-k;}
  return r[abs(x)][abs(y)]*ff;
}

int xn(long long x,long long n)
{
    if (n==1) return x;
    if (n==0) return 1;
    if (n==2) return mul(x,x);
    int kkkk;
    kkkk=xn(x,n/2);
    return mul(kkkk,mul(kkkk,xn(x,n%2)));
}

int main()
{
//	freopen("C-large.in","r",stdin);
//    freopen("out-large.txt","w",stdout);
    long long X,L;
    int a[10100];
    char p[10500];
    int T,ss;
    cin>>T;
    for (int nT=1;nT<=T;nT++)
    {
    	bool flg=true;
	 	cin>>L>>X;
        cin>>p;
        for (int i=0;i<L;i++)
        {
          if (p[i]=='i') a[i+1]=2;
          if (p[i]=='j') a[i+1]=3;
          if (p[i]=='k') a[i+1]=4;
        }
        ss=1;
        for (int i=1;i<=L;i++) 
			ss=mul(ss,a[i]);
        if (xn(ss,X%4)!=-1) 
			flg=false;
		else
		{
	        ss=1;
	        int ii,kk;
	        for (ii=1;ii<=L*(X<=9?X:9);ii++)
	        {
	           ss=mul(ss,a[(ii-1)%L+1]);
	           if (ss==2) break;
	        }
	        if (ss!=2) 
				flg=false;
			else
			{
		        ss=1;
				for (kk=1;kk<=L*(X<=9?X:9)&&(kk+ii<X*L);kk++)
		        {
		        	ss=mul(a[L-(kk-1)%L],ss);
		        	if (ss==4) break;
		        }
		        if (ss!=4) flg=false;
		    }
    	}
        printf(flg?"Case #%d: YES\n":"Case #%d: NO\n",nT);
    }
    return 0;
}
