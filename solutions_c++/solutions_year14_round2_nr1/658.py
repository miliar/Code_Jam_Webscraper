#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
string arr[101];
int brr[101];
int crr[101];
int main()
{
	long long r,T,t,i,j,k,cnt,l,m,g,b,n,x,sm,f;
	//fstream cin;
    char a;
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Round 1B\\A\\Small Input.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Round 1B\\A\\Small Output.txt","w",stdout);
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cout<<"Case #"<<k<<": ";
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>arr[i];
			brr[i]=0;
		}
        cnt=0;
        f=0;
		while(f==0)
		{
			a=arr[0][brr[0]];
            sm=0;
            m=n;
           
            for(i=0;i<n;i++)
            {
                j=0;
                if(arr[i][brr[i]]!=a)break;
                while(arr[i][brr[i]]==a&&brr[i]<arr[i].length())
                {
                    j++;
                    brr[i]++;
                }
                sm+=j;
                if(m>j)m=j;
                crr[i]=j;
                if(brr[i]>=arr[i].length())f=1;
                
            }
            if(i<n)f=1;
            m=0;
            for(j=0;j<n;j++)
                {
                    x=crr[0]-crr[j];
                    if(x<0)x=-x;
                    m+=x;
                }
            for(i=1;i<n;i++)
            {
                l=0;
                for(j=0;j<n;j++)
                {
                    x=crr[i]-crr[j];
                    if(x<0)x=-x;
                    l+=x;
                }
                if(l<m)m=l;
            }
            cnt+=m;
		}
        for(i=0;i<n;i++)
            if(brr[i]<arr[i].length())break;
		if(i<n)cout<<"Fegla Won"<<endl;
		else cout<<cnt<<endl;
	}
	return 0;
}