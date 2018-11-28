#include<iostream>
#include <string>
#include <cstdio>

using namespace std;

int index ( char x) 
{ if ( x=='k') return 4;
	if (x== 'j') return 3;
	if (x== 'i') return 2;
}

int main()
{

	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

	int quaternion [4][4]= { 1, 2, 3, 4, 2,-1, 4,-3, 3, -4, -1 , 2, 4 , 3 , -2 ,-1};
	
	int T;  // no. of cases
	cin >> T;
	for ( int i = 1; i <= T; i++)
	{
		int L, X;
		string s;
		cin >>L>>X>>s;

		if ( L*X <3 ) cout << "Case #"<<i<<": NO"<<endl;

		else if (L == 3 && X==1 ){
			if(s == "ijk") cout << "Case #"<<i<<": YES"<<endl;
			else cout << "Case #"<<i<<": NO"<<endl;}

		else
		{
			string str = s;
			bool ivalid =0, jvalid=0;
			int sign=0, calc =0;
			

			for (int z=0; z< L*X; z++)
			{ 
				// checking for i
				if (z==0 && str[z]== 'i') {ivalid =1; calc=index(str[(z+1)%L]);z++; }

				else if (ivalid ==0)
				{
					if (z==0){  calc=index(str[0]) ; }
					else 
					{ 
						if (calc <0 )
						{
							sign ++;
							calc = abs(calc);
						}
						calc = quaternion [ calc-1 ] [ index(str[z%L])-1 ] ;
						
						if ( calc == -2 && sign%2 )
							{ivalid =1;sign =0; calc=index(str[(z+1)%L]);
							if (str[(z+1)%L] == 'j') { jvalid=1; calc=index(str[(z+2)%L]); z++;}
							z++;  }

							else if ( calc == 2 && sign%2==0 ) 
							{ivalid =1; sign =0; calc=index(str[(z+1)%L]);
							if (str[(z+1)%L] == 'j') { jvalid=1; calc=index(str[(z+2)%L]); z++;}
							z++;  }

					}
					
				}

				// check for j
				else if (ivalid ==1 && jvalid ==0)
				{
					if (z==1 && str[z%L]== 'j') {jvalid =1; calc=index(str[(z+1)%L]);z++; }

					else 
					{ 
						if (calc <0 )
						{
							sign ++;
							calc = abs(calc);
						}
						calc = quaternion [ calc-1 ] [ index(str[z%L])-1 ] ;
						
						if ( calc == -3 && sign%2 ) {jvalid =1; sign =0; calc=index(str[(z+1)%L]);z++; }
						else if ( calc == 3 && sign%2==0 ) {jvalid =1; sign =0; calc=index(str[(z+1)%L]);z++; }

					}
				}

					// check for k
				else if (ivalid ==1 && jvalid ==1)
				{
						if (calc <0 )
						{
							sign ++;
							calc = abs(calc);
						}
						calc = quaternion [ calc-1 ] [ index(str[z%L])-1 ] ;
					
				}


		}
			if (ivalid ==1 && jvalid ==1)
			{
				if (( calc == -4 && sign%2 ) || ( calc == 4 && sign%2==0 ) ) cout << "Case #"<<i<<": YES"<<endl;
				else cout << "Case #"<<i<<": NO"<<endl;
			}
			else cout << "Case #"<<i<<": NO"<<endl;
			


	}
	}

	return 0;
}