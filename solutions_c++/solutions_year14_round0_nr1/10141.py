#include<iostream>
#include<fstream>


using namespace std;


int main()
{
int testno,i,row1,row2,set1[4][4],set2[4][4],k,j,ans,flag=2;

string line;
  ifstream myfile ("A-small-attempt0.in");

ofstream ansfile ("ans.in");

  if (ansfile.is_open())
{
  if (myfile.is_open())
  {
      myfile>>testno;
    
	
for(i=1;i<=testno;i++)
{
	myfile>>row1;

	for(j=0;j<4;j++)
	{
		for(k=0;k<4;k++)
		{
		myfile>>set1[j][k];
		}
	}




	myfile>>row2;

	for(j=0;j<4;j++)
	{
		for(k=0;k<4;k++)
		{
		myfile>>set2[j][k];
		}
	}


for(j=0;j<4;j++)
{
	for(k=0;k<4;k++)
	{
	
	if(set1[row1-1][j]==set2[row2-1][k])
	{

		if(flag==1)
		{
		flag=0;
		break;
		}
		else
		{
		flag=1;
		ans=set1[row1-1][j];
	
		}
	}
	
	}
	if(flag==0)
	break;

}





if(flag==0)
{
ansfile<<"Case #"<<i<<": Bad magician!"<<endl;
}
else if(flag==1){
cout<<ans;
ansfile<<"Case #"<<i<<": "<<ans<<endl;
}
else if(flag==2)
{
ansfile<<"Case #"<<i<<": Volunteer cheated!"<<endl;
}

flag=2;




}



    myfile.close();

//cout<<testno<<" "<<row1;
/*for(j=0;j<4;j++)
{
		for(k=0;k<4;k++)
		{
			cout<<set1[j][k]<<" ";
		}
		cout<<endl;

}

for(j=0;j<4;j++)
{
	for(k=0;k<4;k++)
	{
	cout<<set2[j][k]<<" ";
	}
	cout<<endl;

}

*/
}	
}
return 0;
}

