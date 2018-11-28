#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define si(X) scanf("%d", &(X))
#define sll(X) scanf("%lld",&(X))
#define INFL 0x3f3f3f3f3f3f3f3fLL
ll gcd(ll a,ll b){
	if(b==0)
	return a;
	return gcd(b,a%b);
}
string toBin(ll a) {
	string res = "";
	while (a) {
		res += char((a & 1) + '0');
		a >>= 1;
	}
	reverse(res.begin(), res.end());
	return res;
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

int main(){

	int t;
	si(t);

	for(int alp = 1;alp<=t;alp++){
		int ans = 0;
        int arr[30];
        memset(arr,0,sizeof(arr));

        string str;
        cin>>str;
        int len = str.length();

        for(int i = 0;i<len;i++){
            arr[str[i]-'A'+1]++;
        }

        int fin[11];
        memset(fin,0,sizeof(fin));

        for(int i = 1;i<=26;i++){
            if(arr[i]>0){
                if(i==7){
                    int we = arr[i];
                    arr[5]-=we;
                    arr[9]-=we;
                    arr[7]-=we;
                    arr[8]-=we;
                    arr[20]-=we;
                    fin[8]+=we;
                }
                if(i==21){   //four
                    int we = arr[i];
                    arr[6]-=we;
                    arr[15]-=we;
                    arr[21]-=we;
                    arr[18]-=we;
                    fin[4]+=we;
                }
                if(i==24){
                    int we = arr[i];
                    arr[19]-=we;
                    arr[9]-=we;
                    arr[24]-=we;
                    fin[6]+=we;
                }
                if(i==23){
                    int we = arr[i];
                    arr[20]-=we;
                    arr[23]-=we;
                    arr[15]-=we;
                    fin[2]+=we;
                }
                if(i==26){
                    int we = arr[i];
                    arr[15]-=we;
                    arr[14]-=we;
                    arr[5]-=we;
                    fin[0]+=we;
                }
            }
        }

        for(int i = 1;i<=26;i++){
            if(arr[i]>0){
                if(i==15){//one
                    int we = arr[i];
                    arr[15]-=we;
                    arr[14]-=we;
                    arr[5]-=we;
                    fin[1]+=we;
                }
                if(i==20){ // three
                    int we = arr[i];
                    arr[20]-=we;
                    arr[8]-=we;
                    arr[18]-=we;
                    arr[5]-=(2*we);
                    fin[3]+=we;
                }
                if(i==6){ //five
                    int we = arr[i];
                    arr[6]-=we;
                    arr[9]-=we;
                    arr[22]-=we;
                    arr[5]-=we;
                    fin[5]+=we;
                }
                if(i==19){ //seven
                    int we = arr[i];
                    arr[19]-=we;
                    arr[5]-=we;
                    arr[22]-=we;
                    arr[5]-=we;
                    arr[14]-=we;
                    fin[7]+=we;
                }
                if(i==9){  //nine
                    int we = arr[i];
                    arr[14]-=we;
                    arr[14]-=we;
                    arr[9]-=we;
                    arr[5]-=we;

                    fin[9]+=we;
                }
            }
        }

        cout<<"Case #"<<alp<<": ";
        for(int i = 0;i<10;i++){
            int w = fin[i];
            while(w>0){
                cout<<i;
                w--;
            }
        }
        cout<<endl;











		//cout<<"Case #"<<alp<<": "<<ans<<endl;

	}











}























