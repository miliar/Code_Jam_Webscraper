#include <iostream>
using namespace std;
enum Type{
	Good, Bad, Cheet
};

void main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	for(int  i = 0 ; i < t; i++){
		cout<<"Case #"<<(i+1)<<": ";
		int ms[16] = {0};
		int n;
		cin>>n;
		n--;
		for(int j = 0 ; j < 4 ; j++)
			for(int z = 0; z < 4; z++){
				int val;
				cin>>val;
				if(j == n)
					ms[val-1] ++;
			}
		cin>>n;
		n--;
		for(int j = 0 ; j < 4 ; j++)
			for(int z = 0; z < 4; z++){
				int val;
				cin>>val;
				if(j == n)
					ms[val-1] ++;
			}
		int ans;
		Type type = Type::Cheet;
		for(int i = 0; i < 16; i++)
			if( ms[i] == 2 ){
				if(type == Type::Cheet)
					type = Type::Good;
				else
					type = Type::Bad;
				ans = i;
			}
		
		if(type == Type::Cheet)
			puts("Volunteer cheated!");
		else
			if(type == Type::Bad)
				puts("Bad magician!");
			else
				cout<<ans+1<<endl;
	}
}