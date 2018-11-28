#include <iostream>
#include<string>
using namespace std;

string s;

void flip(int a, int b)
{
	string temp;
	int len = b-a;
	temp = s.substr(a, len+1);
//	cout<<"Temp: "<<temp<<endl;
	
	for(int i=a; i<=b; i++)
	{
		
		if(temp[len] == '+')
		s[i] = '-';
		
		else
		s[i] = '+';
		
		len-- ;
	}
	
//	cout<<"S in function "<<s<<endl;
}


/*

int main()
{
	s = "+--+-++";
	flip(0, 2);
	cout<<s;
	return 0;
}

*/


int main() 
{
	int t = 0, top_count = 0, bottom_count = 0, flip_a = 0, flip_b = 0, len, ans=0, flag = 0;
	bool top, bottom;   //1 for happy side 0 for blank side
	cin>>t;
	for(int i=0; i<t; i++)
	{
		cin>>s;

		len = s.length();
//		cout<<s<<" and length is: "<<len<<endl;
		top = bottom = 0;
		top_count = bottom_count = flag = ans = 0;
		while(flag == 0)
		{
		//	cout<<s<<endl;
			//CALCULATE TOP
			if(s[0] == '+')
			{
				top = 1;
			}
			else
			{
				top = 0;
			}
			top_count = 1;
			
			for(int j=1; j<len; j++)
			{
				if(top && s[j] == '+')
				top_count++;
				
				else if(!top && s[j] == '-')
				top_count++;
				
				else 
				break;
			}
			
			//CALCULATE BOTTOM
	
			if(s[len-1] == '+')
			{
				bottom = 1;
			}
			else
			{
				bottom = 0;
			}
			bottom_count = 1;
			
			for(int j=len-2; j>=0; j--)
			{
				if(bottom && s[j] == '+')
				bottom_count++;
				
				else if(!bottom && s[j] == '-')
				bottom_count++;
				
				else 
				break;
			}
			
//			cout<<"TC: "<<top_count<<" TS: "<<top<<" BC: "<<bottom_count<<" BS: "<<bottom<<endl;
			
			//FOUR CASES PLUS-PLUS MINUS-MINUS AND SO ON
			
			if(top == 1)  //IF TOP IS POSITIVE
			{
				if(bottom == 1) //IF BOTTOM IS POSITIVE
				{
					if(top_count == bottom_count && top_count == len)
					{
						flag=1;
					}
					
					else if(top_count <= bottom_count)
					{
						ans++;
						flip(0, top_count-1);//FLIP TOP PLUS
					}
					
					else
					{
						ans++;
						flip(0, top_count-1);  //FLIP TOTAL
					}
				}
				
				else if(bottom == 0)  //BOTTOM IS MINUS
				{
					if(top_count == 0)
					{
						ans++;
					}
					
					else if(bottom_count == 0)
					{
						flag=1;
					}
					
					else 
					{
						ans++;
						flip(0, top_count-1); //FLIP TOP PLUS
					}
				}
			}
			
			else if(top == 0) //TOP IS MINUS
			{
				if(bottom == 1) //BOTTOM IS PLUS
				{
					if(top_count == 0)
					{
						flag = 1;
					}
					
					else if(bottom_count == 0)
					{
						ans++;
					}
					
					else
					{
						ans++;
						flip(0, top_count-1); //FLIP TOP MINUS
					}
				}
				
				else if(bottom == 0)  //BOTTOM IS MINUS
				{
					if(top_count == bottom_count && top_count == len)
					{
						ans++;
						flag = 1;
					}
					
					else if(top_count >= bottom_count)
					{
						ans++;
						flip(0, top_count-1); //FLIP TOP MINUS
					}
					
					else
					{
						ans++;
						flip(0, len-1);
					}
				}
			}
			
			
		}

		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
