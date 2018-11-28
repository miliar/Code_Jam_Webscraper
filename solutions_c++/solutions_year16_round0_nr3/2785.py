# include <bits/stdc++.h>
using namespace std;
bool p[1000006];
int a[1000006];
vector <int >v;
vector <int >v1;
long long pow(int a, int b)
{
	long long x=1,y=a; 
	while(b > 0)
	{
		if(b%2 == 1)
		{
			x=(x*y);
		}
		y = (y*y);
		b /= 2;
	}
	return x;
}
int main()
{
	freopen("input.txt","r", stdin);
freopen("out.txt", "w", stdout);
memset(p,true,sizeof(p));
int t,i,j,n,c=0,r,i1;long long int s=0;
for(i=2;i*i<1000006;i++)
{
	if(p[i])
	{
		for(j=i*i;j<1000006;j=j+i)
		p[j]=false;
	v.push_back(i);
	}
}


cin>>t;
for(int a1=1;a1<=t;a1++)
{
	
	cin>>n>>j;c=0;
	printf("Case #%d:\n",a1);
	for(i=1<<(n-1);i<(1<<n);i++)
    {  
    if(i%2==0)
	continue;
	int k=i,o=0;
		while(k>0)
		{
			a[o++]=k%2;
            k/=2;
		}
		int flag1=0,flag2=0;
		v1.clear();
		for(r=2;r<=10;r++)
		{
			flag1=0;s=0;
                for(i1=0;i1<o;i1++)
                	s+=a[i1]*pow(r,i1);
                for(i1=0;i1<v.size();i1++)
                {
                	if(s%v[i1]==0)
                	{
                		flag1=1;
                		v1.push_back(v[i1]);
                		break;
                	}
                }
                if(!flag1)
                	flag2=1;
		}
		if(flag2==0)
			 {
			   for(i1=o-1;i1>=0;i1--)
			   	printf("%d",a[i1]);
			   printf(" ");
	           for(i1=0;i1<v1.size();i1++)
	           printf("%d ",v1[i1]);    
	           printf("\n");
	           c++;
	         }
		if(c>=j)
			break;
	}
}
return 0;
}