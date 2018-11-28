#include<bits/stdc++.h>
#define ll long long 
using namespace std;

bool prime[34333393];
vector<long int> v;
long long ans[34];


long long power(long long a,long long b)
{
	long long res=1;
	
	while(b>0)
	{
		if(b%2==1)
		res=(res*a);
		
		a=(a*a);
		b=b/2;
	}
	
	return res;
}

void pre(){
	v.clear();
	long long t,n,z,f,i,j;
prime[1]=true;
for(i=2;i<=34333333;i=i+1){
	if(prime[i]==false){
		v.push_back(i);
	for(j=2*i;j<=34333333;j=j+i)
	prime[j]=true;}
}
}

typedef unsigned long long ULL;

ULL mulmod(ULL a, ULL b, ULL c){
	ULL x = 0,y = a%c;
	
	while(b>0){
		if(b&1) x = (x+y)%c;
		y = (y<<1)%c;
		b >>= 1;
	}
	
	return x;
}

ULL exp(ULL a, ULL b, ULL c){
	ULL x = 1, y = a;
	
	while(b>0){
		if(b&1) x = mulmod(x,y,c);
		y = mulmod(y,y,c);
		b >>= 1;
	}
	
	return x;
}

bool myfunc(ULL p){
	int it=18;
	if(p<2) return false;
	if(p==2) return true;
	if((p&1)==0) return false;
	
	ULL s = p-1;
	while(s%2==0) s >>= 1;
	
	while(it--){
		ULL a = rand()%(p-1)+1,temp = s;
		ULL mod = exp(a,temp,p);
		
		if(mod==-1 || mod==1) continue;
		
		while(temp!=p-1 && mod!=p-1){
			mod = mulmod(mod,mod,p);
			temp <<= 1;
		}
		
		if(mod!=p-1) return false;
	}
	
	return true;
}


long long sp(long long val)
{	int i;
	for(i=0;i<v.size();i++)
	{
		if(val%v[i]==0)
		break;
	}
	
	
	return v[i];
}

int main()
{
	long long n,t,j1,k,j,dig,i,p,a1,a2,a3,a4,a5,a6,a7,a8,a9;
	pre();
//	cout<<"ok";
	ll cou=1;
	cin>>t;
	ll b;
	for(b=1;b<=t;b++)
	{
		cin>>n>>j1;
		printf("Case #%lld:\n",b);
		
		
		dig=n-2;
		
		p=power(2,dig);
		
		//cout<<p<<endl;
		
		for(i=0;i<p && j1>0 ;i++)
		{	a1=a2=a3=a4=a5=a6=a7=a8=a9=1;
			//cout<<i<<endl;
			ans[0]=1;ans[n-1]=1;
			
			for(j=0;j<=dig-1;j++)
			{
			
			if((i& (1<<j))!=0)
			{	j++;
				ans[j]=1;
				a1=a1+power(2,j);
				a2=a2+power(3,j);
				a3=a3+power(4,j);
				a4=a4+power(5,j);
				a5=a5+power(6,j);
				a6=a6+power(7,j);
				a7=a7+power(8,j);
				a8=a8+power(9,j);
				a9=a9+power(10,j);
				j--;
				
			}
			
			else{
			j++;
			ans[j]=0;
			
			j--;}
			
			
			
			}
			
				a1=a1+power(2,n-1);
				a2=a2+power(3,n-1);
				a3=a3+power(4,n-1);
				a4=a4+power(5,n-1);
				a5=a5+power(6,n-1);
				a6=a6+power(7,n-1);
				a7=a7+power(8,n-1);
				a8=a8+power(9,n-1);
				a9=a9+power(10,n-1);
			
				//cout<<a1<<" "<<a2<<" "<<a3<<" "<<a4<<endl;
				if(myfunc(a1)==false && myfunc(a2)==false && myfunc(a3)==false && myfunc(a4)==false && myfunc(a5)==false && myfunc(a6)==false && myfunc(a7)==false && myfunc(a8)==false &&myfunc(a9)==false )
				{	j1--;
					//cout<<"cou="<<cou++<<endl;
					for(k=n-1;k>=0;k--)
					cout<<ans[k];
					cout<<" ";
					cout<<sp(a1)<<" "<<sp(a2)<<" "<<sp(a3)<<" "<<sp(a4)<<" "<<sp(a5)<<" "<<sp(a6)<<" "<<sp(a7)<<" "<<sp(a8)<<" "<<sp(a9)<<"\n";
				}
			}
}
}
