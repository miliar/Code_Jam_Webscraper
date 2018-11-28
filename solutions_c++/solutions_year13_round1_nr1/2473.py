#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

void runCase()
{
    long long r,t;
    cin >> r >> t;
    int a,x=r,y=r+1;
    int res = 0;
    while(1) {
        a = y*y-x*x;
        if(t>=a) t-=a;
        else break;
        res++;
        x+=2; y+=2;
    }
    cout << res << endl;
}

void runSample()
{
	string input;

	char buf[501] = {0};
	cin.getline(buf,501);

	input = buf;


	printf("%s\n",input.c_str());
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();

	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
		//runSample();
	}
}

int main()
{
	solve();
	return 0;
}
