#include<iostream>
#include<cstring> 
using namespace std;
int main(){
	int t;
	cin >> t;
	bool v[17];
	for (int ti=0;ti<t;ti++){
		int r,tmp,cnt=0,ans;
		memset(v,false,sizeof(v));
		cin >> r;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++){
				cin >> tmp;
				if (i+1==r)
					v[tmp]=true;
			}
		cin >> r;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++){
				cin >> tmp;
				if (i+1==r)
					if (v[tmp]){
						cnt++;
						ans=tmp;
					}
			}
		cout << "Case #" << ti+1 << ": "; 
		if (cnt==0)
			cout << "Volunteer cheated!" << endl;
		else if (cnt==1)
			cout << ans << endl;
		else
			cout << "Bad magician!" << endl;
	}
	return 0;
}

