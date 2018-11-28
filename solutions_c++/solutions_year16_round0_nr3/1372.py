#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ull unsigned long long
#define si(X) scanf("%d", &(X))
#define sll(X) scanf("%lld",&(X))
ll gcd(ll a,ll b){
	if(b==0)
	return a;
	return gcd(b,a%b);
}
const int mod = 1e9+7;
ll expo(ll base,ll pow){
    ll ans = 1;
    
    while(pow!=0){
        if(pow&1==1){
            ans = ans*base;
            ans = ans%mod;
        }
        base *= base;
        base%=mod;
        pow/=2;
        
    }
    return ans;
}
double pi = 3.141592653589793238462643;
double error = 0.0000001;
/* -------Template ends here-------- */ 

const int M = 100001;

bool isP(ull num){
	for(ull i = 2;i*i<=num;i++){
		//cout<<"p p "<<num<<"    "<<i<<endl;
		if(num%i==0){
			return false;
		}
	}
	return true;
}

ull creat(string str,int bas){
	ull num = 0;
	int len = str.length();
	for(int i = len-1;i>=0;i--){
		ull pro = 1;
		int act = len-1-i;
		//cout<<i<<"    "<<act<<endl;
		if(str[i]=='0')
		continue;
		
		for(int j = 0;j<act;j++){
			pro*=bas;
			//cout<<"pro "<<pro<<endl;
		}
		num+=pro;
		//cout<<"num is "<<num<<endl;
	}
	return num;
	//cout<<"final "<<num<<endl;
}

bool check(string str,int bas){
	ull num = creat(str,bas);
	//if(num<10000000)
	//cout<<" num is < "<<num<<endl;
	if(isP(num)){
	//	cout<<bas<<"  is prime"<<endl;
		return false;
	}
	//cout<<"chosen  "<<num<<endl;
//	cout<<bas<<"  not prime "<<endl;
	return true;	
}
int er = 0;
void eval(string str){
	cout<<str<<" ";
	for(int bas = 2;bas<=10;bas++){
		ull num = creat(str,bas);
	//	cout<<"the num is "<<num<<endl;
		for(ull i = 2;i<=num;i++){
			if(num%i==0){
				cout<<i<<" ";
				break;
			}
		}
	}	
	cout<<endl;
}

int yu = 0;
void rec(string str,int tot){
	if(yu==50)
	return;
	//cout<<"here "<<str<<"   "<<yu<<endl;
	int len = str.length();
	if(len>tot)
	return;
	
	if(len==tot){
		int o = 0;
		string str2 = "1"+str+"1";
		//cout<<endl<<endl<<"act st "<<str2<<endl;
		for(int i = 2;i<=10;i++){
			if(!check(str2,i)){       // check if any is prime
				o++;
				break;
			}
		}
		if(o==0){
			eval(str2);
			//cout<<"ok it is "<<str2<<endl;
			//cout<<endl;
			yu++;
		}
		return;
	}
	
	else{
		str = str+"0";
		rec(str,tot);
		
		str = str+"1";
		rec(str,tot);
	}

}


int main(){
	
	int t;
	si(t);
	
	for(int alp = 1;alp<=t;alp++){
		int ans = 0;
		
		int n,j;
		si(n);
		si(j);
		
		string a = "";
		int tot_len = n-2;
		cout<<"Case #"<<alp<<": "<<endl;
		if(n==16){
			rec(a,tot_len);                   // string,presentLength,totalpermissible length
		}
		else{
			//rec2(a,0,tot_len,0);
		}
				
	}
	
	
	
}


