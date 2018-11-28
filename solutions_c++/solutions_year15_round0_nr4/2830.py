#include<iostream>
using namespace std;

string ominoWinner(int x,int r,int c)
{
	if(x==1)
		return "GABRIEL";
	else if((r*c)%x!=0)
		return "RICHARD";
	else if(x==2)
		return "GABRIEL";
	else if(r*c==x)
		return "RICHARD";
	else
	{
		if(x==3)
			return "GABRIEL";
		else
		{
			if((r*c)==8)
				return "RICHARD";
			else
				return "GABRIEL";
		}
	}
}

int main()
{
    int cases, X,R,C;
	string winner;	            
	cin >> cases;                    
	for(int c=1; c<=cases; c++)      
	{
		cin >> X; cin >> R; cin>>C;                                 
		winner = ominoWinner(X,R,C); 
		cout<<"Case #"<<c<<": "<<winner<<endl;  
	}
    return 0;                        
}
