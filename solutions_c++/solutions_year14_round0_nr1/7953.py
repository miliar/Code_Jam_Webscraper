#include <iostream>

using namespace std;

int check(int f1, int f2, int f3, int f4, int g1, int g2, int g3, int g4){
	int ans = -1;
	if(f1==g1 || f1==g2 || f1==g3 || f1==g4){
		ans = f1;
	}
	if(f2==g1 || f2==g2 || f2==g3 || f2==g4){
		if(ans == -1) ans = f2;
		else ans = -2;
	}
	if(f3==g1 || f3==g2 || f3==g3 || f3==g4){
		if(ans == -1) ans = f3;
		else ans = -2;
	}
	if(f4==g1 || f4==g2 || f4==g3 || f4==g4){
		if(ans == -1) ans = f4;
		else ans = -2;
	}
	return ans;
}

int main(int argc, char const *argv[])
{
	int n;
	cin>>n;
	for(int i=1; i<=n; i++){
		int a1;
		int t, f1, f2, f3, f4;
		cin>>a1;
		if(a1==1){
			cin>>f1>>f2>>f3>>f4;
		}
		else{
			cin>>t>>t>>t>>t;
		}
		if(a1==2){
			cin>>f1>>f2>>f3>>f4;
		}
		else{
			cin>>t>>t>>t>>t;
		}
		if(a1==3){
			cin>>f1>>f2>>f3>>f4;
		}
		else{
			cin>>t>>t>>t>>t;
		}
		if(a1==4){
			cin>>f1>>f2>>f3>>f4;
		}
		else{
			cin>>t>>t>>t>>t;
		}
		int a2;
		int g1, g2, g3, g4;
		cin>>a2;
		if(a2==1){
			cin>>g1>>g2>>g3>>g4;
		}
		else{
			cin>>t>>t>>t>>t;
		}
		if(a2==2){
			cin>>g1>>g2>>g3>>g4;
		}
		else{
			cin>>t>>t>>t>>t;
		}
		if(a2==3){
			cin>>g1>>g2>>g3>>g4;
		}
		else{
			cin>>t>>t>>t>>t;
		}
		if(a2==4){
			cin>>g1>>g2>>g3>>g4;
		}
		else{
			cin>>t>>t>>t>>t;
		}
		int ans = check(f1, f2, f3, f4, g1, g2, g3, g4);
		cout<<"Case #"<<i<<": ";
		if(ans == -1){
			cout<<"Volunteer cheated!\n";
		}
		else if (ans == -2){
			cout<<"Bad magician!\n";
		}
		else{
			cout<<ans<<endl;
		}
	}
	return 0;
}