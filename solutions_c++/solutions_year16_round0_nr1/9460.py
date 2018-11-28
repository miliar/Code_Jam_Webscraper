#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

using namespace std;

#define s(n) scanf("%d",&n)	
#define sl(n) scanf("%ld",&n)
#define sll(n) scanf("%lld",&n)
#define p(n) printf("%d ",n)
#define pl(n) printf("%ld ",n)
#define pll(n) printf("%lld\n",n)
#define fo(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b)	for(i=a;i>=b;i--)
# define toint(n)	(n-'0')
typedef long long ll;

bool visitedDigit[10];

bool ContainsOddDigit(ll n) {
	int temp;
	while(n) {
		temp=n%10;
		if((temp==1)||(temp==3)||(temp==7)||(temp==9)) {
			return true;
		}
		n/=10;
	}
	return false;
}

bool allVisited() {
	int i;
	fo(i,0,10) {
		if(visitedDigit[i]==false)
			return false;
	}
	return true;
}

int main(int argc, char const *argv[])
{
	//freopen("2016A-large.in","r",stdin);
	//freopen("2016A-large.out","w",stdout);
	int t,k,i,iniLog;
	ll n,ans,temp,tempAns,lim;

	s(t);
	fo(k,1,t+1)
	{

		memset(visitedDigit,false,10);
		ans=-1;

		sll(n);
		if(n==0)
			ans=-1;
		else if(ContainsOddDigit(n)) {
			//cout<<"Contains Odd Digit\n";
			/*temp=n;
			lim=1;
			while(temp) {
				lim*=10;
				temp/=10;
			}*/
			lim=1000000;

			fo(i,1,lim+1) {
				temp=n*i;
				tempAns=temp;
				while(temp) {
					visitedDigit[temp%10]=true;
					temp/=10;
				}
				if(allVisited()) {
					ans=tempAns;
					break;
				}
			}
		}
		else {
			/*cout<<"Contains Even Digit\n";
			iniLog = log10(n);
			temp = n;
			i=2;
			while((int)log10(temp)!=iniLog+1) { 
				temp = n*i;
				i++;
			//	cout<<"Log(n) = "<<log10(n)<<"	log(temp) = "<<log10(temp)<<endl;
			}
			//cout<<"Stage 1\n";
			n= temp;
			cout<<"new n = "<<n<<endl;*/
			
			temp = n;
			lim=1000000;
			/*while(temp) {
				lim*=10;
				temp/=10;
			}*/

			fo(i,1,lim+1) {
				temp=n*i;
				//cout<<"values: "<<n*i<<endl;
				tempAns = temp;
				while(temp) {
					visitedDigit[temp%10]=true;
					temp/=10;
				}
				if(allVisited()) {
					ans=tempAns;
					break;
				}
			}
		}

		if(ans<0)
			printf("Case #%d: INSOMNIA\n",k );
		else
			printf("Case #%d: %lld\n",k,ans);

	}
	return 0;
}