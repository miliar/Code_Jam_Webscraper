#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <bitset>
#include <fstream>
using namespace std;


bool all_(string &N)
{
	for(size_t i = 0 ; i <  N.size() ;i++)
		if(N[i] == '+')	
			return  false;
	return  true;
}


bool allPlus(string &N)
{
	for(size_t i = 0 ; i <  N.size() ;i++)
		if(N[i] == '-')	
			return  false;
	return  true;
}

int main(int argc, char *argv[])
{
//	cout<<endl;
	ofstream ecrire("output.txt");
	ifstream lire("input.txt");
	long long K;
	lire >> K;
	for(long long k=0; k < K;k++)
	{
		string  N;
		lire >> N; 
//		cout<<N<<endl;
		ecrire<<"Case #"<<k+1<<": ";
		
				
		long long result =0;
		
		
		if(allPlus(N))
			{
				result = 0;
				ecrire<<result<<endl;
			}
		else 
		{
			
		
		while (N.back() =='+') {
			N.pop_back();
		}
		
		if(all_(N))
		{
			result=1;
		}
	
		else 
		{
			for(size_t i = 0 ; i < N.size() ;)
					{
					
						char temp = N[i];
						
						size_t j = i;
						for( ; j < N.size() ;j++ )
						{
							if(N[j] != temp)
							{
								if(temp =='+')
								{
									result  +=2; 
									size_t cpt =1;
//									cout<<j<<endl;
									for(size_t v =j; v < N.size() ;v++,cpt++)
									{
										if(N[v] !='-')
										{
											cpt--;
//											cout<<"*"<<cpt<<"*"<<endl;
											break;
										}
									} 
									j += cpt;

								}
								else
								{
//									cout<<"-";
									result+=1;

								}
								break;
							}
						}
//						cout<<j<<endl;
						i =j;

					}		
			
			
		}
		ecrire<<result<<endl;
	}
	}
	return 0;
}