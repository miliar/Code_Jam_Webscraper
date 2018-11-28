#include<bits/stdc++.h>
#define gc getchar//_unlocked
#define pc putchar//_unlocked
#define sz(a) int((a).size())
#define pb push_back
#define pob pop_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
#define SWAP(x,y) x^=y^=x^=y
#define MOD 1000000009
#define ll long long
//memset(bit1,0,sizeof bit1);
using namespace std;
inline long long readInt(){
long long n = 0, c = gc(), f = 1;
while(c != '-' && (c < '0' || c > '9')) c = gc();
if(c == '-') f = -1, c = gc();
while(c >= '0' && c <= '9')
n = (n<<3) + (n<<1) + c - '0', c = gc();
return n * f;
}

inline void writeInt(long long a)
{
    char snum[20];
    int i=0;
    do  {
        snum[i++]=a%10+48;
        a=a/10;
    }while(a!=0);
    i=i-1;
    while(i>=0)
    pc(snum[i--]);
    pc('\n');
}

int main(){
//	f_in("in.txt");
//	f_out("out.txt");
	int t;
	cin>>t;
	for(int z = 1 ; z <=t ; z++){
		int n;
		cin>>n;		
		int arr[1005] = {0};
		
		for(int i=0;i<1005;i++){
			arr[i] = 0;
		}
		for(int i=0;i<n;i++){
			int q;
			cin>>q;
			arr[q]++;
		}
		long long minutes = 0;
		long long min = 100000;
		long long max = 1000;
		long long iter = 100000;// max iterations to make
		while(iter--){
			for(int i=max;i>0;i--){
				if(arr[i]>0){
					max = i;
					break;
				}
			}
			
			long long ans = minutes + max;
			if(ans < min){
				min = ans;												
			}			
			if(max==1) break;
			
			int p1 = max/2 ;
			int p2 = max - p1;
			arr[p1] += arr[max];
			arr[p2] += arr[max];
			minutes = minutes + arr[max];
			arr[max] = 0;
		}
		
		cout<<"Case #"<<z<<": "<<min<<endl;		
	}
	return 0;
}

