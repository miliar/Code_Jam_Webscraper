#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		string s;
		cin>>s;
		int count[127]={0};
		for(int j=0;j<s.length();j++)
		{
			count[s[j]]++;
		}
		int cnt=0;
		string str="";
		int arr[2000];int l=0;
		int order[10]={0,2,4,6,8,5,7,3,1,9};
		for(int k=0;k<10;k++)
		{
			//cout<<count['N']<<" ****\n";
			int j=order[k];
			
			//cout<<j<<"****\n";
			cnt=0;
			switch(j)
			{
				case 0: 
						while(count['Z'] && count['E'] && count['R'] && count['O'])
						{
							count['Z']--;
							count['E']--;
							count['R']--;
							count['O']--;
							cnt++;
						}
						break;
				case 1: 
						while(count['O'] && count['N'] && count['E'] )
						{
							count['O']--;
							count['N']--;
							count['E']--;
							
							cnt++;
						}
						break;
				case 2: 
						while(count['T'] && count['W'] && count['O'])
						{
							count['T']--;
							count['W']--;
							count['O']--;
							cnt++;
						}
						break;
				case 3: 
						while(count['T'] && count['H'] && count['R'] && count['E']>=2 )
						{
							count['T']--;
							count['H']--;
							count['R']--;
							count['E']--;
														count['E']--;

							cnt++;
						}
						break;
				case 4: 
						//cout<<count['F'] <<" "<<count['O'] <<" "<<count['U'] <<" "<<count['R'] <<" ";
						while(count['F'] && count['O'] && count['U'] && count['R'])
						{
							count['F']--;
							count['O']--;
							count['U']--;
							count['R']--;
							cnt++;
						}
						break;
				case 5: 
						while(count['F'] && count['I'] && count['V'] && count['E'])
						{
							count['F']--;
							count['I']--;
							count['V']--;
							count['E']--;
							cnt++;
						}
						break;
				case 6: 
						while(count['S'] && count['I'] && count['X'] )
						{
							count['S']--;
							count['I']--;
							count['X']--;
							
							cnt++;
						}
						break;
				case 7: 
						while(count['S'] && count['E']>=2 && count['V'] && count['N'])
						{
							count['S']--;
							count['E']--;
							count['V']--;
							count['E']--;
							count['N']--;
							cnt++;
						}
						break;
				case 8: 
						while(count['E'] && count['I'] && count['G'] && count['H'] && count['T'])
						{
							count['E']--;
							count['I']--;
							count['G']--;
							count['H']--;
							count['T']--;
							cnt++;
						}
						break;
				case 9: 
						while(count['N']>=2 && count['I'] && count['E'])
						{
							count['N']--;
							count['I']--;
							count['N']--;
							count['E']--;
							cnt++;
						}
						break;
				
			}
			
				//cout<<cnt<<" "<<j<<"\n";

			while(cnt--)
			{
				//cout<<j<<" \n";
				arr[l++]=j;
				//cout<<j;
			}
		}
		sort(arr,arr+l);
		for(int m=0;m<l;m++)
		{
			cout<<arr[m];
		}
		cout<<"\n";
	}
}