#include <iostream>
#include <fstream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#include <stack>
#include <queue>
#include <set>
#include<utility>
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a>b?b:a


typedef long long int ll;
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	int test;
	cin>>test;
	int qw  = 1;
	while(test--){
        int s;
        int count = 0,cur = 0;
        cin>>s;
        string arr;
        cin>>arr;
        cur = arr[0] - '0';
        for(int i = 1 ; i<=s ; ++i){
           // cout<<cur<<" "<<count<<" "<<arr[i]<<endl;
            if(arr[i] == '0')
                continue;
            if(cur < i){
                count += (i-cur);
            }
            cur += ((arr[i]-'0')+count);
        }
        cout<<"Case #"<<qw<<": "<<count<<endl;
        ++qw;

	}
}
