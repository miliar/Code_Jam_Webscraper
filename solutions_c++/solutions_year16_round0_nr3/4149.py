#include "bits/stdc++.h"

using namespace std;

#define mp make_pair
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
/*
int suspect(long long b, int t, long long u, long long n)
{
long long prod=1;
while(u)
{
if(u&1) prod=((prod*b)%n);
b=((b*b)%n);
u/=2;
}
if(prod == 1) return 1;
for(int i = 1; i <= t; i++)
{
if(prod == n-1) return 1;
prod = (prod * prod) % n;
}
return 0;
}
int isprime(long long int n)
{
long long int k = n - 1;
long long int t = 0;
while(!(k%2)) { t++; k/=2; }
if(n>2 && n%2==0) return 0;
if(n>3 && n%3==0) return 0;
if(n>5 && n%5==0) return 0;
if(n>7 && n%7==0) return 0;
if(suspect(61, t, k, n) && suspect(7, t, k, n) && suspect(2, t, k, n))
return 1;
return 0;
}*/
int prime[1000001];
vector<int> prime2;
int main()
{
	ll T,N,J, ans[11], ans2[11], num = 0,i,j,k,t=0,check;
	prime[0] = prime[1] = 1;
	prime2.push_back(2);
	for(i = 2;i<=1000000;i+=2){
		prime[i] = 1;
	}
	for(i = 3;i*i<=1000;i+=2){
		if(prime[i] == 0){
		   prime2.push_back(i);	
           for(j = 2*i;j<=1000000;j+=i) prime[j] = 1;
		}
	}
	for(;i<=1000000;i+=2){
		if(prime[i] == 0) prime2.push_back(i);
	}

	cin >> T;
	cin >> N >> J;
	ll start = (1<<15)+1;
	ll limit = 1<<16;
	//cout << start << ' ' << limit << '\n';
	cout << "Case #1:\n";
	for(i = start;i<limit && t < 50;i+=2){
		num = i;
		string str = "";
		memset(ans,0,sizeof(ans));
		while(num != 0){
			if(num%2==1){
               /*for(j = 2;j<=10;++j){
               	  ans[j] = ans[j]*j + 1;
               }*/
               str = "1"+str;
			}
			else str = "0"+str;
			num/=2;
		}
		for(k=2;k<=10;++k){
		    for(j = 0;j<str.size();++j){
				if(str[j] == '1'){
				   ans[k] = ans[k]*k+1;
				}
				else ans[k]*=k;
			}
		}
		//cout << "Entered\n";
		check = 1;
		/*for(j = 2;j<=10;++j){
			check = 1;
			for(k = 2;k*k<=ans[j];++k){
				if(ans[j]%k==0){
				   check = 0;
				   ans2[j] = k;
				   break;
				}
			}
			if(check == 1) break;
		}*/
		for(j = 2;j<=10;++j){
			if((ans[j] <= 1000000 && prime[ans[j]] == 0)){
                check = 0;
                break;
			}
			else if( ans[j] > 1000000){
				int parity = 1;
                for(k=2;k*k<=ans[j];++k){
                	if(ans[j]%k==0){
                		parity = 0;
                		break;
                	}
                }
                if(parity){
                	check = 0;
                	break;
                }
                				
			}
		}	
		if(check){

			
			cout << str << ' ';
			for(j = 2;j<=10;++j){
				k = 0;
				while(k<prime2.size() && ans[j]%prime2[k] != 0) ++k;
				cout   << prime2[k] << ' ';
			}
			cout << '\n';
			//cout << "Ended\n";
			++t;
		}
		/*if(check == 0){
			cout << i << ' ';
			for(j = 2;j<=10;++j){
				cout << ans2[j] << ' ';
			}
			cout << '\n';
			++t;
		}*/
	}
    return 0;
}
