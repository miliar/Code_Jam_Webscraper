#include <iostream>
using namespace std;

int main() {
	int t,i,j,k,n1,n2,a1[4],a2[4],n,p,t1,l=1;
	cin>>t;
	while(t--){
		cin>>n1;
		n1--;
		k=0;j=0;
		for(i=0;i<16;i++){
			if(i>=(n1*4)&&i<(n1+1)*4)
			cin>>a1[j++];
			else
			cin>>p;
		}
		cin>>n2;
		n2--;
		t1=0;
		for(i=0;i<16;i++){
           	if(i>=(n2*4)&&i<(n2+1)*4){
				cin>>a2[t1++];
                }
                else
                cin>>p;
			}
            for(i=0;i<4;i++)
            for(j=0;j<4;j++){
				if(a1[j]==a2[i]){
					k++;
					n=a2[i];
				}
			}
		if(k==0)
			cout<<"Case #"<<l++<<": "<<"Volunteer cheated!"<<endl;
			else if(k>1)
			cout<<"Case #"<<l++<<": "<<"Bad magician!"<<endl;
			else
			cout<<"Case #"<<l++<<": "<<n<<endl;
	}
	return 0;
}