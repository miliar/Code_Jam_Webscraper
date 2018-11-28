#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
char ans[1000*1000], temp[1000*1000], final[1000*1000], temp1[1000*1000], temp2[1000*1000];
int main() {
	int t, c = 1;
	cin>>t;
	while(t--) {
		
	    bool flag = false;
		int n,r,p,s;
		cin>>n>>r>>p>>s;
		int l;
		char o[100] = {'E','P','S','R'};
		final [0] = 'Z';
		printf("Case #%d: ",c++);
		
		for(int e = 1; e<=3;e++) {
			l = 1;
		    ans[0] = o[e]; 
		    
			for(int i=0;i<n;i++) {
				for(int j=0;j<l;j++) {
					if(ans[j] == 'R') {
					temp[2*j] = 'R';
					temp[2*j + 1] = 'S';
	 			   }
	 				else if(ans[j] == 'S') {
					temp[2*j] = 'P';
					temp[2*j + 1] = 'S';
	 				}
	 				else if(ans[j] == 'P') {
					temp[2*j] = 'P';
					temp[2*j + 1] = 'R';
	 				}
				}
	     	    l = 2*l;  
	     	    //cout<<e<<" "<<l<<" "<<ans<<" "<<temp<<"\n";
				for(int j=0;j<l;j++) ans[j] = temp[j];
				ans[l]='\0';
				//cout<<e<<" "<<l<<" " <<ans<<" "<<temp<<"\n";

			}
			//cout<<e<<" "<<l<<"\n";
			int r1=0,p1=0,s1=0;
			for(int i=0;i<l;i++) {
				if(ans[i]=='R') r1++;
				if(ans[i]=='P') p1++;
				if(ans[i]=='S') s1++;
			}
			//cout<<e<<" "<<r1<<" "<<p1<<" "<<s1<<"\n";
			if(r==r1 && p==p1 && s==s1) {
				
				
				if(strcmp(final,ans) > 0)
				   strcpy(final, ans);
				
				flag = true;
//				break;//
			}
		}
		if(!flag) cout<<"IMPOSSIBLE\n";
		//else cout<<final<<"\n";
		
		for(int j=2;j<l;j=j*2) {
			for(int i = 0; i<l/2;i+=j) {
				for(int k=0;k<j;k++) {
					temp1[k] = final[i*2+k];
				}
				temp1[j]='\0';
				for(int k=0;k<j;k++) {
					temp2[k] = final[i*2+k+j];
				}
				temp2[j]='\0';
				if(strcmp(temp1,temp2) > 0) {
					//cout<<i<<" "<<j<<" "<<temp1<<" "<<temp2<<" changing\n";
					for(int k=0;k<j;k++) {
					   final[i*2+k+j] = temp1[k];
				    }
				    for(int k=0;k<j;k++) {
					   final[i*2+k] = temp2[k];
				    }
				}
				//cout<<i<<" "<<j<<" "<<temp1<<" "<<temp2<<"\n";
			}
		}
		if(flag)
		cout<<final<<"\n";
	}
}
