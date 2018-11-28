#include<iostream>
#include<cstdio>
using namespace std;
int main(){
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int t,i,j,test=1;
char st[4][4];
cin>>t;
while(test<=t)
	{
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		cin>>st[i][j];
	int counter1 =0,counter2 =0,counter3 =0,noh=0,nov=0,nocomp=0,nodl=0,nodr=0;
	char won[5];
	won[4] = 'D';
	won[2] = st[0][0];
	won[3] = st[3][0];
	if(won[2] == 'T')
	won[2] = st[3][3];
	if(won[3] == 'T')
	won[3] = st[0][3];
	for(i=0;i<4;i++)
		{
		counter1 =1,counter2 =1,noh=0,nov=0;
		won[0] = st[i][0];
		won[1] = st[0][i];
		
		if(won[0] == '.' || won[1] == '.')
			{
			nocomp = 1;			
			}
		for(j=1;j<4;j++)
			{
			//cout<<"st["<<i<<"]["<<j<<"]"<<st[i][j]<<"-"<<won[0]<<endl;
			if(st[i][j] != won[0] &&( st[i][j] != 'T' ))
			{noh =1; //cout<<"TER1"<<endl;
			}
			if(!noh)
			counter1++;
			//cout<<"st["<<j<<"]["<<i<<"]"<<st[j][i]<<"-"<<won[1]<<endl;
			if(st[j][i] != won[1] &&( st[j][i]  != 'T' ))
			{nov=1;//cout<<"TER2"<<endl;
			}
			if(!nov)
			counter2++;
			
			if(noh && nov)
			break;
			
			if(st[i][j] == '.' ||  st[j][i] == '.'  )
				{
				nocomp = 1;			
				}

			}
			//cout<<counter1<<" "<<counter2<<endl;
		if(counter1==4)
			{
			won[4] = won[0];
			nodl = nodr = 1;
			break;
			}
		else if(counter2==4)
			{
			won[4] = won[1];
			nodl = nodr = 1;
			break;		
			}
		else 
			{
			if(st[i][i] != won[2] && st[i][i] != 'T' )
				{nodl =1;//cout<<"st["<<i<<"]["<<i<<"]"<<st[i][i]<<"-"<<won[2]<<endl;
				}
		 	if(st[i][3-i] != won[3] && st[i][3-i] != 'T')
				{nodr =1;//cout<<"st["<<i<<"]["<<3-i<<"]"<<st[i][3-i]<<"-"<<won[3]<<endl;
				}
			}
		}

	
	if(!nodl)
		cout<<"Case #"<<test<<": "<<won[2]<<" won\n";
	else if(!nodr)
		cout<<"Case #"<<test<<": "<<won[3]<<" won\n";
	else 
		{
		if(won[4] != 'D' && won[4] != '.')
		cout<<"Case #"<<test<<": "<<won[4]<<" won\n";
		else if(!nocomp)
		cout<<"Case #"<<test<<": Draw\n";
		else if(nocomp)
		cout<<"Case #"<<test<<": Game has not completed\n";
		}
	
	

	test++;
	}//while loop ends here

return 0;
}
