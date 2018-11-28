#include<iostream>


using namespace std;

int Fi_Ans;
int Se_Ans;
int Fi_Arr[4][4];
int Se_Arr[4][4];

void Enter_Array(int Arr[][4]);
void Compare(int _Fi_Arr[][4],int _Se_Arr[][4],int Case);
bool search(int Num);

int main()

{
	freopen("output.txt","w",stdout);
	freopen("Text.txt","r",stdin);
	int No_Case;
	cin>>No_Case;





	for(int Case=0;Case<No_Case;Case++)
	{

		for(int Ans=0 ; Ans<2 ; Ans++)
		{
			if(Ans==0) {						
				cin>>Fi_Ans;
				Enter_Array(Fi_Arr);

			}
			else {
				cin>>Se_Ans;
				Enter_Array(Se_Arr);
			}
		}
		  

		Compare(Fi_Arr,Se_Arr,Case);
	}
	


	return 0;
}


void Enter_Array(int Arr[][4])
{
	for(int x=0;x<4;x++){
		for(int y=0;y<4;y++){
			cin>>Arr[x][y];
		}
	}
}
void Compare(int _Fi_Arr[][4],int _Se_Arr[][4],int Case)
{
	bool First = false;
	int Number_Show;
	for(int y=0;y<4;y++){
		if(true == search(Fi_Arr[Fi_Ans-1][y])) 
			if(!First){Number_Show=Fi_Arr[Fi_Ans-1][y]; First=true;}
			else {cout<<"Case #"<<Case+1<<": Bad magician!"<<endl; Number_Show=-1; break;}
	}

	if(!First) cout<<"Case #"<<Case+1<<": Volunteer cheated!"<<endl;
	else if(Number_Show != -1) cout<<"Case #"<<Case+1<<": "<<Number_Show<<endl;
}


bool search(int Num)
{	
		for(int y=0;y<4;y++)
			if(Num == Se_Arr[Se_Ans-1][y])
				return true;

		return false;
}