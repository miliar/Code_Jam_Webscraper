#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<iostream>
#include<string.h>
#include<limits.h>
#include<functional>
#include<vector>
#include<utility>
#include<stdlib.h>
#include<time.h>
using namespace std;

#define mem(a) memset(a,0,sizeof(a))
int a[11];

bool update(long long int n) {
	while(n>0) {
		int k = n%10;
		a[k] = 1;
		n/=10;
	}
	for(int i=0;i<10;i++){
		if(a[i]==0){
			return false;
		}
	}
	return true;
}

int main() {
	// your code goes here
	long long tc;
	cin>>tc;
	long long int n;
	for(int c=1;c<=tc;c++) {
		string s;
		cin>>s;
		int ans[15] = {0};
		int len = s.length();
		int arr[300] = {0};
		for(int i=0;i<len;i++) {
            arr[s[i]]++;
		}
		if(arr['Z']>0){
            ans[0] = arr['Z'];
            arr['E'] -= arr['Z'];
            arr['R'] -= arr['Z'];
            arr['O'] -= arr['Z'];
            arr['Z'] = 0;
		}
		if(arr['W']>0){
            ans[2] = arr['W'];
            arr['T'] -= arr['W'];
            arr['O'] -= arr['W'];
            arr['W'] = 0;
		}
		if(arr['U']>0){
            ans[4] = arr['U'];
            arr['F'] -= arr['U'];
            arr['O'] -= arr['U'];
            arr['R'] -= arr['U'];
            arr['U'] = 0;
		}
		if(arr['X']>0){
            ans[6] = arr['X'];
            arr['S'] -= arr['X'];
            arr['I'] -= arr['X'];
            arr['X'] = 0;
		}
		if(arr['G']>0){
            ans[8] = arr['G'];
            arr['E'] -= arr['G'];
            arr['I'] -= arr['G'];
            arr['H'] -= arr['G'];
            arr['T'] -= arr['G'];
            arr['G'] = 0;
		}
		if(arr['O']>0){
            ans[1] = arr['O'];
            arr['N'] -= arr['O'];
            arr['E'] -= arr['O'];
            arr['O'] = 0;
		}
		if(arr['T']>0){
            ans[3] = arr['T'];
            arr['H'] -= arr['T'];
            arr['R'] -= arr['T'];
            arr['E'] -= 2*arr['T'];
            arr['T'] = 0;
		}
		if(arr['S']>0){
            ans[7] = arr['S'];
            arr['E'] -= 2*arr['S'];
            arr['V'] -= arr['S'];
            arr['N'] -= arr['S'];
            arr['S'] = 0;
		}
		if(arr['F']>0){
            ans[5] = arr['F'];
            arr['I'] -= arr['F'];
            arr['V'] -= arr['F'];
            arr['E'] -= arr['F'];
            arr['F'] = 0;
		}
		ans[9] = arr['I'];





		cout<<"Case #"<<c<<": ";
		for(int i=0;i<10;i++) {
            while(ans[i]>0){
                cout<<i;
                ans[i]--;
            }
		}
		cout<<endl;

	}
	return 0;
}
