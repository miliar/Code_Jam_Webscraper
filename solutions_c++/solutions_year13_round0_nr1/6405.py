#include<iostream>

using namespace std;

#define mod 1000000007
typedef long long ll ;


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.in", "w", stdout);
    int n;
    cin>>n;
    
    for(int t=1;t<=n;t++)
    {
    	string s[4];
    	int flagx=0, flago=0, flagdot=0;
    	for(int i=0;i<4;i++)
    	{
    		cin>>s[i];
    		if( (s[i][0]=='X' || s[i][0] == 'T' )  && (s[i][1]=='X' || s[i][1] == 'T' )  && (s[i][2]=='X' || s[i][2] == 'T' )  && (s[i][3]=='X' || s[i][3] == 'T' ) )
    		flagx=1;
    		else if( (s[i][0]=='O' || s[i][0] == 'T' )  && (s[i][1]=='O' || s[i][1] == 'T' )  && (s[i][2]=='O' || s[i][2] == 'T' )  && (s[i][3]=='O' || s[i][3] == 'T' ) )
    		flago=1;
    		else if( s[i][0]=='.' || s[i][1] == '.' || s[i][2]=='.' || s[i][3] == '.' ) 
    		flagdot=1;
    	
		}
		
		for(int i=0;i<4;i++)
    	{
    	
    		if( (s[0][i]=='X' || s[0][i] == 'T' )  && (s[1][i]=='X' || s[1][i] == 'T' )  && (s[2][i]=='X' || s[2][i] == 'T' )  && (s[3][i]=='X' || s[3][i] == 'T' ) )
    		flagx=1;
    		else if( (s[0][i]=='O' || s[0][i] == 'T' )  && (s[1][i]=='O' || s[1][i] == 'T' )  && (s[2][i]=='O' || s[2][i] == 'T' )  && (s[3][i]=='O' || s[3][i] == 'T' ) )
    		flago=1;
    	
		}
		
			if( (s[0][0]=='X' || s[0][0] == 'T' )  && (s[1][1]=='X' || s[1][1] == 'T' )  && (s[2][2]=='X' || s[2][2] == 'T' )  && (s[3][3]=='X' || s[3][3] == 'T' ) )
    		flagx=1;
    		else if( (s[0][0]=='O' || s[0][0] == 'T' )  && (s[1][1]=='O' || s[1][1] == 'T' )  && (s[2][2]=='O' || s[2][2] == 'T' )  && (s[3][3]=='O' || s[3][3] == 'T' ) )
    		flago=1;
    		
    		if( (s[0][3]=='X' || s[0][3] == 'T' )  && (s[1][2]=='X' || s[1][2] == 'T' )  && (s[2][1]=='X' || s[2][1] == 'T' )  && (s[3][0]=='X' || s[3][0] == 'T' ) )
    		flagx=1;
    		else if( (s[0][3]=='O' || s[0][3] == 'T' )  && (s[1][2]=='O' || s[1][2] == 'T' )  && (s[2][1]=='O' || s[2][1] == 'T' )  && (s[3][0]=='O' || s[3][0] == 'T' ) )
    		flago=1;
    		
    		
    		if(flagx==1) cout<<"Case #"<<t<<": X won\n";
    		else if (flago==1) cout<<"Case #"<<t<<": O won\n";
			else if(flagdot==1) cout<<"Case #"<<t<<": Game has not completed\n";
			else cout<<"Case #"<<t<<": Draw\n";
			 
    }
    return 0;
    }
