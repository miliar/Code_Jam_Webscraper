#include <vector>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

char _buffer[2048];

#define FILE_NAME "A"
#define LL long long
#define ULL unsigned long long
#define CASET int _t=0, case_num;cin>>case_num;while(++_t<=case_num)

typedef vector<int> VI;
typedef vector<VI> VVI;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
char dir[4] = {'E', 'S', 'W', 'N'};

bool solve()
{
	return false;
}	

int main()
{
	sprintf(_buffer, "%s.in", FILE_NAME);
	freopen(_buffer, "r", stdin);
	sprintf(_buffer, "%s.out", FILE_NAME);
	freopen(_buffer, "w", stdout);

	CASET
	{
		int N, ans;
		cin>>N;
		VI flag(10, 1);
		int cnt = 10;
		if(N){
			for(int i=1;;i++){
				LL t = N*i;
				ans = t;
				while(t){
					int digit = t%10;
					if(flag[digit]){
						flag[digit]=0;
						cnt--;
					}
					t/=10;
				}
				if(cnt<=0)
					break;
			}
		}else
			ans = 0;
		
		cout<<"Case #"<<_t<<": ";
		if(ans)
			cout<<ans;
		else
			cout<<"INSOMNIA";
		cout<<endl;
	}
		
	return 0;
}