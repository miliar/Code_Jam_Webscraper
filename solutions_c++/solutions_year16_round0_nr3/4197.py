#include<iostream>
#include<math.h>
#include<Infint.h>

using namespace std;
InfInt power(int b,int j)
{
	InfInt tot=1;
	for(;j>0;j--)
		tot*=b;
	return tot;
}
int pcheck(InfInt a)
{
	InfInt sq=a.intSqrt();
	if(a%2==0)
		return 2;


	for(InfInt i=3;i<sq;i+=2)
	{
		if(a%i==0)
		{
			return i.toInt();
		}
	}
	return -1;
}
InfInt base(char a[],int n,int b)
{
	InfInt tot=0;
	int j=n-1;
	for(int i=0;i<n;i++,j--)
	{
		if(a[i]=='1')
			tot+=(power(b,j));
	}
	return tot;
}

static char *binrep (unsigned int val, char *buff, int sz) {
    char *pbuff = buff;
    pbuff += sz;
    *pbuff-- = '\0';
    *pbuff-- = '1';
	sz--;
    while (val != 0) {
        *pbuff-- = ((val & 1) == 1) ? '1' : '0';

        val >>= 1;
        sz--;
    }
    while(sz>1) {
    	*pbuff-- ='0';
    	sz--;
	}
    *pbuff='1';
    return pbuff;
}


int main()
{
	int n,nc,flag;
	int i,j;
	int ans[10];
	char a[33],*p;
	cin>>n;
	nc=n;
	while(n>0)
	{
		cin>>i>>j;
		cout<<"Case #"<<(nc-n)+1<<": ";
		for(int k=0;(k<pow(2,(i-2)))&&j>0;k++)
		{
			p=binrep(k,a,i);
			//cout<<p<<" ";
			flag=1;
			for(int m=2;m<=10;m++)
			{
				//cout<<base(p,i,m)<<" ";
				ans[m-2]=pcheck(base(p,i,m));
				if(ans[m-2]==-1)
				{
					flag=0;
					break;
				}
				//cout<<m<<" ";
			}
			if(flag){
				j--;
				cout<<endl<<p<<" ";
				for(int m=0;m<=8;m++)
					cout<<ans[m]<<" ";
				//cout<<endl;
				
			}
			//else cout<<" nop\n";
		}
		
		
		n--;
	
		
	}
}
