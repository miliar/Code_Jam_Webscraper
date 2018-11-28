#include<bits/stdc++.h>
using namespace std;

void flip(char *s,int i,int j)
{
	int k,l;
	char temp;
	for(k=i,l=j;k<=l;k++,l--)
		{
			temp=s[k];
			
			if(temp=='+')	
				temp='-';
			else
				temp='+';
				
			if(s[l]=='+')
				s[l]='-';
			else
				s[l]='+';
			s[k]=s[l];
			s[l]=temp;
		}
}

int main()
{
	int test;
	int cas=1;
	ifstream infile;
	ofstream outfile;
	
	infile.open("F.in");
	outfile.open("result5.txt");
	
	infile >> test;
	
	while(test--)
		{
			char s[101];
			int i=0;
			infile >> s;
			
			int l=strlen(s);
			int ops=0;
			
			for(i=l-1;i>=0;i--)
				{
					if(s[i]=='+')
						continue;
					else if(s[i]=='-')
						{
							if(s[0]=='-')
								{
									flip(s,0,i);
									ops+=1;
								}
							else if(s[0]=='+')
								{
									for(int k=0;k<i;k++)
										if(s[k]=='+')
											s[k]='-';
										else if(s[i]=='-')
											break;
											
									flip(s,0,i);
									ops+=2;		
								}
						}
				}
				
			outfile << "Case #"<<cas++<<": "<< ops <<endl;
		}
}
