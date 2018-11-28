#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <climits>


using namespace std;


int main(){
	freopen("/Users/Arseniy/All/A/input.txt", "r", stdin);
    freopen("/Users/Arseniy/All/A/output.txt", "w", stdout);
    int c,d,v,t;
    cin >> t;
    int a[100];
	int can[1000];
    for (int o=0;o<t;o++){
    	cout << "Case #" << o+1 << ": ";
    	cin >> c >> d >> v;
    	for (int i=0;i<d;i++)
    		cin >> a[i];
    	if (c != 1){
    		cout << endl;
    		continue;
    	}
    	for (int i=0;i<=v;i++)
    		can[i] = false;
    	can[0] = 1;
    	for (int i=0;i<d;i++){
    		if (a[i] <= v)
    			can[a[i]] = 1;
    	}
    	vector <int> b;
    	b.clear();
    	for (int i=1;i<=v;i++)
    		if (!can[i]) 
    			b.push_back(i);	
    	vector <int> y;
    	y.clear();
    	for (int i=1;i<(1 << d);i++){
    		int s = 0;
    		for (int j=0;j<d;j++){
    			if ((i >> j) & (1))
    				s += a[j];
    		}
    		if (s <= v){
    			can[s] = true;
    			y.push_back(s);
    		}
    	}
    	bool f = true;
    	for (int i=0;i<=v;i++)
    		if (!can[i])
    			f = false;
    	if (f){
    		cout << 0 << endl;
    		continue;
    	}
    	int ans = 0;
    	for (int i=0;i<=v;i++){
    		if (!can[i]){
    			ans++;
    			for (int j=v;j>=0;j--)
    				if ((can[j]) && (j + i <= v))
    					can[j+i] = true;
    		}
    	}
    	cout << ans << endl;
    }
	return 0;
}