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
	f_in("in.txt");
	f_out("out.txt");
	int t;
	t = readInt();
	for(int x = 1 ; x <= t ; x++){
		int n = readInt();
		char str[1001];
		cin>>str;
		int sPerson = 0 , rPerson = 0;
		for(int i=0;str[i]!='\0';i++){
			if(str[i] == '0')
				continue;
			if(sPerson >= i){
				sPerson += (str[i]-'0');
			}else{
				rPerson += (i - sPerson);
				sPerson += rPerson + (str[i]-'0');
			}
		}
		
		cout<<"Case #"<<x<<": "<<rPerson<<endl;
	}
	return 0;
}

