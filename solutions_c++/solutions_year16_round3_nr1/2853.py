#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <limits.h>
#include <map>
//#define max 100002

#include <time.h>
#include <stdlib.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    int t, n;
    int tb[26];
    cin >> t;
    for (int icase = 1; icase <=t; icase++){
    	for (int i = 0; i<26; i++)
    		tb[i] = 0;
    	cin >> n;
    	int mx1 = 0, mx2 = 1;
    	cin >> tb[0];
    	cin >> tb[1];
    	if (tb[mx1] < tb[mx2])
    		swap(mx1, mx2);
    	for (int i = 2; i<n; i++){
    		cin >> tb[i];
    		if (tb[i] > tb[mx1]){
    			mx2 = mx1;
    			mx1 = i;
    		}
    		else if (tb[i] > tb[mx2])
    			mx2 = i;
    	}
    	//cout << mx1 << mx2 << endl;
    	cout << "Case #" << icase << ": ";
    	if (tb[mx1] - tb[mx2] == 2){
    		cout << (char)(mx1 + 'A') << (char)(mx1 + 'A') << " ";
    		tb[mx1]-=2;
    	}
    	else if (tb[mx1] - tb[mx2] == 1){
    		cout << (char)(mx1 + 'A') << " ";
    		tb[mx1]--;
    	}
    	for (int i = 0; i<26; i++){
    		if (tb[i] > 0 && i != mx1 && i != mx2){
    			while (tb[i] > 0){
    				cout << (char)(i+'A') << " ";
    				tb[i]--;
    			}
    		}
    	}
    	//cout << mx1 << mx2 << endl;
    	//cout << tb[mx1] << endl;
    	while (tb[mx1] > 0){
    		cout << (char)(mx1 + 'A') << (char)(mx2 + 'A') << " ";
    		tb[mx1]--;
    	}
    	cout << endl;
    }
    return 0;
}