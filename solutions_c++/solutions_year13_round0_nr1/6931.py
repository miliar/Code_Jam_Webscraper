#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int win(char spaces[4][4])
{
	    for( int i = 0; i < 4; i++ )
	{
			if((spaces[i][0] =='T' ||  spaces[i][0]=='X') &&(spaces[i][1] =='T' ||spaces[i][1]=='X' )&&(spaces[i][2] =='T' || spaces[i][2]== 'X' )&&(spaces[i][3]=='X' ||spaces[i][3] =='T' ))
				return 1;
			else if((spaces[i][0] =='T' ||  spaces[i][0]=='O') &&(spaces[i][1] =='O' ||spaces[i][1]=='T' )&&(spaces[i][2] =='T' || spaces[i][2]== 'O' )&&(spaces[i][3]=='T' ||spaces[i][3] =='O' ))
			     return 2;

	}
	for( int i = 0; i < 4; i++ )
	{
			if( (spaces[0][i] =='T' ||  spaces[0][i]=='X') &&(spaces[1][i] =='T' ||spaces[1][i]=='X' )&&(spaces[2][i] =='T' || spaces[2][i]== 'X' )&&(spaces[3][i]=='X' ||spaces[3][i] =='T' ))
				return 1;

			else if((spaces[0][i] =='T' ||  spaces[0][i]=='O') &&(spaces[1][i] =='T' ||spaces[1][i]=='O' )&&(spaces[2][i] =='T' || spaces[2][i]== 'O' )&&(spaces[3][i]=='O' ||spaces[3][i] =='T' ))
			     return 2;

	}

		if( (spaces[0][0] =='T' ||  spaces[0][0]=='X') &&(spaces[1][1] =='T' ||spaces[1][1]=='X' )&&(spaces[2][2] =='T' || spaces[2][2]== 'X' )&&(spaces[3][3]=='X' ||spaces[3][3] =='T' ))
				return 1;
			else if((spaces[0][0] =='T' ||  spaces[0][0]=='O') &&(spaces[1][1] =='T' ||spaces[1][1]=='O' )&&(spaces[2][2] =='T' || spaces[2][2]== 'O' )&&(spaces[3][3]=='O' ||spaces[3][3] =='T' ))
			     return 2;


		if( (spaces[0][3] =='T' ||  spaces[0][3]=='X') &&(spaces[1][2] =='T' ||spaces[1][2]=='X' )&&(spaces[2][1] =='T' || spaces[2][1]== 'X' )&&(spaces[3][0]=='X' ||spaces[3][0] =='T' ))
				return 1;
        else if( (spaces[0][3] =='T' ||  spaces[0][3]=='O') &&(spaces[1][2] =='T' ||spaces[1][2]=='O' )&&(spaces[2][1] =='T' || spaces[2][1]== 'O' )&&(spaces[3][0]=='O' ||spaces[3][0] =='T' ))
			     return 2;

        return 0;

	}

	int main()
	{
	    freopen("A.txt","r",stdin);
        freopen("ap.txt","w",stdout);
	    int a,b;
	    bool y;
	    char spaces[4][4];
	    scanf("%d",&a);
	    for(int z=1;z<=a;++z)
	    {
	        y=false;
	        for(int j=0;j<4;j++)
	        scanf("%s",&spaces[j]);
	        b=win(spaces);
	        if(b==1)
	        cout<<"Case #"<<z<<": "<<"X won\n";
	        else if( b==2)
	        cout<<"Case #"<<z<<": "<<"O won\n";
	        else if(b==0)
	        {
	            for(int k=0;k<4;k++)
	            {

	                for(int j=0;j<4;j++)
	                {
	                    if(spaces[k][j]=='.')
	                    {
	                        y=true;
	                    }
	                }
	            }
	            if(y==true)
	            cout<<"Case #"<<z<<": "<<"Game has not completed\n";
	            else
                cout<<"Case #"<<z<<": "<<"Draw\n";
	        }
	    }


	}




