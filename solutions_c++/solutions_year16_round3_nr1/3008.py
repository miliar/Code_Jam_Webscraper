#include <vector>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <iostream>
#include <string>
#include <cstdio>
#include <sstream>

using namespace std;

char _buffer[2048];

#define FILE_NAME "A"
#define LL long long
#define ULL unsigned long long
#define CASET int _t=0, case_num;cin>>case_num;while(++_t<=case_num)

typedef vector<int> VI;
typedef vector<VI> VVI;

typedef struct data{
	char sym;
	int val;
}d;

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
char dir[4] = {'E', 'S', 'W', 'N'};

bool solve()
{
	return false;
}	

int cmp(const data a, const data b){
	return a.val >= b.val;
}

int main()
{
	sprintf(_buffer, "%s.in", FILE_NAME);
	freopen(_buffer, "r", stdin);
	sprintf(_buffer, "%s.out", FILE_NAME);
	freopen(_buffer, "w", stdout);

	CASET
	{
		int N, num, sum=0;
		cin>>N;
		vector< data > arr;
		for(int i=0;i<N;i++){
			cin>>num;
			data d;
			d.sym = 'A'+i;
			d.val = num;
			arr.push_back(d);
			sum+=num;
			// cout<<' '<<num;
		}
		// cout<<endl;
		cout<<"Case #"<<_t<<":";
		int cnt = 0;
		while(sum){
			sort(arr.begin(), arr.end(), cmp);
			if(arr[0].val==1){
				if(sum==2){
					sum-=2;
					cout<<' '<<arr[0].sym<<arr[1].sym;
				}else{
					sum-=1;
					arr[0].val-=1;
					cout<<' '<<arr[0].sym;
				}
			}else if(arr[1].val<=(sum-2)/2){
				arr[0].val-=2;
				sum-=2;
				cout<<' '<<arr[0].sym<<arr[0].sym;
			}else if((arr[1].val-1)<=(sum-1)/2){
				arr[0].val-=1;
				arr[1].val-=1;
				sum-=2;
				cout<<' '<<arr[0].sym<<arr[1].sym;
			}else{
				arr[0].val-=1;
				sum-=1;
				cout<<' '<<arr[0].sym;
			}
			// for(int i=0;i<N;i++){
				// cout<<endl<<arr[i].sym<<' '<<arr[i].val;
			// }
			// cout<<endl;
			// cnt++;
			// if(cnt==2)
				// break;
		}
		cout<<endl;
	}
		
	return 0;
}