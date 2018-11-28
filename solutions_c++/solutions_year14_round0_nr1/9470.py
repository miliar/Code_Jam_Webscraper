#include<iostream>
using namespace std;
main()
{
	int t,i,j,k;
	cin>>t;
	for(k=1;k<=t;k++){
		int a[4][4],b[4][4],no,nt,c[17]={0},num,count=0;
		cin>>no;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>a[i][j];
		for(i=0;i<4;i++)
  			c[a[no-1][i]]++;
		cin>>nt;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>b[i][j];
		for(i=0;i<4;i++)
  			c[b[nt-1][i]]++;
		for(i=1;i<17;i++){
			if(c[i]==2){
				count++;
 				num=i;
			}
		}
		if(count>=2)
			cout<<"Case #"<<k<<": Bad magician!"<<endl;
		else if(count==1)
			cout<<"Case #"<<k<<": "<<num<<endl;	
		else if(count==0)
  			cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
	}
	return 0;
}
