#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>


//#define PI 3.1415926

using namespace std;



int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

	
	
	int T;
	string s;
	int n;


	input>>T;// cout<<n<<endl;
	
	int l,count,ans,point,counter=0;
	char c;

	int left[100]={0},right[100]={0};

	for(int i=0;i<T;i++)
	{

		input>>s>>n;

		l=s.length();
		point=ans=count=counter=0;
		for(int ii=0;ii<100;ii++)
			left[ii]=right[ii]=0;

		int j=0;
		while(j<l)
		{
			c=s[j];
			if((c!='a')&&(c!='o')&&(c!='e')&&(c!='i')&&(c!='u'))
			{

				if(!count)
					point=j;
					
				count++;

				if(j==l-1)
					if(count>=n)
				{
					left[counter]=point;
					right[counter++]=j;
				}
				
				
//				if(count>=n)
//				{
//					ans+=(j-n+2)*(l-j);
//				}
			}
			else
			{
				if(count>=n)
				{
					left[counter]=point;
					right[counter++]=j-1;
				}
				
				count=0;
			}
			j++;
		}

//		cout<<endl;
		
		if(counter!=0){
		ans+=((l-left[0]-n+1)+(l-right[0]))*(right[0]-left[0]-n+2)/2;
//		if(right[0]-left[0]==n-1)
//			ans++;

		ans+=(left[0])*(l-left[0]-n+1);

		int jj=1;
		while(jj<counter)
		{
			ans+=((l-left[jj]-n+1)+(l-right[jj]))*(right[jj]-left[jj]-n+2)/2;

			ans+=(left[jj]-right[jj-1]+n-2)*(l-left[jj]-n+1);
			jj++;
		}

		}

		output<<"Case #"<<i+1<<": "<<ans<<endl;
		
	}
		
	input.close();
	output.close();
//	system("pause");
	return 0;
}
