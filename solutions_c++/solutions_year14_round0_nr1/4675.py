

#include <iostream>
#include<iomanip>
#include<vector>
#include<algorithm>
using namespace std;
void resetChoice(int choice[]){
	for(int i=0;i<16;i++){
		choice[i]=-1;
	}
}


int main()
{
	int iCases;
	int iAnswer;
	int firstChoice[16];
	int iTemp;
	int iMatches;
	int iCard;
	cin>>iCases;
	for(int i=0;i<iCases;i++){
			resetChoice(firstChoice);
			iMatches=0;
			cin>>iAnswer;
		iAnswer--;
			for(int r=0;r<4;r++){
				for(int c=0;c<4;c++){
				cin>>iTemp;
					if(r==iAnswer){
						firstChoice[iTemp-1]=1;
					}
				}
			}
			cin>>iAnswer;
		iAnswer--;
			for(int r=0;r<4;r++){
				for(int c=0;c<4;c++){
				cin>>iTemp;
					if(r==iAnswer){
						if(firstChoice[iTemp-1]==1){
							iMatches++;
							iCard=iTemp;
						}
					}
				}
			}
cout<<"Case #"<<i+1<<": ";
		switch(iMatches){
			case 0:
				cout<<"Volunteer cheated!\n";
				break;
				case 1:
				cout<<iCard<<"\n";
				break;
				default:
				cout<<"Bad magician!\n";
		}
		
			
	}
	return 0;
}

