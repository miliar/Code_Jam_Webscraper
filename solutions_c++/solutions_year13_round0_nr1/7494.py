#include "iostream"

using namespace std;

int main()
{
long testcases =0;
cin>>testcases;
long caseno = 1;
while(testcases--)
{
	char arr[4][4];
	for(int i =0;i<4; i++)
	{		
	char str[10];
	cin>>str;
		for(int j=0;j<4;j++)
	{
		arr[i][j]=str[j];	
	}
	}
	bool winner = false;
	char winnerPlayer = '.';
	bool anyDots = false;
	for(int i =0;i<4;i++)
		{
//		cout<<"Considering the row "<<i<<endl;
		int T =0,X=0,O=0;
		for(int j=0;j<4;j++)
		{
			char c = arr[i][j];
			if(c=='.') {
				 	// no win in this row... 
					anyDots= true;
					}
			if(c=='T') 
					T++;
			else if(c=='X') X++;
			else if(c=='O') O++;

		}
		if(true)
		{
		//	cout<<T<<" "<<X<<" "<<O<<endl;
			if((T==1 && X==3) || (T==0 && X==4) ) {
						winner=true; winnerPlayer = 'X';
				}
			else if((T==1 && O==3) || (T==0 && O ==4)) 
			{
			 winner=true; winnerPlayer ='O';
			}	
			else {winner =false;}

		}
		if(winner) { //cout<<"winner found in rows : "<<winnerPlayer<<endl;
		break;}
		
		}

		for(int i =0;i<4;i++)
                {
		if(winner) break;
               // cout<<"Considering the column "<<i<<endl;
                int T =0,X=0,O=0;
                for(int j=0;j<4;j++)
                {
                        char c = arr[j][i];
                        if(c=='.') {
                                        // no win in this row... 
                                        anyDots= true;
                                        }
                        if(c=='T')
                                        T++;
                        else if(c=='X') X++;
                        else if(c=='O') O++;

                }
                if(true)
                {
                        if((T==1 && X==3) || (T==0 && X==4) ) {
                                                winner=true; winnerPlayer = 'X';
                                } 
                        else if((T==1 && O==3) || (T==0 && O ==4))
                        {
                         winner=true; winnerPlayer ='O';
                        } 
                        else {winner =false;}

                }
                if(winner) break;

                }
	
		bool flag = false;	
		bool flipColumn = false;
		for(int i =0;i<2;i++)
                {
                if(winner) break;
                //cout<<"Considering the digonal "<<i<<endl;
                if(flag == false ) {flag = true; }
                        else flipColumn =true;
		int T =0,X=0,O=0;
                for(int j=0;j<4;j++)
                {
                        int row = j;
			int column;
			if(flipColumn) column = 3-j;
			else  column =j;
			char c = arr[row][column];
		//	cout<<row<<","<<column<<" "<<arr[row][column]<<endl;
                        if(c=='.') {
                                        // no win in this row... 
                                        anyDots= true;
                                        }
                        if(c=='T')
                                        T++;
                        else if(c=='X') X++;
                        else if(c=='O') O++;

                }
                if(true)
                {
                        if((T==1 && X==3) || (T==0 && X==4) ) {
                                                winner=true; winnerPlayer = 'X';
                                }
                        else if((T==1 && O==3) || (T==0 && O ==4))
                        {
                         winner=true; winnerPlayer ='O';
                        }
                        else {winner =false;}

                }
                if(winner) break;

                }
  	cout<<"Case #"<<caseno<<": ";
	if(!winner && !anyDots) cout<<"Draw\n";
	else if(!winner && anyDots) cout<<"Game has not completed\n";
	else if(winner) cout<<winnerPlayer<<" won"<<endl;
	caseno++;

}
return 0;
}


