#include <iostream>

using namespace std;
int main() {
	int n;
	cin >> n;
	for(int x=0;x<n;x++){
	string t;
	cin >> t;	
	cout<<"Case #"<<(x+1)<<": ";
	string z = string(1,t[0]);
	for(int xx=1;xx<strlen(t.c_str());xx++){
	if(t[xx]>=z[0]){
	z = t[xx]+z;
}else{
	z= z+t[xx];
}
}
cout<<z<<endl;	
}
}

