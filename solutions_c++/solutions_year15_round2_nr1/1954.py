#include<bits/stdc++.h>
using namespace std;
#define sd(x) 						scanf("%d", &x)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
#define      fill(a)           memset(a, 0, sizeof (a))
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define MOD 1000000007
#define D double
#define LD long double
typedef long long int LL;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<LL> vl;
typedef vector< vector<int> > vii;
typedef vector< vector<LL> > vll;
ifstream fin;        ofstream fout;

LL reverse(LL num){
	LL rev_num = 0;
    while(num > 0)
    {
        rev_num = rev_num*10 + num%10;
        num = num/10;
    }
    return rev_num;
}
LL inp_arr[5000001];
int main(int argc, char *argv[])
{
	if(argc == 3){
		cout<<"Insied";fin.open(argv[1]);fout.open(argv[2]);}
	LL tc;
	fin>>tc;
	cout<<tc;
	inp_arr[11] = 11;
	cout<<reverse(345);
	cout<<reverse(100);
	for(int i = 12;i < 1000005;i++){
		if(inp_arr[i] == 0)
			inp_arr[i] = inp_arr[i - 1] + 1;
		else 
			inp_arr[i] = min(inp_arr[i],inp_arr[i - 1] + 1);
		LL temp = reverse(i);
		if(temp <= 1000000 && inp_arr[temp] > 0 && temp >= 12)
			inp_arr[temp] = min(inp_arr[i] + 1,inp_arr[temp]);
		
		else if(temp <= 1000000 && temp >= 12)
			inp_arr[temp] = inp_arr[i] + 1;
	}
	for(int i = 1;i <= tc;i++){
		LL n;
		fin>>n;
		if(n <= 11)
			fout<<"Case #"<<i<<": "<<n<<endl;
		else
			fout<<"Case #"<<i<<": "<<inp_arr[n]<<endl;
	}
}