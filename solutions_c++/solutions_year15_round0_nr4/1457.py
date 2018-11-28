#include <bits/stdc++.h>
using namespace std;
int main(){
int T;cin >>T;
for(int Case=1;Case<=T;Case++){
	int X,R,C;cin >> X >> R >>C;
	if(R<C)swap(R,C);
	bool ans=true;
	if((R*C)%X)ans=false;
	if(X>=2*C+1)ans=false;//L shaped longer than C
	if(X>R)ans=false;//I shaped, longer than long edge.
	if(X>=7)ans=false;
	if(X==4 && C==2)ans=false;
	if(X==6 && C==3)ans==false;
	printf("Case #%d: %s\n",Case,(ans?"GABRIEL":"RICHARD"));


}
}
