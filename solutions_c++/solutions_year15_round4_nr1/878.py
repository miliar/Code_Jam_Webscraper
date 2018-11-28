#include<iostream>
#include<algorithm>
#include<cstring>
#include <string>
#include<vector>
#include <queue>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int r,c;
char a[101][101];
int L[101], R[101], U[101], D[101];
bool walk(int i,int j, int cur, int cnt){
	if (i==r || j==c || i<0 || j<0) return false;
	if (cnt==r*c+1) return true;
	if (a[i][j]=='^') cur = 0;
	else if (a[i][j] == '>') cur = 1;
	else if (a[i][j] == 'v') cur = 2;
	else if (a[i][j] == '<') cur = 3;
	if (cur==0) return walk(i-1,j,cur,cnt+1);
	if (cur==1) return walk(i,j+1,cur,cnt+1);
	if (cur==2) return walk(i+1,j,cur,cnt+1);
	if (cur==3) return walk(i,j-1,cur,cnt+1);

}
const int hi[] = {0, 0, 1, -1};
const int hj[] = {1, -1, 0, 0};
const char sym[] = {'>', '<', 'v', '^'};
 

 

        
    
  
int main(){
   // freopen("input1.txt","r",stdin);
   //freopen("A-small-attempt1.in","r",stdin);
   freopen("A-large.in","r",stdin);
    freopen("output1.txt","w",stdout);
    
    int t;
    cin >> t;
	
    for(int ti=1;ti<=t;ti++){
		cout << "Case #"<<ti<<": ";
        cin>>r>>c;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cin>>a[i][j];
			}
		}
		/*int good = 0;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if (a[i][j]=='.') {
					good++;
					continue;
				}
				int cur;
				if (a[i][j]=='^') cur = 0;
				else if (a[i][j] == '>') cur = 1;
				else if (a[i][j] == 'v') cur = 2;
				else if (a[i][j] == '<') cur = 3;
				good += walk(i,j,cur,1);
			}
		}

		if (good==r*c) puts("0");
		else if (good+1==r*c) puts("IMPOSSIBLE");
		else cout << (r*c-good)/2 << "\n";*/
		/*for(int i = 0; i < r; i++)
            L[i] = c, R[i] = -1;
        for(int i = 0; i < c; i++)
            U[i] = r, D[i] = -1;
		for(int i = 0; i < r; i++){           
            for(int j = 0; j < c; j++)
				if(a[i][j] != '.'){
                L[i] = min(L[i], j);
                R[i] = max(R[i], j);
                U[j] = min(U[j], i);
                D[j] = max(D[j], i);
            }
        } 
        int ans = 0;
        bool ok = true; 
        for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(a[i][j] != '.'){                 
					bool f1 = (R[i] > j);
					bool f2 = (L[i] < j);
					bool f3 = (D[i] > i);
					bool f4 = (U[i] < i);
					if (!(f1|f2|f3|f4)) ok = false;
					else if (a[i][j]=='>' && !f1) ans++;
					else if (a[i][j]=='<' && !f2) ans++;
					else if (a[i][j]=='v' && !f3) ans++;
					else if (a[i][j]=='^' && !f4) ans++;
				}
			}
		}
		if (!ok) puts("IMPOSSIBLE");
		else cout << ans << "\n";*/
		int ans = 0;
        for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (a[i][j] == '.') continue;
				if (ans == -1) break;
				bool ok = false;
				bool ok2 = false;
				for (int k = 0; k < 4; k++) {
					bool ok3 = false;
					int ii = i + hi[k], jj = j + hj[k];
					while (ii >= 0 && ii < r && jj >= 0 && jj < c) {
						if (a[ii][jj] != '.') {
							ok3 = true;
							break;
						}
						ii += hi[k];
						jj += hj[k];
					}
					if (ok3) {
						ok2 = true;
						if (sym[k] == a[i][j]) ok = true;
					}
				}
				if (ok2) {
					if (!ok) ans++;
				}
				else ans = -1;
        }
        
        if (ans == -1) puts("IMPOSSIBLE");
        else cout << ans << "\n";
	}
	
    return 0;
}
