#include<bits/stdc++.h>
using namespace std;

void input(){
	freopen("B-large.in","r",stdin);
   	freopen("B-large.out","w",stdout);
}




int main(){
input();
string  str;
long long int count,flip,i,j,ts=1,t;

cin>>t;
while(t--){
	
	
	cin>>str;
	cout<<"Case #"<<ts<<": ";ts++;
	count=0;
	for(i=str.size()-1;i>=0;i--){
		if(str[i]=='+')
		continue;
		else{
			for(j=0;j<=(i)/2 &&j>=0;j++){
				if(str[j]=='+') str[j]='-';
				else str[j]='+';
				if(j!=(i-j)){
					if(str[i-j]=='+') str[i-j]='-';
					else  str[i-j]='+';
				}
				swap(str[j],str[i-j]);
			}
			count++;
			flip=0;
			while(str[i]=='-' && i>=0){
				i--;
				flip=1;
			}

			if(flip==1) count++;
		}
	}
	cout<<count<<endl;

}
				
	
		







	











return 0;
}
