#include<iostream>
using namespace std;


int main(){
	int M[4][4];
	int N[4][4];
	int n,v;
	int sol1,sol2,sol;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		sol=0;
		cin>>sol1;
		for(int j=0;j<4;j++)
			for(int g=0;g<4;g++)
				cin>>M[j][g];
		cin>>sol2;
		for(int j=0;j<4;j++)
			for(int g=0;g<4;g++)
				cin>>N[j][g];
		sol1--; sol2--;
		for(int j=0;j<4;j++)
			for(int g=0;g<4;g++) 
				if(M[sol1][j]==N[sol2][g])
				{
						sol++;
						v=M[sol1][j];
				}
		//solution
		if(sol==1) 
			cout<<"Case #"<<i+1<<": "<<v<<endl;
		else if(sol>1) 
			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		else 
			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
	}
	return 0;
};