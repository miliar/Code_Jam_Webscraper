#include<iostream>
#include<stdio.h>
#include<conio.h>
using namespace std;
int main()
{
		unsigned short T=0;
		unsigned short C1=0;
		unsigned short C2=0;
		unsigned short temp=0;
		unsigned short possibleSel[4]={0};
		int found = 0;
		int i,j,k=0;
		cin >> T;
		
		for(int C = 1;C<=T;C++)
		{
			found =0;
			cin>> C1;
			
			for(i=0;i<4;i++)
			{
				for (j=0;j<4;j++){
					if(C1==i+1)
						cin>>possibleSel[j];
					else
					cin>>temp;
				}
			}
			
			cin>> C2;
			
			for(i=0;i<4;i++)
			{
				for (j=0;j<4;j++){
					cin>>temp;
					//cout<<"C2----"<< C2 <<"   "<< i+1<<endl;
					if(C2==i+1)
					{
						for (k=0;k<4;k++){
						//	cout<<"Temp and poss"<<temp<<"  "<<possibleSel[k]<<endl;
								if(temp == possibleSel[k]){
									if(found == 0)
									{
									found = temp;
									//cout<<"Found "<<temp<<endl;
									}
									else
									{
										found =-1;
										//cout<<"Found double"<<temp<<endl;
									}
								}
							}
						
						}
				}
					
					
				}
			
		
						if(found < 0)
						{
							printf("Case #%d: Bad magician!\n",C);
							continue;
										
						}
						
						if(found ==0)
						{
						printf("Case #%d: Volunteer cheated!\n",C);
												}
						else
						{
							{
						printf("Case #%d: %d\n",C,found);
						
						}
					}
		}
	return 0;
}


