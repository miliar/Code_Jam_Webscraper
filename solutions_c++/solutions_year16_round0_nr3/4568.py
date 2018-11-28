#include<bits/stdc++.h>
using namespace std;
vector<long long>v;
#define ULL unsigned long long
//const long long MOD=1E9+7;
long long fast_exp(long long base, long long exp) 
{
    long long res=1;
    while(exp>0) {
       if(exp%2==1) res=(res*base);
       base=(base*base);
       exp/=2;
    }
    return res;
}
void prime_fact(long long n)
{
	//long long num=n;
    if (n%2 == 0)
    {
        printf("%lld ", 2);
        return;
        //n = n/2;
    }
    for (long long i = 3; i <= sqrt(n); i = i+2)
    {
        if (n%i == 0)
        {
            printf("%lld ", i);
            return;
            //n = n/i;
        }
    }
    //if (n > 2)
      //  printf ("%lld ", n);
}

ULL mulmod(ULL a, ULL b, ULL c){
	ULL x = 0,y = a%c;
	
	while(b>0){
		if(b&1) x = (x+y)%c;
		y = (y<<1)%c;
		b >>= 1;
	}
	
	return x;
}

ULL pow(ULL a, ULL b, ULL c){
	ULL x = 1, y = a;
	
	while(b>0){
		if(b&1) x = mulmod(x,y,c);
		y = mulmod(y,y,c);
		b >>= 1;
	}
	
	return x;
}

bool miller_rabin(ULL p, int it){
	if(p<2) return false;
	if(p==2) return true;
	if((p&1)==0) return false;
	
	ULL s = p-1;
	while(s%2==0) s >>= 1;
	
	while(it--){
		ULL a = rand()%(p-1)+1,temp = s;
		ULL mod = pow(a,temp,p);
		
		if(mod==-1 || mod==1) continue;
		
		while(temp!=p-1 && mod!=p-1){
			mod = mulmod(mod,mod,p);
			temp <<= 1;
		}
		
		if(mod!=p-1) return false;
	}
	
	return true;
}
 
int main()
{
	freopen("output.txt","w",stdout);
	int t,i,j,n,m;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		
		cin>>n>>m;
		cout<<"Case #"<<i<<" :\n";
		int x=1;
		for(j=0;j<fast_exp(2,n);j++)
		{
			if(x>m)
			break;
			long long num=j;
			int arr[n],index=0;
			for(int y=0;y<n;y++)
			{
				if(j&(1<<y))
				arr[index++]=1;
				else
				arr[index++]=0;
			}
			if((arr[0]==1) && (arr[n-1]==1))
			{
				//for(int k=1;k<=m;k++)
				//{
					
				for(int base=2;base<=10;base++)
				{
					
					long long num1=0;
					for(index=0;index<n;index++)
					{
						num1+=arr[index]*fast_exp(base,index);
					}
					
					if(miller_rabin(num1,18)==false)
					{
						v.push_back(num1);
					}
			//	}
				}
				if(v.size()<9)
				{
					v.clear();
				}
				else
				{
					x++;
					for(int k=n-1;k>=0;k--)
					cout<<arr[k];
					for(int base=2;base<=10;base++)
					{
						cout<<" ";
						prime_fact(v[base-2]);
					}
					cout<<endl;
					v.clear();
				}
			}
		}
	v.clear();
	}
return 0;
}
