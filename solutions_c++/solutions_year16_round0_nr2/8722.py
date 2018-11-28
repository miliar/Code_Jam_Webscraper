#include<bits/stdc++.h>
using namespace std;

int main()
{
	char tab2[200];
	string str;
	int t,i,c,j;
	freopen("B-large.in","r",stdin);
	freopen("Boutputlarge1.in","w",stdout);
	cin>>t;
	for( j=1;j<=t;j++){
	cin>>str;
    c=0;
strncpy(tab2, str.c_str(), sizeof(tab2));
for( i=0;tab2[i]!=0;i++){
	if(i==0&&tab2[0]=='-')
	c++;
	if(tab2[i-1]=='+'&&tab2[i]=='-')
	c=c+2;
}
    cout << "Case #" << j << ": " <<c<< endl;
for(int k=0;tab2[k]!=0;k++)    
     tab2[k]=0;
	
}
	return 0;
}
