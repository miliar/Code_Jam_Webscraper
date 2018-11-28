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

/*bool walk(int i,int j, int cur, int cnt){
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

}*/

 

        
double C[101],R[101];
int n;
double X,V;    
  
int main(){
   // freopen("input1.txt","r",stdin);
   freopen("B-small-attempt0.in","r",stdin);
   //freopen("A-large.in","r",stdin);
    freopen("output1.txt","w",stdout);
    
    int t;
    cin >> t;
	
    for(int ti=1;ti<=t;ti++){
		cout << "Case #"<<ti<<": ";
        /*cin>>r>>c;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cin>>a[i][j];
			}
		}*/
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
		cin>>n>>V>>X;
		for(int i=0;i<n;i++) cin>>R[i]>>C[i];
		if (n==1){
			if (C[0]!=X) puts("IMPOSSIBLE");
			else{
				double tim = V*1.0/R[0];
				printf("%.7f\n",tim);
			}
		}
		else{
			if (C[0]<X && C[1]<X) puts("IMPOSSIBLE");
			else if (C[0]>X && C[1]>X) puts("IMPOSSIBLE");
			else if (C[0]==X && C[1]==X){
				double tim = V*1.0/(R[0]+R[1]);
				printf("%.7f\n",tim);
			}
			else if (C[0]==X){
				double tim = V*1.0/(R[0]);
				printf("%.7f\n",tim);
			}
			else if (C[1]==X){
				double tim = V*1.0/(R[1]);
				printf("%.7f\n",tim);
			}
			else{
				double tim = V*1.0/(R[0]+R[1]);
				if (tim * (C[0]*R[0]+C[1]*R[1]) == X*V*1.0) printf("%.7f\n",tim);
				else{
					//(R[0]+R[1])*t1 + R[1]*t2 = V
					//(C[0]*R[0]+C[1]*R[1])*t1 + C[1]*R[1]*t2 = V*X
					double t1 = (V*C[1]-V*X)*1.0/(R[0]*C[1]-C[0]*R[0]);
					double t2 = (V-(R[0]+R[1])*t1)/R[1];
					//(R[0]+R[1])*t3 + R[0]*t4 = V
					//(C[0]*R[0]+C[1]*R[1])*t3 + C[0]*R[0]*t4 = V*X
					double t3 = (V*C[0]-V*X)*1.0/(R[1]*C[0]-C[1]*R[1]);
					double t4 = (V-(R[0]+R[1])*t3)/R[0];
					double tim;
					if (t1<0 || t2<0) tim = t3+t4;
					else if (t3<0 || t4<0) tim = t1+t2;
					else tim = min(t1+t2,t3+t4);
					printf("%.7f\n",tim);
				}
			}
		}
	}
	
    return 0;
}
