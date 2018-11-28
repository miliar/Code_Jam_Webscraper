#include<iostream>

#include<cstdio>

using namespace std;

int main()
{
	int test;
	cin>>test;
	string str[4];
	string col[4];
	
	char arr[5][5];
	int c = 1;
	int flag;
	int not_complete = 0;
	
	while(test--)
	{
				int i,j;
				string ldig = "";
				string rdig = "";
				flag = 0;
				not_complete = 0;
				char winner;
				string s="";
				for(int i = 0; i<4; i++)
				{
					for(j = 0; j<4; j++)
					{
						cin>>arr[i][j];
						s = s+arr[i][j];
						if(arr[i][j] == '.')
							not_complete = 1;
					}
					str[i] = s;
					s = "";
				}
				for(int i = 0; i<4; i++)
				{
					s = "";
					for(j = 0; j<4; j++)
					{
						s = s+arr[j][i];
						if(i == j)
							ldig = ldig+arr[i][j];
						if((i+j)== 3)
							rdig = rdig+arr[i][j];
					}
					col[i] = s;
				}
					if(ldig == "XXXX" || ldig == "XXXT" || ldig == "XXTX" || ldig == "XTXX" || ldig == "TXXX")
					{
						cout<<"Case #"<<c<<": "<<"X won"<<endl;
						c++;
						continue;
					}
					if(ldig == "OOOO" || ldig == "OOOT" || ldig == "OOOT" || ldig == "OOTO" || ldig == "OTOO" || ldig == "TOOO")
					{
						cout<<"Case #"<<c<<": "<<"O won"<<endl;
						c++;
						continue;
					}
					if(rdig == "XXXX" || rdig == "XXXT" || rdig == "XXTX" || rdig == "XTXX" || rdig == "TXXX")
					{
						cout<<"Case #"<<c<<": "<<"X won"<<endl;
						c++;
						continue;
					}
					if(rdig == "OOOO" || rdig == "OOOT" || rdig == "OOOT" || rdig == "OOTO" || rdig == "OTOO" || rdig == "TOOO")
					{
						cout<<"Case #"<<c<<": "<<"O won"<<endl;
						c++;
						continue;
					}
				//check row wise
				
				for(int i = 0; i<4; i++)
				{
					if(str[i] == "XXXX" || str[i] == "XXXT" || str[i] == "XXTX" || str[i] == "XTXX" || str[i] == "TXXX")
					{
						flag = 1;
						winner = 'X';
						break;
					}
					if(str[i] == "OOOO" || str[i] == "OOOT" || str[i] == "OOOT" || str[i] == "OOTO" || str[i] == "OTOO" || str[i] == "TOOO")
					{
						flag = 1;
						winner = 'O';
						break;
					}
				}
				
				if(flag == 1)
				{
					cout<<"Case #"<<c<<": "<<winner<<" won"<<endl;
					c++;
					continue;
				}
				
				//check column wise
				
				for(int i = 0; i<4; i++)
				{
					if(col[i] == "XXXX" || col[i] == "XXXT" || col[i] == "XXTX" || col[i] == "XTXX" || col[i] == "TXXX")
					{
						flag = 1;
						winner = 'X';
						break;
					}
					if(col[i] == "OOOO" || col[i] == "OOOT" || col[i] == "OOOT" || col[i] == "OOTO" || col[i] == "OTOO" || col[i] == "TOOO")
					{
						flag = 1;
						winner = 'O';
						break;
					}
				}
				
				if(flag == 1)
				{
					cout<<"Case #"<<c<<": "<<winner<<" won"<<endl;
					c++;
					continue;
				}
				
				if(flag == 0)
			    {
			    	if(not_complete == 1)
			    		cout<<"Case #"<<c<<": "<<"Game has not completed";
			    	else
			    		cout<<"Case #"<<c<<": "<<"Draw";
			    }
			    cout<<endl;
			    c++;
	}
	
	return 0;
}
