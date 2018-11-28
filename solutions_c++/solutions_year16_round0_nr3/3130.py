#include <iostream>
#include <string>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <vector>
using namespace std;


unsigned long long N,J;

unsigned long long num[35];
int modulo(long long  a,long long b,long long c){
    long long x=1,y=a; // long long is taken to avoid overflow of intermediate results
    while(b > 0){
        if(b%2 == 1){
            x=(x*y)%c;
        }
        y = (y*y)%c; // squaring the base
        b /= 2;
    }
    return x%c;
}
long long mulmod(long long a,long long b,long long c){
    long long x = 0,y=a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y)%c;
        }
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}
bool Miller(long long p,int iteration){
    if(p<2){
        return false;
    }
    if(p!=2 && p%2==0){
        return false;
    }
    long long s=p-1;
    while(s%2==0){
        s/=2;
    }
    for(int i=0;i<iteration;i++){
        long long a=rand()%(p-1)+1,temp=s;
        long long mod=modulo(a,temp,p);
        while(temp!=p-1 && mod!=1 && mod!=p-1){
            mod=mulmod(mod,mod,p);
            temp *= 2;
        }
        if(mod!=p-1 && temp%2==0){
            return false;
        }
    }
    return true;
}
bool primes[10000010];
vector < unsigned long long > prs;
unsigned long long modl[32][10][10];
void era()
{
	primes[2] = false;
	for(unsigned long long i =  3 ;  i < 10000010; i++)
	{
		if(primes[i])continue;
		prs.push_back(i);
		for(unsigned long long j = i*i;j< 10000010; j+=i)
			primes[j] = true;
	}
}
unsigned long long divs[11];
void rec(int i)
{
	if(i == 13)
	{
		unsigned long long res = 0LL;
	bool f = true;
	//for(int k = J-1;k>=0;k--)
	//		cout << num[k];
	//		cout << endl;
		for(unsigned long long j = 2 ; j <=10 && f;j++ )
		{
			
			res = 0LL;
				unsigned long long p = 1;
			for(int k = 0 ; k < 13; k++,p*=j)
			  res += p * num[k];
			
			
			
			bool founddiv= false;
			for(int k = 0 ; k < prs.size(); k++)
			{
				if((res%prs[k] + modulo(j,J-1,prs[k]))%prs[k]==0){
					divs[j] = prs[k];
					founddiv= true;
					break;
				}		
			}
			if(!founddiv){
				f = false;
				break;
			}
		}
		if(f){
		//cout << N << endl;
			for(int k = J-1;k>=0;k--)
			cout << num[k];
			for(int k=2;k<=10;k++)
			{
			
		
			res = 0LL;
			unsigned long long p = 1;
			for(int K = 0 ; K < 13; K++,p*=k)
			{
					res += p * num[K];
			}
		//cout << " " << res;
	//	if(divs[k] == 269) cout <<" " << res << " ---------x ";
		cout << " " << divs[k];
			}
			cout << endl;
			N--;
		}
		
	}else{
		num[i] = 0LL;
		if(N>0)rec(i+1);
		num[i] = 1LL;
		if(N>0)rec(i+1);
	}
	
}
long long solve()
{
	num[0] = 1LL;
	num[J-1] = 1LL;
	rec(1);
}
int main()
{
//	srand((int)time(NULL));
	 // ios_base::sync_with_stdio(false);
    freopen("1.in","r",stdin);   freopen("1.out","w",stdout);
    era();
 cout << modulo(4,31,189187) << endl;
    
 int T;
 cin >> T;
 long long maxres=0;
 for(int i = 0 ; i <T ; i++)
 {
 
	cin >> J >> N;
	cout << "Case #1:\n";
	
	solve();
	}
//cout << maxres << endl;
	return 0;
}
