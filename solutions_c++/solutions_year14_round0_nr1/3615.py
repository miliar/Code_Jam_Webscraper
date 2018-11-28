#include<iostream>
#include<stdio.h>
#include<conio.h>
#include <fstream>
using namespace std;
int main()
{
	int T,cardArray1[4][4],cardArray2[4][4],r1,r2,i,j,k,count = 0,card;
	freopen("A-small-attempt0.in","r",stdin);freopen("practiceout.out","w",stdout);
    cin>>T;
   // cout<<T<<endl;
    for(i = 0;i < T;i++)
    {count = 0;
    card = 0;
    //cout<<i<<endl;
		cin>>r1;
		r1--;
		for(j = 0;j<4;j++)
			for(k = 0;k<4;k++)
			   cin>>cardArray1[j][k];
		cin>>r2;
		r2--;
		for(j = 0;j<4;j++)
			for(k = 0;k<4;k++)
			   cin>>cardArray2[j][k];
		for(j = 0;j < 4;j++)
		for(k = 0;k < 4;k++)
		if(cardArray1[r1][j] == cardArray2[r2][k])
		{card = cardArray1[r1][j];
		count++;
	    }
	    //cout<<count<<" "<<card<<endl;
		switch(count)
		{
			case 0:
				cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
				break;
			case 1:
				cout<<"Case #"<<i+1<<": "<<card<<endl;
				break;
			 default:
				cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}
    }
   // getch();
}
