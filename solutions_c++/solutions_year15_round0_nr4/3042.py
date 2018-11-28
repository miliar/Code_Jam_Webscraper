# include<iostream>
# include<conio.h>

using namespace std;

int main()
{
	int T,i;
	int product;
	int ans[100];
	int X,R,C;
	cin>>T;
	for(i=0;i<T;i++)
	{
		cin>>X>>R>>C;
		product=R*C;
		switch(X)
		{
		case 1:
			ans[i]=1; //Gabriel
			break;
		case 2:
			if(product%2==0)
				ans[i]=1;
			else
				ans[i]=0;
			break;
		case 3:
			if(product%3==0&&product/3>1)
				ans[i]=1;
			else
				ans[i]=0;
			break;
		case 4:
			if(product%4==0&&product/4>2)
				ans[i]=1;
			else
				ans[i]=0;
			break;
		}
	}
	for(i=0;i<T;i++)
		if(ans[i]==1)
			cout<<"\nCase #"<<i+1<<": GABRIEL";
		else
			cout<<"\nCase #"<<i+1<<": RICHARD";
	getch();
}