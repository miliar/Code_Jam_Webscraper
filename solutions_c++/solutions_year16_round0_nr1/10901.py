#include <bits/stdc++.h>
using namespace std;

int main(){
	freopen("input_file_name.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int t;
	cin>>t;
	for(int q=1;q<=t;q++){
		int n;
		
		cin>>n;
		
		if(n==0)
			cout<<"Case #"<<q<<": "<<"INSOMNIA"<<endl;
		
		else{
			int count = 0;
			map <int, int> M;

			int i=1;
			int num;
			int finAnswer;

			while(1){
				if(count==10){
					finAnswer=n*(i-1);
					break;
				}

				num=n*i;
				//cout<<num<<' '<<i<<endl;
				while(num!=0){	
					if(M.find(num%10)==M.end()){
						M[num%10]=1;
						count++;
					}
					num=num/10;
				}	

				i++;

			}
			cout<<"Case #"<<q<<": "<<finAnswer<<endl;
		}

	}
	
	return 0;
}