#include<bits/stdc++.h>
using namespace std;

int main()
{
	int test;
	int cas=1;
	
	ifstream infile;
	ofstream outfile;
	infile.open("large.in");
	outfile.open("result.txt");
	
	infile >> test;
	
	while(test--)
		{
			int n;
			
			infile >> n;
			
			if(n==0)
				{
					outfile <<"Case #"<<cas++<<": "<< "INSOMNIA" <<endl;
					continue;
				}
			int Hash[10]={0};
			int j=1;
			int result=n;
			string ultimate;
			int i,flag=0;
			
			while(flag==0)
				{
					int flag=1;
					
					result=n*j;
					j++;
					
					stringstream convert;
					convert << result;
					ultimate=convert.str();
					
				
					for(i=0;i<ultimate.length();i++)
						Hash[ultimate[i]-48]++;
						
					for(i=0;i<10;i++)
						{
							
							if(Hash[i]==0)
							{
								flag=0;
								break;
							}
						}
					
					
					if(flag==1)
						{
							outfile <<"Case #"<<cas++<<": "<< ultimate <<endl;
						//	outfile << ultimate << endl;
							break;
						}
					
				}
		}
	return 0;
}
