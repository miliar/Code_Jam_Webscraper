#include <iostream>
#include <conio.h>
using namespace std;
int get ()
{
	char ch = _getche();
	int temp;
	int i=0;
	while (int(ch)!=32 && int(ch)!=13)
	{
		temp=int(ch);
		i = i*10 + temp;
		ch = _getche();
	}
	return i;
}

void main()
{
	int index,index2=1,row,column;
	cin>>index;
	int ** items=0;
	bool check = false;

	while (index)
	{	
		cin>>row>>column;
		int temp;
		items = new int * [row];
		for (int i = 0; i < row; i++)
		{
			items[i] = new int [column];
			for (int j = 0; j < column; j++)
			{
				int val;
				cin>>val;
				items[i][j] = val;
			}
			int j = column-1;
		
		}
				
		//***********************************************
		for(int i = 0; i < column; i++)
			for (int j = 0; j < row; j++)
			{
				bool pos1 = true;
				bool pos2 = true;
				bool pos3 = true;
				bool pos4 = true;
				temp = 0;
				
				while(temp<i)	//left
				{
					if(items[j][i] < items[j][temp])
					{
						pos1 = false;
						break;
					}
					temp++;
				}
				temp = i+1;
				while(temp<column)	//right
				{					
					if(items[j][i] < items[j][temp])
					{
						pos2 = false;
						break;
					}
					temp++;
				}
				///////////////////////////////								
				temp = 0;
				while (temp<j)	//up
				{
					if(items[j][i] < items[temp][i])
					{
						pos3 = false;
						break;
					}
					temp++;
				}
				temp = j+1;
				while (temp<row)	//down
				{
					if(items[j][i] < items[temp][i])
					{
						pos4 = false;
						break;
					}
					temp++;
				}
				//////////////////////////////////
		/*		if(pos1==false && pos2==false && pos3==false && pos4==false)
				{
						cout<<"Case #"<<index2<<": "<<"NO"<<endl;
						index2++;
						i=column;
						check=true;
						break;
				}	*/
				if((pos1 == false || pos2 == false) && (pos3 == false || pos4 == false))
				{
					cout<<"Case #"<<index2<<": "<<"NO"<<endl;
					index2++;
					i=column;
					check=true;
					break;
				}
	/*			for(int i = 0 ; i < row ; i++)
					delete [] items[i];
				delete [] items;*/
			}
		if(check == false )
		{
			cout<<"Case #"<<index2<<": "<<"YES"<<endl;
			index2++;
		}
		index--;
		check = false;
	}
	for(int i = 0 ; i < row ; i++)
		delete [] items[i];
	delete [] items;
}
