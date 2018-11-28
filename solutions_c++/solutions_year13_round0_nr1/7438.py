#include<iostream>
using namespace std;
char a[4][4];
int count1,count2,count3;

void init()
{
  count1=count2=count3=0;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("zm.txt","w",stdout);
	int t,i,j,status;
	char c;
	cin>>t;
	int count=0;
	while(t--)
	{
       for(i=0;i<=3;i++)
		   for(j=0;j<=3;j++)
			   cin>>a[i][j];// ‰»Î
       status=0;
	   for(i=0;i<=3;i++)
	   {
		   init();
		   for(j=0;j<=3;j++)
		   {
			   if(a[i][j]=='X') count1++;
			   else if(a[i][j]=='O') count2++;
			   else if(a[i][j]=='T') count3++;
		   }
           if((count1==3&&count3==1)||count1==4) {status=1;c='X';break;}
		   if((count2==3&&count3==1)||count2==4) {status=1;c='O';break;}	   
	   }
       if(status==1)
	   {cout<<"Case #"<<++count<<": "<<c<<" won"<<endl;continue;}  //≈–∂œ∫·œÚ



	   for(i=0;i<=3;i++)
	   {
		   init();
		   for(j=0;j<=3;j++)
		   {
			   if(a[j][i]=='X') count1++;
			   else if(a[j][i]=='O') count2++;
			   else if(a[j][i]=='T') count3++;
		   }
           if((count1==3&&count3==1)||count1==4) {status=1;c='X';break;}
		   if((count2==3&&count3==1)||count2==4) {status=1;c='O';break;}	   
	   }
       if(status==1)
	   {cout<<"Case #"<<++count<<": "<<c<<" won"<<endl;continue;}  //≈–∂œ◊›œÚ
        

	    init();
		for(i=0;i<=3;i++)
		{
               if(a[i][i]=='X') count1++;
			   else if(a[i][i]=='O') count2++;
			   else if(a[i][i]=='T') count3++;
		}
		if((count1==3&&count3==1)||count1==4) {status=1;c='X';}
		if((count2==3&&count3==1)||count2==4) {status=1;c='O';}
	    if(status==1)
		 {cout<<"Case #"<<++count<<": "<<c<<" won"<<endl;continue;}

		init();
		for(i=0;i<=3;i++)
		{
               if(a[i][3-i]=='X') count1++;
			   else if(a[i][3-i]=='O') count2++;
			   else if(a[i][3-i]=='T') count3++;
		}
		if((count1==3&&count3==1)||count1==4) {status=1;c='X';}
		if((count2==3&&count3==1)||count2==4) {status=1;c='O';}
	    if(status==1)
		 {cout<<"Case #"<<++count<<": "<<c<<" won"<<endl;continue;}//≈–∂œ∂‘Ω«œﬂ

       for(i=0;i<=3;i++)
		   for(j=0;j<=3;j++)
		   {
			   if(a[i][j]=='.') {status=2;break;}
		   }

		   if(status==2) 
		   {cout<<"Case #"<<++count<<": Game has not completed"<<endl;continue;}
		   cout<<"Case #"<<++count<<": Draw"<<endl; 
        
	}
	return 0;
}