#include <iostream>
#include <conio.h>
#include <string>
#include <fstream>


using namespace std;

void main()
{
	string line;
	std::freopen("output_A.txt", "w", stdout);
	ifstream file("A-large.in", ios::in);
	
	if(!file)
		cout<<"File not opened\n";
	
	int count;
	file>>count;
	char matrix[5][5]={0};
	bool x=false, o=false, draw=false, undone=false;
	int dots=0;
	for(int i=0;i<count;i++)
	{
		x=false;
		o=false;

		dots=0;
		printf("Case #%d: ",i+1);
		
		
		for(int j=0;j<4;j++)
			file>>matrix[j];

		for(int j=0;j<4;j++){
			int x_count=0, o_count=0;
			for(int k=0;k<4;k++){
				if(matrix[j][k]=='X'||matrix[j][k]=='T')
					x_count++;
				if(matrix[j][k]=='O'||matrix[j][k]=='T')
					o_count++;
				if(matrix[j][k]=='.')
					dots++;
			}
			if(x_count==4){
				cout<<"X won\n";
				x=true;
				break;
			}
			if(o_count==4){
				cout<<"O won\n";
				o=true;
				break;
			}
			if(x || o)
				break;
		}
		if(!(x || o || draw || undone)){
			for(int j=0;j<4;j++){
				int x_count=0,o_count=0;
				for(int k=0;k<4;k++){
					if(matrix[k][j]=='X'||matrix[k][j]=='T')
						x_count++;
					if(matrix[k][j]=='O'||matrix[k][j]=='T')
						o_count++;
					
				}
				if(x_count==4){
					cout<<"X won\n";
					x=true;
					break;
				}
				if(o_count==4){
					cout<<"O won\n";
					o=true;
					break;
				}
				if(x || o)
					break;
			}			
		}

		if(!(x || o || draw || undone)){
			int x_count=0;
			int o_count=0;
			for(int j=0;j<4;j++){
				if(matrix[j][j]=='X' || matrix[j][j]=='T')
					x_count++;
				
				if(matrix[j][j]=='O' || matrix[j][j]=='T')
					o_count++;					
				
				if(x_count==4){
					cout<<"X won\n";
					x=true;
					break;
				}
				if(o_count==4){
					cout<<"O won\n";
					o=true;
					break;
				}
			}
		}

		if(!(x || o || draw || undone)){
			int x_count=0;
			int o_count=0;
			for(int j=0;j<4;j++){
				if(matrix[j][3-j]=='X' || matrix[j][3-j]=='T')
					x_count++;
				
				if(matrix[j][3-j]=='O' || matrix[j][3-j]=='T')
					o_count++;					
				
				if(x_count==4){
					cout<<"X won\n";
					x=true;
					break;
				}
				if(o_count==4){
					cout<<"O won\n";
					o=true;
					break;
				}
			}
			
		}
		
		if(!(x || o || draw || undone)){
			if(dots>0)
				cout<<"Game has not completed\n";
			else
				cout<<"Draw\n";
		}
		//file>>matrix[4];//to remove the empty line
	}
	
}