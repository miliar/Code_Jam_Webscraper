#include<iostream>
using namespace std;


int main()
{
	
	int t;
	cin>>t;
	int x,r,c;
	for(int i=0 ; i<t ; i++)
	{
		cin>>x>>r>>c;
		
		cout<<"Case #"<<i+1<<": ";
                if (x == 1) 
		{
                   	cout<<"GABRIEL";
                } 
		else if (x == 2) 
		{
                     	if ((r * c) % 2 == 0) 
			{
                                cout<<"GABRIEL";
                        } 
			else 
			{
                                cout<<"RICHARD";
                        }
                } 
		else if (x == 3) 
		{
                        if ((r * c) % 3 == 0)
			{
                                if (r == 1 || c == 1)
                                        cout<<"RICHARD";
                                else
                                        cout<<"GABRIEL";
                        } else {
                                cout<<"RICHARD";
                        }
                } else if(x ==4){
                        if ((r * c) % 4 == 0){
                                if (r == 1 || c == 1){
                                        cout<<"RICHARD";
                                } else if (r == 2 || c == 2) {
                                        cout<<"RICHARD";
                                } else if(r == 3 || c == 3){
                                        cout<<"GABRIEL";
                                }
                                else {
                                        cout<<"GABRIEL";
                                }
                        }
                        else
                                cout<<"RICHARD";
                }
		else
		{
                	cout<<"RICHARD";
		}			
		
		cout<<endl;

	}


}
