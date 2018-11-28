#include<bits/stdc++.h>
using namespace std;

#define st_clk double st=clock();
#define end_clk double en=clock();
#define show_time cout<<"\tTIME="<<(en-st)/CLOCKS_PER_SEC<<endl;


#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);

int main(){
	 #ifndef ONLINE_JUDGE
     f_in("in");
     f_out("out");
     #endif
     int t,case1 = 0;
     scanf("%d",&t);
     while(t--){
     	case1++;
        int a;
        scanf("%d",&a); a--;
        int a1[5][5],a2[5][5];
		for(int i=0;i<4;i++){
		   for(int j=0;j<4;j++) scanf("%d",&a1[i][j]);
		}
		int b;
        scanf("%d",&b); b--;
		for(int i=0;i<4;i++){
		   for(int j=0;j<4;j++) scanf("%d",&a2[i][j]);
		}
		vector<int> ans;
		for(int i=0;i<4;i++){
		   for(int j=0;j<4;j++){
		      if(a1[a][i]==a2[b][j]) ans.push_back(a1[a][i]);
		   }
		}
		if(ans.size()==0) cout << "Case #" << case1 << ": Volunteer cheated!" << endl;
		else if(ans.size() >1 ) cout << "Case #" << case1 << ": Bad magician!" << endl;
		else cout << "Case #" << case1 << ": " << ans[0] << endl;;
	 }
}

