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
#define MX 1000002
#define MOD 100000001
#define BASE 5.0

#include <time.h>
#include <stdlib.h>
using namespace std;

char cake[102];

void cakereverse(int pos){
	reverse(cake, cake+pos);
	for (int i = 0; i<pos; i++)
		if (cake[i] == '-')
			cake[i] = '+';
		else cake[i] = '-';
}
int main(){
	ios_base::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    int t;
    
    cin >> t;
    for (int icase = 1; icase <=t; icase++){
    	cin >> cake;
    	int len = strlen(cake);
    	int stepcount = 0;
    	while (1){
    		int l = 0; 
    		while (cake[l] == '+')
    			l++;
    		if (l == len){
    			cout << "Case #" << icase << ": " << stepcount << "\n";
    			break;
    		}
    		if (l > 0){
    			cakereverse(l);
    			stepcount++;
    		}
    		int r = len-1;
    		while (cake[r] == '+')
    			r--;
    		r++;
    		cakereverse(r);
    		stepcount++;
    	}
    }
    return 0;
}