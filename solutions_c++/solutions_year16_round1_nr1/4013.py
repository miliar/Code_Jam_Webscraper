#include <bits/stdc++.h>
using namespace std;

int main(void)
{
	int t,k=1,i,j,che;
	string s;
	char fin[1000];
	cin>>t;
	while(t--){
        che=0;
		cin>>s;
		fin[0]=s[0];
		che++;
		for(i=1;i<s.length();i++){
			if(s[i]<fin[0]){
				fin[i]=s[i];
				che++;
			}
			else{
				for(j=che;j>0;j--){
					fin[j]=fin[j-1];
				}
				che++;
                fin[0]=s[i];
			}
		}
		cout<<"Case #"<<k<<": ";
		for(i=0;i<che;i++)
            cout<<fin[i];
        cout<<endl;
		k++;
	}
}
