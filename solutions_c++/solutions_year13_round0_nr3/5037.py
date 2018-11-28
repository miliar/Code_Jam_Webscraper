#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<vector>
#include<iterator>
using namespace std;

inline int scan() {
    int p=0;
    char c;
    c=getchar_unlocked();
    while(c<'0' || c>'9')
        c=getchar_unlocked();
    while(c>='0' && c<='9'){
        p=(p<<3)+(p<<1)+c-'0';
        c=getchar_unlocked();
    }
    return p;
}

int main() {
	int test;
	test = scan();
	for(int t = 0; t<test; t++) {
		int arr[5] = {1, 4, 9, 121, 484};
		int a, b;
		a = scan(); b = scan();
		int count = 0;
		for(int i=0; i<5; i++) {
			if(arr[i]>=a && arr[i]<=b)
				count++;
		}
		cout<<"Case #"<<t+1<<": "<<count<<endl;
	}
	return 0;
}
