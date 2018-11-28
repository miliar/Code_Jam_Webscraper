#include<bits/stdc++.h>
using namespace std;

int nq,n,r,p,s;
int a[10010];

void solve(int l,int r,int p)
{if(l==r)
 {	a[l]=p;	
 	return;
 }
 solve(l,(l+r)/2,(p+1)%3);
 solve((l+r)/2+1,r,(p-1+3)%3);
}

void change(int l,int r)
{int mid=(l+r)/2,i,j,s=1,flag=1;
 if(l==r) return;
 change(l,mid);
 change(mid+1,r);
 while(s<=mid-l+1 && a[l+s-1]==a[mid+s]) s++;
 if(s<=mid-l+1 && a[l+s-1]>a[mid+s])
 {	for(j=1;j<=mid-l+1;j++)
 		swap(a[l+j-1],a[mid+j]);
 }
}

int main()
{freopen("Al.in","r",stdin);
 freopen("Al.out","w",stdout);

 int i,j,q,s1,s2,s3,flag;
 
 scanf("%d",&nq);
 for(q=1;q<=nq;q++)
 {	scanf("%d%d%d%d",&n,&r,&p,&s);
 	solve(1,(1<<n),0);
 	s1=0;
 	s2=0;
 	s3=0;
 	for(i=1;i<=(1<<n);i++)
 		if(a[i]==0)
 			s1++;
 		else if(a[i]==1)
 			s2++;
 		else
 			s3++;
 	//cout<<s1<<" "<<s2<<" "<<s3<<endl;
 	//for(i=1;i<=(1<<n);i++) cout<<a[i]<<" ";
 	//cout<<endl;
 	if(p==s1)
 	{	for(i=1;i<=(1<<n);i++)
 			if(a[i]==0)
 				a[i]=1;
 			else if((r==s2 && a[i]==1) || (r!=s2 && a[i]!=1))
 				a[i]=2;
 			else
 				a[i]=3;
 	}
 	else if(p==s2)
 	{	for(i=1;i<=(1<<n);i++)
 			if(a[i]==1)
 				a[i]=1;
 			else if((r==s1 && a[i]==0) || (r!=s1 && a[i]!=0))
 				a[i]=2;
 			else
 				a[i]=3;
 	}
 	else
 	{	for(i=1;i<=(1<<n);i++)
 			if(a[i]==2)
 				a[i]=1;
 			else if((r==s1 && a[i]==0) || (r!=s1 && a[i]!=0))
 				a[i]=2;
 			else
 				a[i]=3;
 	}
 	flag=1;
 	s1=0;
 	s2=0;
 	s3=0;
 	for(i=1;i<=(1<<n);i++)
 		if(a[i]==1)
 			s1++;
 		else if(a[i]==2)
 			s2++;
 		else
 			s3++;
 	//cout<<s1<<" "<<s2<<" "<<s3<<endl;		
 	if(s1!=p || s2!=r || s3!=s)
 		flag=0;
 	change(1,(1<<n));
 	printf("Case #%d: ",q);
	if(flag)
	{	for(i=1;i<=(1<<n);i++)
			if(a[i]==1)
				printf("P");
			else if(a[i]==2)
				printf("R");
			else
				printf("S");
		printf("\n");
	}
	else
		printf("IMPOSSIBLE\n");
 }
 return 0;
}
