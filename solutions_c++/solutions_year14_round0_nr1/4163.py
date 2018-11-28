#include<iostream>
#include<stdio.h>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
int main()
{
	int i,j,t,k,n,a,b,r,ii,l;
	//fstream cin;
	double p,ans,x,y;
	vector<int>arr,brr;
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Quali\\A\\Small Input.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Quali\\A\\Small Output.txt","w",stdout);
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>r;
        arr.clear();
        brr.clear();
        for(i=1;i<5;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>l;
                if(i==r)
                    arr.push_back(l);
            }
        }
        cin>>r;
        for(i=1;i<5;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>l;
                if(i==r)
                {
                    for(ii=0;ii<4;ii++)
                    {
                        if(l==arr[ii])
                        {
                            brr.push_back(l);
                            break;
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<k<<": ";
        if(brr.size()==1)cout<<brr[0];
        else if(brr.size()==0)cout<<"Volunteer cheated!";
        else cout<<"Bad magician!";
        cout<<endl;

	}
	return 0;
}