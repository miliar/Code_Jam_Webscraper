#include "iostream"
#include "fstream"
#include<conio.h>
using namespace std;
int main()
{
    int t,i,j,k,a,b,cnt,ans;
    int arr1[5][5],arr2[5][5];
    ifstream fin("a.in");
    ofstream fout("a.out");
    fin>>t;
    for(i=0;i<t;i++)
    {
    	fin>>a;
    	for(j=0;j<4;j++)
    		for(k=0;k<4;k++)
    			fin>>arr1[j][k];
    	fin>>b;
    	for(j=0;j<4;j++)
    		for(k=0;k<4;k++)
    			fin>>arr2[j][k];
    	cnt=0;
    	for(j=0;j<4;j++)
    		for(k=0;k<4;k++)
    		{
    			if(arr1[a-1][j]==arr2[b-1][k])
    			{
    				ans=arr1[a-1][j];
    				cnt++;
    			}
    		}
    	if(cnt==0)
    		fout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
    	else if(cnt>1)
    		fout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
    	else fout<<"Case #"<<i+1<<": "<<ans<<endl;
    		
    }
    cout<<"ok";
    getch();
    
}
