//      jam1.cpp
//      
//      Copyright 2013 METIN BALABAN <e1819077@inek27>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;
int arr[4][4];
int main(int argc, char **argv)
{
	int k;
	char temp;
	int holdp,holdq;	
	int diagon1=1;
	int diagon2=1;		
	int totalpro=1;
		
	cin >> k;
	for(int i=0;i<k;i++)
	{
		for(int p=0;p<4;p++){
			for(int q=0;q<4;q++)
			{
					cin>>temp;
					switch(temp)
					{
						case 'X': arr[p][q]=2; break;
						case 'O': arr[p][q]=3; break;
						case '.': arr[p][q]=0; break;
						case 'T': arr[p][q]=6; break;
					}
			}
		}
/*		for(int p=0;p<4;p++)
		{
			for(int q=0;q<4;q++)
				cout << arr[p][q] << " ";
			cout << endl;
			
		}*/
		int ver=1,hor=1;
		for(int p=0;p<4;p++)
		{
			ver=1;hor=1;
			int q=0;
			for(;q<4;q++)
			{
				ver*=arr[p][q];
			}
			if(ver==0) {ver =1 ;goto here;}
			
			if(ver%16==0)
			{	
					holdp=p;
					holdq=q;
	//	cout << "line 72\n" ;

					goto xwins;
			}
			else if(ver%81==0)
			{
				goto owins;
			}
			else 
				ver=1;
			
			here:
			for(int q=0;q<4;q++)
			{
				hor*=arr[q][p];
			}
			if(hor==0) {hor =1 ;continue;}
			
			if(hor%16==0)
			{
		//			cout << "line 90\n" ;
					goto xwins;
			}
			else if(hor%81==0)
			{
				goto owins;
			}
			else 
				hor=1;			
			
		}
	 diagon1=1;
	 diagon2=1;		
	 totalpro=1;
		
		for(int p=0;p<4;p++)
		{
				diagon1*=arr[p][p];
				diagon2*=arr[p][3-p];
		}
		if(diagon1!=0){
			 if(diagon1%16==0)
				goto xwins;
			 if(diagon1%81==0)
				goto owins;
		}
		if(diagon2!=0){
			 if(diagon2%16==0)
				goto xwins;
			 if(diagon2%81==0)
				goto owins;
		}		
		for(int p=0;p<4;p++)
		{
			for(int q=0;q<4;q++)
			{
				totalpro*=arr[p][q];
			}
		}
		if(totalpro==0)
		{
			printf( "Case #%d: Game has not completed\n",i+1 );
			continue;
		}
		else
			printf( "Case #%d: Draw\n",i+1 );
	continue;		
	xwins:
	
	printf( "Case #%d: X won\n",i+1 );
	continue;
	
	
	owins:
	printf( "Case #%d: O won\n",i+1 );
	continue;
	
	}
	
	
	return 0;
}

