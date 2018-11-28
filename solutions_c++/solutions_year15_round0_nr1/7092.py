#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int getChart(char t){
	if(t == '9') return 9;
	if(t == '8') return 8;
	if(t == '7') return 7;
	if(t == '6') return 6;
	if(t == '5') return 5;
	if(t == '4') return 4;
	if(t == '3') return 3;
	if(t == '2') return 2;
	if(t == '1') return 1;
	return 0;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    freopen("input.txt","r",stdin);
    freopen("Redownload A-small-attempt1.out","w",stdout);
    int t,n,m;
    cin>>t;
    for(int i = 1; i <= t; i++){
        cin>>n;
        int count = 0;
        int sum = 0;
        char t;
        cin>>t;
        sum = getChart(t);
        for(int j = 1; j <= n; j++){
        	cin>>t;
        	m = getChart(t);
        	if(m == 0) continue;
        	if(sum < j){
        		count += j - sum;
        		sum = j;
			}
			sum += m;
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
    }
    return 0;
}

