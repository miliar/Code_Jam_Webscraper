#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

double her[1004], his[1004], her_c[1004], his_c[1004];

bool cmp_small(const double &a, const double &b){
	return a < b;
}

bool cmp_big(const double &a, const double &b){
	return a > b;
}

int Honest(double her[1004], double his[1004], int n){
	
		int ans, i, j;
		
		sort(her, her+n, cmp_small);
		sort(his, his+n, cmp_small);
		ans = 0;
		
		for(i = 0; i < n; i++){
			
			for(j = 0; j < n; j++){
				
				if(his[j] > her[i]){
					his[j] = -1;
					break;
				}
			}
			
			if(j == n)
			    ans++;
		}
		
		return ans;
	
}

int Cheat(double her[1004], double his[1004], int n){
	
	int ans, i, j, s, e;
	
	sort(her, her+n, cmp_small);
	sort(his, his+n, cmp_big);
	
//		for(int i = 0; i < n; i++)
//		    printf("%.5lf ", her[i]);
//		cout << endl;
//		
//		for(int i = 0; i < n; i++)
//		    printf("%.5lf ", his[i]);
//		cout << endl;
	
	ans = 0;
	for(i = 0; i < n; i++){
		
		s = -1; e = -1;
		
		for(j = 0; j < n; j++){
			
			if(his[j] != -1)
			{
				s = j;
				break;
			}
		}
		
		for(j = n-1; j > -1; j--){
			if(his[j] != -1){
				e = j;
				break;
			}
		}
		
//		cout << s << " " << e << endl;

		if(s == e){

			if(her[i] > his[s])
			    ans++;
			break;
		}
		
		if(her[i] > his[e]){
			ans ++;
			his[e] = -1;
		}
		else{
			his[s] = -1;
		}
	}
	
	return ans;
}

int main(){
	
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int t, no, n;
	int cheat, honest;
	scanf("%d", &t);
	
	for(int no = 1; no <= t; no++){
		
		scanf("%d", &n);
		
		for(int i = 0; i < n; i++)
		{
			scanf("%lf", &her[i]);
			her_c[i] = her[i];
		}
			
			
		for(int i = 0; i < n; i++)
		{
			scanf("%lf", &his[i]);
			his_c[i] = his[i];
		}
			
		
//		for(int i = 0; i < n; i++)
//		    printf("%.5lf ", her[i]);
//		cout << endl;
//		
//		for(int i = 0; i < n; i++)
//		    printf("%.5lf ", his[i]);
//		cout << endl;
		
		cheat = 0;
		honest = 0;
		
		honest = Honest(her, his, n);
		cheat = Cheat(her_c, his_c, n);
		
		printf("Case #%d: %d %d\n", no, cheat, honest);

		
	}
	return 0;
}
