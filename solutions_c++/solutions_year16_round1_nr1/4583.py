#include<iostream>
#include<math.h>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	int T,l,high,low,mid,s;
	string S,S1;
	char arr[20],temp;
//	cout<<"enter the number of test cases";
//	cin>>T;
	ifstream in("A-small-attempt1(1).in");
	in>>s;
	T=s;
	for(int i=0;i<T;i++)
	{
		//cout<<"enter the string";
		in>>S;
		l=S.length();
		//cout<<l;
		arr[l]='0';
		mid=(l/2)+1;
		arr[mid]=S[0];
		low=mid;
		high=mid;
		
		for(int j=1;j<l;j++)
		{
			if(S[j]<=arr[high])
			{
				//cout<<"hi";
				high++;
				arr[high]=S[j];
		//		cout<<arr[high];
			}
			else if(S[j]>=arr[low])
			{
		//		cout<<"hi";
				
				low--;
				arr[low]=S[j];
		//		cout<<low<<arr[low];
			}
			else
			{
				high++;
				
				arr[high]=S[j];
			}
			
	}
	//int c=0;
		ofstream out;
		out.open("output7",ios::app);
			out<<"Case"<<" "<<"#"<<(i+1)<<":"<<" ";
		for(int q=low;q<=high;q++)
		{
			///S1[c]=arr[q];
			out<<arr[q];
		//	c++;
		}
		out<<endl;
		out.close();
		//cout<<"Case"<<" "<<"#"<<T<<":"<<" "<<S1;
	}
	return 0;
}
