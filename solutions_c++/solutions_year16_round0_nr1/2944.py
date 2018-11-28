//By Tapesh Joham
#include<bits/stdc++.h>
using namespace std;

#define SCAN(x) scanf("%d",&x)
#define SCAN2(x,y) scanf("%d%d",&x,&y)
#define PRI(x) printf("%d\n",x)
#define FOR(A,B,C) for(int A=B;A<C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))
#define mod 1000000007
#define gc getchar_unlocked
typedef long long int LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;

int main()
{
	int test,cnt=0;
	SCAN(test);
	while(test--){
        cnt++;
		LL n,ans;
		cin >> n;
		printf("Case #%d: ",cnt);
		if(n==0){
			printf("INSOMNIA\n");
			continue;
		}
		int it=1,arr[10]={0},check;
		while(it<1000000){
            check = 1;
            ans = it*n;
            stringstream convert;
            convert << ans;
            string a = convert.str();
            FOR(i,0,(int)a.length())
                arr[a[i]-'0']++;
            FOR(i,0,10){
                if(!arr[i]){
                    check=0;
                    break;
                }
            }
            if(check)
                break;
            it++;
        }
        cout << ans << endl;
	}
	return 0;
}
